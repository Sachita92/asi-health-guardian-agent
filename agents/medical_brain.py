from datetime import datetime
from uuid import uuid4
import os
from dotenv import load_dotenv
from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    TextContent,
    chat_protocol_spec,
)

# Load environment variables
load_dotenv()

# Try to import MeTTa (optional)
try:
    from hyperon import MeTTa
    METTA_AVAILABLE = True
except ImportError:
    METTA_AVAILABLE = False
    print("⚠️  MeTTa not available. Using basic knowledge base.")

# Create the Medical Brain Agent
agent = Agent(
    name="medical_brain",
    seed="medical_brain_secret_seed_phrase_2024",
    port=8001,
    endpoint=["http://localhost:8001/submit"],
)

# Initialize chat protocol
chat_proto = Protocol(spec=chat_protocol_spec)

# Initialize MeTTa if available
metta = None
if METTA_AVAILABLE:
    try:
        metta = MeTTa()
        # Load knowledge base
        knowledge_path = os.path.join(os.path.dirname(__file__), '..', 'knowledge', 'medical_knowledge.metta')
        if os.path.exists(knowledge_path):
            with open(knowledge_path, 'r') as f:
                metta.run(f.read())
            print("✅ MeTTa knowledge graph loaded successfully!")
        else:
            print(f"⚠️  Knowledge file not found at {knowledge_path}")
            metta = None
    except Exception as e:
        print(f"⚠️  Error loading MeTTa: {e}")
        metta = None

# Medical knowledge base (fallback)
MEDICAL_KNOWLEDGE = {
    "headache": {
        "conditions": ["Tension headache", "Migraine", "Dehydration", "Eye strain"],
        "advice": [
            "Rest in a quiet, dark room",
            "Apply cold or warm compress",
            "Stay hydrated",
            "Avoid bright lights and loud sounds",
            "Consider over-the-counter pain relief"
        ],
        "warning": "Seek immediate care if headache is sudden and severe, or accompanied by fever, stiff neck, confusion, or vision changes."
    },
    "fever": {
        "conditions": ["Viral infection", "Bacterial infection", "Heat exhaustion", "Common cold", "Flu"],
        "advice": [
            "Monitor temperature regularly",
            "Stay well hydrated",
            "Rest and avoid strenuous activity",
            "Use fever-reducing medication as directed",
            "Wear light, breathable clothing"
        ],
        "warning": "Seek medical attention if fever exceeds 103°F (39.4°C), lasts more than 3 days, or is accompanied by severe symptoms."
    },
    "cough": {
        "conditions": ["Common cold", "Bronchitis", "Allergies", "Asthma", "Flu"],
        "advice": [
            "Stay hydrated with warm fluids",
            "Use honey (for adults and children over 1 year)",
            "Try steam inhalation",
            "Avoid irritants like smoke",
            "Consider cough suppressants if dry cough"
        ],
        "warning": "Consult a doctor if cough persists beyond 3 weeks, produces blood, or is accompanied by high fever or difficulty breathing."
    },
    "fatigue": {
        "conditions": ["Sleep deprivation", "Anemia", "Thyroid issues", "Depression", "Dehydration"],
        "advice": [
            "Ensure 7-9 hours of quality sleep",
            "Maintain regular exercise routine",
            "Eat balanced, nutritious meals",
            "Manage stress through relaxation techniques",
            "Stay hydrated throughout the day"
        ],
        "warning": "Persistent unexplained fatigue lasting more than 2 weeks should be evaluated by a healthcare provider."
    },
    "nausea": {
        "conditions": ["Food poisoning", "Gastritis", "Motion sickness", "Pregnancy", "Migraine"],
        "advice": [
            "Sip clear fluids slowly",
            "Eat bland foods (crackers, rice, toast)",
            "Avoid strong odors",
            "Get fresh air",
            "Try ginger tea or peppermint"
        ],
        "warning": "Seek immediate care if nausea is accompanied by severe abdominal pain, blood in vomit, signs of dehydration, or chest pain."
    },
    "chest pain": {
        "conditions": ["Heart attack", "Angina", "Muscle strain", "Anxiety"],
        "advice": [
            "🚨 CALL EMERGENCY SERVICES IMMEDIATELY",
            "Do not drive yourself",
            "Chew aspirin if not allergic",
            "Stay calm and rest"
        ],
        "warning": "⚠️ EMERGENCY: Chest pain can be life-threatening. Seek immediate medical attention!"
    }
}


def create_text_chat(text: str) -> ChatMessage:
    """Create a chat message with text content"""
    content = [TextContent(type="text", text=text)]
    return ChatMessage(
        timestamp=datetime.utcnow(),
        msg_id=uuid4(),
        content=content,
    )


def query_metta_knowledge(symptom: str) -> dict:
    """Query MeTTa knowledge graph for symptom information"""
    if not metta:
        return None
    
    try:
        # Query for conditions related to symptom
        result = metta.run(f"!(get-conditions-for-symptom {symptom})")
        return {"metta_result": str(result)}
    except Exception as e:
        print(f"MeTTa query error: {e}")
        return None


def analyze_symptoms(user_message: str) -> str:
    """Analyze symptoms using medical knowledge base and MeTTa"""
    message_lower = user_message.lower()
    
    # Check for emergency symptoms first
    emergency_keywords = ['chest pain', 'chest-pain', 'shortness of breath', 'difficulty breathing', 
                          'severe bleeding', 'unconscious', 'stroke', 'heart attack']
    
    for keyword in emergency_keywords:
        if keyword in message_lower:
            return (
                "🚨 **EMERGENCY ALERT** 🚨\n\n"
                "Based on your symptoms, you may be experiencing a medical emergency.\n\n"
                "**IMMEDIATE ACTIONS:**\n"
                "1. Call emergency services (911 or local emergency number) NOW\n"
                "2. Do not drive yourself\n"
                "3. Stay calm and sit or lie down\n"
                "4. If someone is with you, inform them\n\n"
                "⚠️ Do not wait or try to treat this yourself. Get emergency help immediately!"
            )
    
    # Find matching symptoms
    matched_symptoms = []
    for symptom, data in MEDICAL_KNOWLEDGE.items():
        if symptom in message_lower or symptom.replace(' ', '') in message_lower.replace(' ', ''):
            matched_symptoms.append((symptom, data))
            
            # Query MeTTa if available
            if metta:
                metta_result = query_metta_knowledge(symptom.replace(' ', '-'))
                if metta_result:
                    print(f"MeTTa analysis for {symptom}: {metta_result}")
    
    if not matched_symptoms:
        return (
            "🤔 I need more information to provide accurate guidance.\n\n"
            "Could you describe your symptoms in more detail? For example:\n"
            "• What are you feeling? (pain, discomfort, etc.)\n"
            "• Where is it located?\n"
            "• When did it start?\n"
            "• How severe is it (1-10)?\n\n"
            "💡 Common symptoms I can help with: headache, fever, cough, "
            "fatigue, nausea, chest pain, and more."
        )
    
    # Generate comprehensive response
    response = "🏥 **Medical Analysis**\n\n"
    
    if metta:
        response += "✨ *Analysis powered by MeTTa Knowledge Graph*\n\n"
    
    for symptom, data in matched_symptoms:
        response += f"**Symptom: {symptom.capitalize()}**\n\n"
        
        response += "**Possible Conditions:**\n"
        for condition in data["conditions"]:
            response += f"• {condition}\n"
        response += "\n"
        
        response += "**Recommended Actions:**\n"
        for advice in data["advice"]:
            response += f"✓ {advice}\n"
        response += "\n"
        
        response += f"⚠️ **Warning:** {data['warning']}\n\n"
    
    response += (
        "---\n\n"
        "**Important Disclaimer:**\n"
        "This is general health information and not a substitute for professional "
        "medical advice. Always consult with a qualified healthcare provider for "
        "diagnosis and treatment.\n\n"
        "🆘 **Seek immediate emergency care if you experience:**\n"
        "• Chest pain or pressure\n"
        "• Difficulty breathing\n"
        "• Severe bleeding\n"
        "• Loss of consciousness\n"
        "• Severe allergic reaction\n"
        "• Stroke symptoms (FAST: Face drooping, Arm weakness, Speech difficulty, Time to call 911)\n"
    )
    
    return response


@chat_proto.on_message(ChatMessage)
async def handle_analysis_request(ctx: Context, sender: str, msg: ChatMessage):
    """Handle incoming analysis requests from Health Guardian"""
    ctx.logger.info(f"Received analysis request from {sender}")
    
    # Send acknowledgement
    await ctx.send(
        sender,
        ChatAcknowledgement(
            timestamp=datetime.utcnow(),
            acknowledged_msg_id=msg.msg_id
        )
    )
    
    # Process the message
    for item in msg.content:
        if isinstance(item, TextContent):
            request_text = item.text
            ctx.logger.info(f"Analysis request: {request_text}")
            
            # Extract the actual user query
            if "ANALYZE:" in request_text:
                user_query = request_text.split("ANALYZE:")[1].split("CONTEXT:")[0].strip()
            else:
                user_query = request_text
            
            # Perform analysis
            analysis_result = analyze_symptoms(user_query)
            
            # Send result back to Health Guardian
            await ctx.send(sender, create_text_chat(analysis_result))
            ctx.logger.info("Analysis sent back to Health Guardian")


@chat_proto.on_message(ChatAcknowledgement)
async def handle_acknowledgement(ctx: Context, sender: str, msg: ChatAcknowledgement):
    """Handle message acknowledgements"""
    ctx.logger.info(f"Message {msg.acknowledged_msg_id} acknowledged by {sender}")


# Include chat protocol
agent.include(chat_proto, publish_manifest=True)


if __name__ == "__main__":
    print("=" * 60)
    print("🧠 Medical Brain Agent Starting...")
    print("=" * 60)
    print(f"Agent Address: {agent.address}")
    print(f"Agent Name: {agent.name}")
    print(f"MeTTa Status: {'✅ Enabled' if metta else '⚠️  Disabled (using fallback)'}")
    print("=" * 60)
    print("\n⚠️  IMPORTANT: Copy the agent address above!")
    print("Update MEDICAL_BRAIN_ADDRESS in health_guardian.py\n")
    
    agent.run()