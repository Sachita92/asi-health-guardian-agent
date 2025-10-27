;; Medical Knowledge Graph for Health Guardian
;; This represents medical relationships and reasoning

;; Symptom definitions
(: symptom Type)
(: headache symptom)
(: fever symptom)
(: cough symptom)
(: fatigue symptom)
(: nausea symptom)
(: dizziness symptom)
(: chest-pain symptom)
(: shortness-of-breath symptom)

;; Condition definitions
(: condition Type)
(: common-cold condition)
(: flu condition)
(: migraine condition)
(: tension-headache condition)
(: dehydration condition)
(: viral-infection condition)
(: bacterial-infection condition)
(: allergies condition)
(: anxiety condition)
(: heart-attack condition)

;; Severity levels
(: severity Type)
(: mild severity)
(: moderate severity)
(: severe severity)
(: emergency severity)

;; Symptom-Condition relationships
(has-symptom common-cold cough)
(has-symptom common-cold fatigue)
(has-symptom common-cold fever)

(has-symptom flu fever)
(has-symptom flu fatigue)
(has-symptom flu cough)
(has-symptom flu headache)

(has-symptom migraine headache)
(has-symptom migraine nausea)
(has-symptom migraine dizziness)

(has-symptom tension-headache headache)
(has-symptom tension-headache fatigue)

(has-symptom dehydration headache)
(has-symptom dehydration fatigue)
(has-symptom dehydration dizziness)

(has-symptom viral-infection fever)
(has-symptom viral-infection fatigue)

(has-symptom heart-attack chest-pain)
(has-symptom heart-attack shortness-of-breath)
(has-symptom heart-attack nausea)

;; Severity classification
(symptom-severity headache mild)
(symptom-severity fever moderate)
(symptom-severity cough mild)
(symptom-severity fatigue mild)
(symptom-severity nausea moderate)
(symptom-severity chest-pain emergency)
(symptom-severity shortness-of-breath emergency)

;; Treatment recommendations
(: treatment Type)
(: rest treatment)
(: hydration treatment)
(: pain-relief treatment)
(: antibiotics treatment)
(: emergency-care treatment)

(recommends-treatment common-cold rest)
(recommends-treatment common-cold hydration)

(recommends-treatment flu rest)
(recommends-treatment flu hydration)
(recommends-treatment flu pain-relief)

(recommends-treatment migraine rest)
(recommends-treatment migraine pain-relief)

(recommends-treatment dehydration hydration)
(recommends-treatment dehydration rest)

(recommends-treatment heart-attack emergency-care)

;; Emergency detection rules
(: emergency-symptom (-> symptom Bool))
(= (emergency-symptom chest-pain) True)
(= (emergency-symptom shortness-of-breath) True)
(= (emergency-symptom $other) False)

;; Condition likelihood based on symptom combination
(: diagnose (-> symptom symptom condition))
(= (diagnose fever cough) common-cold)
(= (diagnose fever fatigue) flu)
(= (diagnose headache nausea) migraine)
(= (diagnose chest-pain shortness-of-breath) heart-attack)

;; Risk assessment
(: risk-level (-> condition severity))
(= (risk-level common-cold) mild)
(= (risk-level flu) moderate)
(= (risk-level migraine) moderate)
(= (risk-level heart-attack) emergency)
(= (risk-level dehydration) moderate)

;; Time-based advice
(: duration Type)
(: acute duration)
(: chronic duration)

(duration-type common-cold acute)
(duration-type flu acute)
(duration-type migraine acute)
(duration-type tension-headache chronic)

;; Query functions for reasoning
(: get-conditions-for-symptom (-> symptom List))
(= (get-conditions-for-symptom $s)
   (match &self (has-symptom $c $s) $c))

(: get-treatments-for-condition (-> condition List))
(= (get-treatments-for-condition $c)
   (match &self (recommends-treatment $c $t) $t))

(: is-emergency (-> symptom Bool))
(= (is-emergency $s)
   (emergency-symptom $s))

;; Symptom correlation rules
(: correlated-symptoms (-> symptom symptom))
(correlated-symptoms fever fatigue)
(correlated-symptoms headache nausea)
(correlated-symptoms cough fever)
(correlated-symptoms chest-pain shortness-of-breath)

;; Age-specific considerations
(: age-group Type)
(: child age-group)
(: adult age-group)
(: elderly age-group)

;; Medication contraindications (simplified)
(: medication Type)
(: aspirin medication)
(: ibuprofen medication)
(: acetaminophen medication)

(safe-for-age aspirin adult)
(safe-for-age aspirin elderly)
(safe-for-age ibuprofen adult)
(safe-for-age ibuprofen elderly)
(safe-for-age acetaminophen child)
(safe-for-age acetaminophen adult)
(safe-for-age acetaminophen elderly)

;; Prevention tips
(: prevention Type)
(: hand-washing prevention)
(: vaccination prevention)
(: hydration prevention)
(: exercise prevention)
(: sleep prevention)

(prevents common-cold hand-washing)
(prevents common-cold hydration)
(prevents flu vaccination)
(prevents flu hand-washing)
(prevents dehydration hydration)
(prevents tension-headache sleep)
(prevents tension-headache exercise)