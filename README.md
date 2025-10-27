# ASI Health Guardian Agent

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

## Project Overview

ASI Health Guardian is an intelligent multi-agent healthcare system built on the ASI Alliance infrastructure. It combines natural language understanding, medical knowledge reasoning, and autonomous agent communication to provide personalized health guidance and symptom analysis.

The system demonstrates the power of decentralized AI agents working together to solve real-world healthcare accessibility challenges.

## Agent Architecture

### Agent 1: Health Guardian (User Interface)
- **Name:** `health_guardian`
- **Address:** `agent1qg4n6jwk986w6jzqld2ft7awm6c695dn995svevet6rc6fjt2tgcj38ut6c`
- **Port:** 8000
- **Role:** Primary interface for user interaction via ASI:One chat protocol
- **Features:**
  - Natural language symptom collection
  - Conversation context management
  - User-friendly health guidance
  - Agent-to-agent communication coordination

### Agent 2: Medical Brain (Knowledge Engine)
- **Name:** `medical_brain`
- **Address:** `agent1qv9r6hdpszufw00l78567gm8uuq68pjv4tx6clw98f9uvfckvya8gd3qzz8`
- **Port:** 8001
- **Role:** Medical knowledge reasoning and analysis
- **Features:**
  - Comprehensive medical knowledge base
  - Multi-symptom pattern recognition
  - Emergency symptom detection
  - Evidence-based health recommendations

## Technologies Used

- **Fetch.ai uAgents Framework**: Autonomous agent communication and orchestration
- **SingularityNET MeTTa**: Knowledge graph for medical reasoning (with fallback)
- **Chat Protocol**: ASI:One integration for human-agent interaction
- **Agentverse**: Agent registry and deployment platform
- **Python 3.8+**: Core programming language

## Key Features

**Intelligent Symptom Analysis**
- Multi-symptom pattern recognition
- Context-aware health recommendations
- Emergency detection and alerting

**Comprehensive Medical Knowledge**
- Covers common symptoms: headache, fever, cough, fatigue, nausea, chest pain
- Condition identification and treatment suggestions
- Professional medical disclaimers and warnings

**Multi-Agent Collaboration**
- Autonomous agent-to-agent communication
- Distributed knowledge processing
- Coordinated response generation

**ASI:One Integration**
- Natural language chat interface
- Real-time conversation handling
- User-friendly interaction design

**Emergency Response System**
- Detects critical symptoms (chest pain, difficulty breathing)
- Provides immediate emergency guidance
- Prioritizes user safety

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Agentverse account (for deployment)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Sachita92/asi-health-guardian-agent.git
cd asi-health-guardian-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables (Optional)
Create a `.env` file for API keys if you want to use advanced AI features:
```bash
ANTHROPIC_API_KEY=your_api_key_here
# or
OPENAI_API_KEY=your_api_key_here
```

**Note:** The system works perfectly without API keys using the built-in medical knowledge base.

## Running Locally

### Start Medical Brain Agent (Terminal 1)
```bash
cd agents
python medical_brain.py
```

You should see:
```
Medical Brain Agent Starting...
Agent Address: agent1qv9r6hdpszufw00l78567gm8uuq68pjv4tx6clw98f9uvfckvya8gd3qzz8
```

### Start Health Guardian Agent (Terminal 2)
```bash
cd agents
python health_guardian.py
```

You should see:
```
Health Guardian Agent Starting...
Agent Address: agent1qg4n6jwk986w6jzqld2ft7awm6c695dn995svevet6rc6fjt2tgcj38ut6c
```

Both agents must be running simultaneously for full functionality.

## Deployment to Agentverse

### 1. Register Agents
1. Log in to [Agentverse](https://agentverse.ai)
2. Click "Create Agent" or "Deploy Agent"
3. Upload or paste agent code
4. Configure agent settings:
   - Name: `health_guardian` / `medical_brain`
   - Category: **Innovation Lab**
   - Enable **Chat Protocol**

### 2. Enable ASI:One Integration
- In Agentverse settings, enable Chat Protocol
- Your agents will be discoverable through ASI:One interface
- Users can interact via natural language chat

## Usage Examples

### Example 1: Single Symptom Analysis
**User:** "I have a headache"

**Response:**
- Possible conditions: Tension headache, Migraine, Dehydration
- Recommended actions: Rest, hydration, pain relief
- Warning signs to watch for

### Example 2: Multi-Symptom Analysis
**User:** "I have a fever and cough"

**Response:**
- Possible conditions: Common cold, Flu, Viral infection
- Comprehensive treatment recommendations
- When to seek medical attention

### Example 3: Emergency Detection
**User:** "I have severe chest pain"

**Response:**
- **EMERGENCY ALERT**
- Immediate instruction to call emergency services
- Critical safety guidance

## Project Structure

```
asi-health-guardian-agent/
├── agents/
│   ├── __init__.py              # Python package initialization
│   ├── health_guardian.py       # User interface agent
│   └── medical_brain.py         # Medical knowledge agent
├── knowledge/
│   └── medical_knowledge.metta  # MeTTa knowledge graph
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not in git)
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## Demo Video

[Demo Video Link] - *Coming Soon*

**Demo Highlights:**
- Agent initialization and communication
- Real-time symptom analysis
- Agent-to-agent message flow
- Emergency detection system
- Medical knowledge reasoning
- ASI:One integration

## Testing

The system has been tested with various scenarios:
- Single symptom queries (headache, fever, cough, fatigue, nausea)
- Multi-symptom analysis (fever + cough, headache + nausea)
- Emergency detection (chest pain, difficulty breathing)
- Agent-to-agent communication
- Chat Protocol integration
- Context preservation across conversations

## Medical Disclaimer

**IMPORTANT:** This system provides general health information only and is NOT a substitute for professional medical advice, diagnosis, or treatment. 

- Always consult with qualified healthcare providers for medical concerns
- In case of emergency, call your local emergency number immediately
- This is an educational demonstration project
- Not intended for actual medical diagnosis or treatment

## ASI Alliance Hackathon Submission

This project is submitted for the **ASI Alliance Hackathon: Build Autonomous AI Agents**.

### Judging Criteria Addressed:

**Functionality & Technical Implementation (25%)**
- Fully functional multi-agent system
- Real-time agent communication
- Robust error handling
- Comprehensive medical knowledge base

**Use of ASI Alliance Tech (20%)**
- Fetch.ai uAgents framework
- Chat Protocol for ASI:One integration
- Agentverse deployment
- MeTTa knowledge graph structure
- Agent discovery and orchestration

**Innovation & Creativity (20%)**
- Novel approach to healthcare accessibility
- Multi-agent medical reasoning
- Emergency detection system
- Context-aware conversations

**Real-World Impact (20%)**
- Addresses healthcare accessibility challenges
- Provides immediate health guidance
- Could reduce unnecessary ER visits
- Scalable to global populations

**User Experience & Presentation (15%)**
- Natural language interface
- Clear, actionable responses
- Professional documentation
- Easy deployment and testing

## Future Enhancements

- **AI Integration**: Add Claude/GPT for more natural conversations
- **Multi-language Support**: Expand to support multiple languages
- **Appointment Scheduling**: Integrate with healthcare providers
- **Health Tracking**: Monitor symptoms over time
- **Medication Reminders**: Alert users about medication schedules
- **Telemedicine Integration**: Connect users with doctors
- **Blockchain Records**: Secure health data on blockchain

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Sachita Sigdel**
- GitHub: [@Sachita92](https://github.com/Sachita92)
- Email: sachitasigdel0713@gmail.com

## Acknowledgments

- **ASI Alliance** for the hackathon opportunity and infrastructure
- **Fetch.ai** for the powerful uAgents framework
- **SingularityNET** for MeTTa knowledge graph technology
- The open-source community for inspiration and support

## Support & Resources

- [Fetch.ai Documentation](https://docs.fetch.ai)
- [SingularityNET MeTTa Docs](https://metta-lang.dev)
- [Agentverse Platform](https://agentverse.ai)
- [ASI Alliance Website](https://asi.ai)

---

**Built with love for accessible healthcare using ASI Alliance technology**

*Making health guidance accessible to everyone, everywhere, through the power of autonomous AI agents.*