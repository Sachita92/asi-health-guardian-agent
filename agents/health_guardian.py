from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    StartSessionContent,
    TextContent,
    EndSessionContent,
    chat_protocol_spec,
)
from datetime import datetime
from uuid import uuid4

# Create the Health Guardian Agent (with integrated medical knowledge)
agent = Agent(
    name="health_guardian",
    seed="health_guardian_final_combined_v1",
)

# Initialize chat protocol
chat_proto = Protocol(spec=chat_protocol_spec)

# Comprehensive Medical Knowledge Base
MEDICAL_KNOWLEDGE = {
    "headache": {
        "conditions": ["Tension headache", "Migraine", "Cluster headache", "Dehydration", "Eye strain", "Sinus infection"],
        "advice": [
            "Rest in a quiet, dark room",
            "Apply cold or warm compress to head",
            "Stay well hydrated with water",
            "Avoid bright lights and loud sounds",
            "Try relaxation techniques and deep breathing",
            "Consider over-the-counter pain relief (ibuprofen, acetaminophen)",
            "Maintain regular sleep schedule"
        ],
        "warning": "Seek immediate care if headache is sudden and severe ('thunderclap'), or accompanied by fever, stiff neck, confusion, vision changes, difficulty speaking, or numbness.",
        "prevention": "Stay hydrated, maintain good posture, manage stress, get regular sleep, limit screen time"
    },
    "fever": {
        "conditions": ["Viral infection (flu, cold)", "Bacterial infection", "COVID-19", "Heat exhaustion", "Urinary tract infection"],
        "advice": [
            "Monitor temperature every 4 hours",
            "Stay well hydrated with water, clear broths, and electrolyte drinks",
            "Rest adequately and avoid strenuous activity",
            "Use fever-reducing medication as directed (acetaminophen or ibuprofen)",
            "Wear light, breathable clothing",
            "Use lukewarm sponge baths if needed",
            "Maintain cool room temperature"
        ],
        "warning": "Seek medical attention if fever exceeds 103°F (39.4°C), lasts more than 3 days, occurs with severe headache, rash, difficulty breathing, chest pain, or persistent vomiting.",
        "prevention": "Wash hands frequently, get vaccinated, avoid sick contacts, maintain good hygiene"
    },
    "cough": {
        "conditions": ["Common cold", "Bronchitis", "Pneumonia", "Allergies", "Asthma", "GERD", "Post-nasal drip"],
        "advice": [
            "Stay hydrated with warm fluids (tea, soup, warm water)",
            "Use honey for soothing (for adults and children over 1 year)",
            "Try steam inhalation or humidifier",
            "Avoid irritants like smoke, strong perfumes, and pollution",
            "Elevate head while sleeping",
            "Consider cough suppressants for dry cough or expectorants for productive cough",
            "Gargle with warm salt water"
        ],
        "warning": "Consult a doctor if cough persists beyond 3 weeks, produces blood, is accompanied by high fever (>101°F), difficulty breathing, chest pain, or unexplained weight loss.",
        "prevention": "Avoid smoking, stay away from allergens, wash hands regularly, get flu vaccine"
    },
    "fatigue": {
        "conditions": ["Sleep deprivation", "Anemia", "Thyroid problems", "Depression", "Chronic fatigue syndrome", "Diabetes", "Heart disease"],
        "advice": [
            "Ensure 7-9 hours of quality sleep nightly",
            "Maintain regular exercise routine (30 min daily)",
            "Eat balanced, nutritious meals with lean protein",
            "Manage stress through meditation, yoga, or counseling",
            "Stay hydrated throughout the day",
            "Limit caffeine and alcohol",
            "Take short breaks during work",
            "Get sunlight exposure during the day"
        ],
        "warning": "Persistent unexplained fatigue lasting more than 2 weeks, especially with other symptoms like weight changes, shortness of breath, or depression, should be evaluated by a healthcare provider.",
        "prevention": "Maintain healthy sleep habits, regular exercise, balanced diet, stress management"
    },
    "nausea": {
        "conditions": ["Food poisoning", "Gastritis", "Gastroenteritis", "Motion sickness", "Pregnancy", "Migraine", "Medication side effects"],
        "advice": [
            "Sip clear fluids slowly (water, ginger ale, clear broth)",
            "Eat bland foods when able (crackers, rice, toast, bananas)",
            "Avoid strong odors, greasy, or spicy foods",
            "Get fresh air and avoid lying down immediately after eating",
            "Try ginger tea, peppermint tea, or lemon water",
            "Eat small, frequent meals instead of large ones",
            "Rest and avoid sudden movements"
        ],
        "warning": "Seek immediate care if nausea is accompanied by severe abdominal pain, blood in vomit, signs of dehydration (dark urine, dizziness), chest pain, severe headache, or high fever.",
        "prevention": "Eat slowly, avoid trigger foods, stay hydrated, practice food safety"
    },
    "chest pain": {
        "conditions": ["⚠️ HEART ATTACK", "Angina", "Panic attack", "Muscle strain", "Acid reflux", "Pneumonia"],
        "advice": [
            "🚨 CALL EMERGENCY SERVICES (911) IMMEDIATELY",
            "Do not drive yourself - wait for ambulance",
            "Chew aspirin if not allergic (ask dispatcher)",
            "Stay calm and sit or lie down",
            "Loosen tight clothing",
            "If someone is with you, inform them of your symptoms"
        ],
        "warning": "⚠️ EMERGENCY: Chest pain can be life-threatening. Seek immediate medical attention! Especially if accompanied by shortness of breath, pain radiating to arm/jaw/back, sweating, nausea, or dizziness.",
        "prevention": "Maintain healthy weight, exercise regularly, eat heart-healthy diet, manage stress, don't smoke"
    },
    "sore throat": {
        "conditions": ["Viral pharyngitis", "Strep throat", "Tonsillitis", "Allergies", "Dry air", "GERD"],
        "advice": [
            "Gargle with warm salt water several times daily",
            "Stay hydrated with warm liquids (tea with honey, soup)",
            "Use throat lozenges or hard candy",
            "Rest your voice",
            "Use humidifier to add moisture to air",
            "Avoid irritants like smoke",
            "Take over-the-counter pain relievers"
        ],
        "warning": "See a doctor if sore throat is severe, lasts more than a week, is accompanied by high fever, difficulty swallowing or breathing, or white patches on tonsils.",
        "prevention": "Wash hands frequently, avoid sharing utensils, stay away from sick people"
    },
    "dizziness": {
        "conditions": ["Dehydration", "Low blood pressure", "Inner ear problems", "Anemia", "Low blood sugar", "Anxiety"],
        "advice": [
            "Sit or lie down immediately if dizzy",
            "Drink water slowly",
            "Avoid sudden position changes - rise slowly",
            "Eat something if blood sugar is low",
            "Focus on a fixed point",
            "Get fresh air if indoors",
            "Rest until dizziness passes"
        ],
        "warning": "Seek immediate medical help if dizziness is accompanied by chest pain, severe headache, loss of consciousness, difficulty speaking, numbness, or double vision.",
        "prevention": "Stay hydrated, rise slowly from sitting/lying, avoid alcohol, manage stress"
    }
}


def create_text_chat(text: str) -> ChatMessage:
    """Create a chat message with text content"""
    content = [TextContent(type="text", text=text)]
    return ChatMessage(
        timestamp=datetime.now(datetime.UTC) if hasattr(datetime, 'UTC') else datetime.utcnow(),
        msg_id=uuid4(),
        content=content,
    )


def analyze_symptoms(user_message: str) -> str:
    """Analyze symptoms using medical knowledge base"""
    message_lower = user_message.lower()
    
    # Check for emergency symptoms first
    emergency_keywords = ['chest pain', 'chest-pain', 'shortness of breath', 'difficulty breathing', 
                          'severe bleeding', 'unconscious', 'stroke', 'heart attack', 'can\'t breathe',
                          'choking', 'severe head injury', 'seizure']
    
    for keyword in emergency_keywords:
        if keyword in message_lower:
            return (
                "🚨 **EMERGENCY ALERT** 🚨\n\n"
                "Based on your symptoms, you may be experiencing a medical emergency.\n\n"
                "**IMMEDIATE ACTIONS:**\n"
                "1. ☎️ Call emergency services (911 or your local emergency number) NOW\n"
                "2. 🚗 Do NOT drive yourself - wait for ambulance\n"
                "3. 💊 If prescribed, take emergency medication (e.g., nitroglycerin for chest pain)\n"
                "4. 🧘 Stay calm, sit or lie down comfortably\n"
                "5. 👥 If someone is with you, inform them immediately\n\n"
                "⚠️ **Do not wait or try to treat this yourself. Professional medical help is critical!**\n\n"
                "Time is critical in emergencies. Help is on the way."
            )
    
    # Find matching symptoms
    matched_symptoms = []
    for symptom, data in MEDICAL_KNOWLEDGE.items():
        if symptom in message_lower or symptom.replace(' ', '') in message_lower.replace(' ', ''):
            matched_symptoms.append((symptom, data))
    
    # Check for greetings first
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings']
    if any(greeting in message_lower for greeting in greetings):
        return (
            "👋 **Hello! I'm Health Guardian AI**\n\n"
            "I'm here to help you with health concerns and symptom analysis.\n\n"
            "**How can I assist you today?**\n"
            "Simply describe any symptoms you're experiencing, and I'll provide guidance.\n\n"
            "**Examples:**\n"
            "• \"I have a headache\"\n"
            "• \"I'm feeling tired and have a fever\"\n"
            "• \"My stomach hurts\"\n\n"
            "What would you like help with? 💚"
        )
    
    if not matched_symptoms:
        # Check if they're describing something medical
        medical_keywords = ['pain', 'hurt', 'ache', 'sick', 'ill', 'feel', 'feeling', 'symptom', 
                           'problem', 'issue', 'discomfort', 'trouble', 'disease', 'condition']
        
        is_medical_query = any(keyword in message_lower for keyword in medical_keywords)
        
        if is_medical_query:
            return (
                "🤔 **I understand you're not feeling well.**\n\n"
                "While I don't have specific information about this particular symptom in my current knowledge base, "
                "I can offer some general guidance:\n\n"
                "**📋 Please provide more details:**\n"
                "• What exactly are you experiencing?\n"
                "• Where is the discomfort located?\n"
                "• When did it start?\n"
                "• How severe is it (1-10 scale)?\n"
                "• Any other symptoms accompanying it?\n\n"
                "**💡 Common symptoms I specialize in:**\n"
                "Headache, Fever, Cough, Fatigue, Nausea, Sore throat, Dizziness, Chest pain\n\n"
                "**⚕️ General Advice:**\n"
                "• If symptoms are severe or worsening, consult a healthcare provider\n"
                "• Stay hydrated and get adequate rest\n"
                "• Monitor your symptoms and note any changes\n"
                "• Seek immediate care if you experience severe pain, difficulty breathing, or other alarming symptoms\n\n"
                "**📞 Need immediate help?**\n"
                "If you're experiencing a medical emergency, please call emergency services (911) immediately.\n\n"
                "Would you like to describe your symptoms in more detail, or ask about one of the conditions I specialize in?"
            )
        else:
            return (
                "👋 **I'm here to help with health-related concerns!**\n\n"
                "I specialize in analyzing symptoms and providing health guidance.\n\n"
                "**What I can help with:**\n"
                "💊 Headache, Fever, Cough, Fatigue, Nausea, Sore throat, Dizziness, Chest pain, and more.\n\n"
                "**How to get started:**\n"
                "Simply describe any health symptoms you're experiencing.\n\n"
                "**Example:** \"I have a headache and feel tired\"\n\n"
                "What health concern can I help you with today? 💚"
            )
    
    # Generate comprehensive response
    response = "🏥 **Medical Analysis & Recommendations**\n\n"
    
    for symptom, data in matched_symptoms:
        response += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        response += f"📋 **Symptom: {symptom.upper()}**\n"
        response += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        response += "**🔍 Possible Conditions:**\n"
        for i, condition in enumerate(data["conditions"], 1):
            response += f"   {i}. {condition}\n"
        response += "\n"
        
        response += "**💡 Recommended Actions:**\n"
        for i, advice in enumerate(data["advice"], 1):
            response += f"   ✓ {advice}\n"
        response += "\n"
        
        if "prevention" in data:
            response += f"**🛡️ Prevention Tips:**\n   • {data['prevention']}\n\n"
        
        response += f"⚠️ **When to Seek Medical Help:**\n   {data['warning']}\n\n"
    
    response += (
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "**📢 Important Medical Disclaimer:**\n"
        "This is general health information for educational purposes only and is NOT a substitute "
        "for professional medical advice, diagnosis, or treatment. Always consult with a qualified "
        "healthcare provider for personalized medical guidance.\n\n"
        "**🆘 Seek IMMEDIATE Emergency Care if you experience:**\n"
        "• 🫀 Chest pain or pressure\n"
        "• 🫁 Severe difficulty breathing\n"
        "• 🩸 Heavy bleeding that won't stop\n"
        "• 😵 Loss of consciousness or severe confusion\n"
        "• 🤒 Severe allergic reaction (throat swelling, can't breathe)\n"
        "• 🧠 Stroke symptoms: FAST (Face drooping, Arm weakness, Speech difficulty, Time to call 911)\n"
        "• 🚨 Any symptom that feels life-threatening\n\n"
        "**Need more help?** Feel free to describe additional symptoms or ask follow-up questions!\n"
        "I'm here to help guide you toward better health. 💚"
    )
    
    return response


@chat_proto.on_message(ChatMessage)
async def handle_user_message(ctx: Context, sender: str, msg: ChatMessage):
    """Handle incoming messages from users"""
    ctx.logger.info(f"Health Guardian received message from {sender}")
    
    # Send acknowledgement
    await ctx.send(
        sender, 
        ChatAcknowledgement(
            timestamp=datetime.now(datetime.UTC) if hasattr(datetime, 'UTC') else datetime.utcnow(),
            acknowledged_msg_id=msg.msg_id
        )
    )
    
    # Process message content
    for item in msg.content:
        if isinstance(item, StartSessionContent):
            ctx.logger.info(f"Session started with {sender}")
            welcome_msg = (
                "👋 **Welcome to Health Guardian AI!**\n\n"
                "I'm your intelligent health assistant, ready to help you understand symptoms and provide health guidance.\n\n"
                "**🏥 What I Can Help You With:**\n"
                "• 🤒 Symptom analysis (Headache, Fever, Cough, Fatigue, Nausea, Sore throat, Dizziness, Chest pain)\n"
                "• 💊 Treatment recommendations and home remedies\n"
                "• ⚕️ When to seek professional medical care\n"
                "• 🚨 Emergency symptom detection\n"
                "• 🛡️ Prevention and wellness tips\n\n"
                "**📝 To Get Started:**\n"
                "Just describe your symptoms naturally:\n"
                "• \"I have a headache\"\n"
                "• \"I've been feeling tired and have a fever\"\n"
                "• \"My throat hurts\"\n\n"
                "**💡 For best results:** Include when symptoms started, severity (1-10), and any other symptoms.\n\n"
                "**🔒 Privacy:** Your health information is confidential.\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                "**❓ What health concerns can I help you with today?**"
            )
            await ctx.send(sender, create_text_chat(welcome_msg))
            
        elif isinstance(item, TextContent):
            user_message = item.text
            ctx.logger.info(f"Analyzing user message: {user_message}")
            
            # Analyze symptoms directly using integrated medical knowledge
            analysis_result = analyze_symptoms(user_message)
            
            # Send result to user
            await ctx.send(sender, create_text_chat(analysis_result))
            ctx.logger.info("Analysis sent to user")
            
        elif isinstance(item, EndSessionContent):
            ctx.logger.info(f"Session ended with {sender}")
            goodbye_msg = (
                "👋 **Thank you for using Health Guardian!**\n\n"
                "Remember:\n"
                "• Stay healthy and take care of yourself 💚\n"
                "• Always consult healthcare professionals for serious concerns\n"
                "• I'm here anytime you need health guidance\n\n"
                "Feel better soon! Don't hesitate to reach out again. 🌟"
            )
            await ctx.send(sender, create_text_chat(goodbye_msg))


@chat_proto.on_message(ChatAcknowledgement)
async def handle_acknowledgement(ctx: Context, sender: str, msg: ChatAcknowledgement):
    """Handle message acknowledgements"""
    ctx.logger.info(f"Acknowledgement received from {sender}")


# Include chat protocol and publish manifest
agent.include(chat_proto, publish_manifest=True)

if __name__ == "__main__":
    agent.run()