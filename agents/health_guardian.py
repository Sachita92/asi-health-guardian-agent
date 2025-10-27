from datetime import datetime
from uuid import uuid4
import os
from dotenv import load_dotenv
from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    StartSessionContent,
    TextContent,
    EndSessionContent,
    chat_protocol_spec,
)

# Load environment variables
load_dotenv()

# Create the Health Guardian Agent
agent = Agent(
    name="health_guardian",
    seed="health_guardian_secret_seed_phrase_2024",
    port=8000,
    endpoint=["http://localhost:8000/submit"],
)

# Initialize chat protocol
chat_proto = Protocol(spec=chat_protocol_spec)

# Medical Brain Agent address
MEDICAL_BRAIN_ADDRESS = "agent1qv9r6hdpszufw00l78567gm8uuq68pjv4tx6clw98f9uvfckvya8gd3qzz8"

# Store conversation context
conversation_context = {}


def create_text_chat(text: str) -> ChatMessage:
    """Create a chat message with text content"""
    content = [TextContent(type="text", text=text)]
    return ChatMessage(
        timestamp=datetime.utcnow(),
        msg_id=uuid4(),
        content=content,
    )


@chat_proto.on_message(ChatMessage)
async def handle_user_message(ctx: Context, sender: str, msg: ChatMessage):
    """Handle incoming messages from users or other agents"""
    ctx.logger.info(f"Received message from {sender}")
    
    # Send acknowledgement
    await ctx.send(
        sender, 
        ChatAcknowledgement(
            timestamp=datetime.utcnow(), 
            acknowledged_msg_id=msg.msg_id
        )
    )
    
    # Process message content
    for item in msg.content:
        if isinstance(item, StartSessionContent):
            ctx.logger.info(f"Session started with {sender}")
            welcome_msg = (
                "👋 Hello! I'm your Health Guardian AI.\n\n"
                "I can help you with:\n"
                "• Symptom analysis\n"
                "• Health advice\n"
                "• Medication information\n"
                "• General wellness tips\n\n"
                "What health concerns can I help you with today?"
            )
            await ctx.send(sender, create_text_chat(welcome_msg))
            
        elif isinstance(item, TextContent):
            user_message = item.text
            ctx.logger.info(f"User message: {user_message}")
            
            # Store context
            if sender not in conversation_context:
                conversation_context[sender] = []
            conversation_context[sender].append(user_message)
            
            # Check if Medical Brain address is configured
            if MEDICAL_BRAIN_ADDRESS == "agent1q...":
                # Simple response without AI (for testing)
                response = await generate_simple_response(user_message)
            else:
                # Forward to Medical Brain for analysis
                analysis_request = create_text_chat(
                    f"ANALYZE: {user_message}\n"
                    f"CONTEXT: {conversation_context.get(sender, [])}"
                )
                await ctx.send(MEDICAL_BRAIN_ADDRESS, analysis_request)
                
                # For now, acknowledge we're processing
                response = (
                    "🔍 I'm analyzing your symptoms with my medical knowledge base. "
                    "One moment please..."
                )
            
            await ctx.send(sender, create_text_chat(response))
            
        elif isinstance(item, EndSessionContent):
            ctx.logger.info(f"Session ended with {sender}")
            if sender in conversation_context:
                del conversation_context[sender]
            goodbye_msg = (
                "Thank you for using Health Guardian! "
                "Stay healthy and don't hesitate to reach out anytime. 🌟"
            )
            await ctx.send(sender, create_text_chat(goodbye_msg))


async def generate_simple_response(user_message: str) -> str:
    """Generate simple responses without AI API (for testing)"""
    message_lower = user_message.lower()
    
    # Symptom keywords
    if any(word in message_lower for word in ['headache', 'pain', 'hurt', 'ache']):
        return (
            "I understand you're experiencing pain. Here are some general tips:\n\n"
            "• Rest in a quiet, dark room\n"
            "• Stay hydrated\n"
            "• Consider over-the-counter pain relief\n"
            "• If severe or persistent, consult a doctor\n\n"
            "⚠️ This is general advice. Please consult a healthcare professional "
            "for personalized medical guidance."
        )
    
    elif any(word in message_lower for word in ['fever', 'temperature', 'hot']):
        return (
            "For fever management:\n\n"
            "• Monitor your temperature regularly\n"
            "• Stay hydrated with water and clear fluids\n"
            "• Rest adequately\n"
            "• Use fever-reducing medication if needed\n"
            "• Seek medical attention if fever exceeds 103°F (39.4°C)\n\n"
            "⚠️ Always consult a healthcare provider for medical concerns."
        )
    
    elif any(word in message_lower for word in ['cold', 'cough', 'flu']):
        return (
            "For cold and flu symptoms:\n\n"
            "• Get plenty of rest\n"
            "• Drink warm fluids (tea, soup)\n"
            "• Use humidifier for congestion\n"
            "• Gargle with salt water for sore throat\n"
            "• Consider vitamin C and zinc supplements\n\n"
            "⚠️ If symptoms worsen or persist beyond 7-10 days, see a doctor."
        )
    
    else:
        return (
            "I'm here to help with your health concerns. Could you provide more details?\n\n"
            "For example:\n"
            "• What symptoms are you experiencing?\n"
            "• When did they start?\n"
            "• How severe are they?\n\n"
            "💡 The more information you provide, the better I can assist you!"
        )


@chat_proto.on_message(ChatAcknowledgement)
async def handle_acknowledgement(ctx: Context, sender: str, msg: ChatAcknowledgement):
    """Handle message acknowledgements"""
    ctx.logger.info(f"Message {msg.acknowledged_msg_id} acknowledged by {sender}")


# Include chat protocol and publish manifest
agent.include(chat_proto, publish_manifest=True)


if __name__ == "__main__":
    print("=" * 60)
    print("🏥 Health Guardian Agent Starting...")
    print("=" * 60)
    print(f"Agent Address: {agent.address}")
    print(f"Agent Name: {agent.name}")
    print("=" * 60)
    print("\n⚠️  IMPORTANT: Copy the agent address above!")
    print("You'll need it for agent communication and Agentverse.\n")
    
    agent.run()