# ASI Health Guardian Agent

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

## Project Overview

ASI Health Guardian is an intelligent healthcare agent built on the ASI Alliance infrastructure. It combines natural language understanding, medical knowledge reasoning, and autonomous processing to provide personalized health guidance and symptom analysis.

The system demonstrates the power of decentralized AI agents solving real-world healthcare accessibility challenges through modular, intelligent design.

---

## Agent Architecture

### Health Guardian AI (Integrated System)
- **Name:** `health_guardian`
- **Address:** `agent1qvywrugtv0nqxhheedynf68v6u3rpy0fg7r8hu52r8j8nmnxu3rqvdmqcsm`
- **Port:** 8000
- **Role:** Intelligent health assistant with integrated medical knowledge processing
- **Architecture:** Modular design combining user interface and medical analysis components

**Core Features:**
- Natural language symptom collection and analysis
- Comprehensive medical knowledge base (8 symptoms, dozens of conditions)
- Multi-symptom pattern recognition
- Emergency detection and alerting
- Evidence-based health recommendations
- ASI:One Chat Protocol integration

**System Design:**

The agent uses a modular architecture with integrated components:
- **User Interface Module**: Handles Chat Protocol communication and natural language interaction
- **Medical Knowledge Processor**: Analyzes symptoms using a comprehensive knowledge base
- **Emergency Detection System**: Identifies critical symptoms requiring immediate care
- **Response Generator**: Provides structured, actionable health guidance

This integrated approach ensures reliable performance while maintaining the modularity and separation of concerns found in multi-agent systems.

---

## Architecture Philosophy

**Design Approach:**

This project demonstrates a **modular integrated architecture** - combining the benefits of both multi-agent and single-agent systems:

**Advantages of This Approach:**
- **Reliability**: Eliminates inter-agent communication issues on Agentverse
- **Performance**: Faster response times (no network hops between agents)
- **Modularity**: Clear separation of concerns within the codebase
- **Maintainability**: Single deployment unit, easier debugging and updates
- **Scalability**: Can be easily extended with additional knowledge modules

**Future Multi-Agent Evolution:**

The system is architected to scale into a true distributed multi-agent network:
- Separate deployment of specialized medical knowledge engines
- Domain-specific agents (pediatrics, geriatrics, cardiology, etc.)
- Agent coordination for complex multi-specialty consultations
- Distributed knowledge processing across the ASI Alliance network
- Cross-chain medical data integration

**MeTTa Integration:**

The `knowledge/medical_knowledge.metta` file demonstrates the structure for advanced reasoning capabilities using SingularityNET's MeTTa. While the current implementation uses an integrated knowledge base for Agentverse reliability, the MeTTa graph shows the potential for sophisticated logical reasoning in future versions.

---

## Technologies Used

- **Fetch.ai uAgents Framework**: Autonomous agent creation and orchestration
- **Chat Protocol**: ASI:One integration for human-agent interaction  
- **Agentverse**: Agent deployment and discovery platform
- **Python 3.8+**: Core programming language
- **Comprehensive Medical Knowledge Base**: Evidence-based symptom analysis
- **MeTTa Knowledge Graph**: Structured medical knowledge representation

**Technical Stack:**
- Natural language processing for symptom understanding
- Rule-based medical reasoning with extensible knowledge base
- Emergency detection algorithms
- ASI:One Chat Protocol implementation
- Agentverse deployment and discovery

---

## Key Features

### **Intelligent Symptom Analysis**
- Multi-symptom pattern recognition
- Context-aware health recommendations
- Covers: Headache, Fever, Cough, Fatigue, Nausea, Sore throat, Dizziness, Chest pain

### **Comprehensive Medical Knowledge**
- 8 primary symptoms with detailed information
- Dozens of possible conditions
- Evidence-based treatment recommendations
- Prevention tips and wellness guidance
- Professional medical disclaimers

### **Emergency Response System**
- Real-time detection of critical symptoms
- Immediate emergency guidance (chest pain, difficulty breathing, etc.)
- Prioritizes user safety above all
- Clear instructions for emergency situations

### **Natural Language Interaction**
- Conversational interface via ASI:One
- Understands casual symptom descriptions
- Handles greetings and follow-up questions
- Provides clear, structured responses

### **Smart Query Handling**
- Known symptoms: Detailed medical analysis
- Unknown symptoms: General guidance and detail requests
- Greetings: Friendly, concise responses
- Emergency keywords: Immediate alert protocols

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Agentverse account (for deployment)

---

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

### 3. Environment Variables (Optional)
The system works perfectly without any API keys using the built-in medical knowledge base.

If you want to extend with AI capabilities:
```bash
# Create .env file (optional)
ANTHROPIC_API_KEY=your_api_key_here
# or
OPENAI_API_KEY=your_api_key_here
```

---

## Running Locally

### Start Health Guardian Agent
```bash
cd agents
python health_guardian.py
```

**Expected Output:**
```
Health Guardian Agent Starting...
Agent Address: agent1q...
Agent Name: health_guardian
```

The agent is now running and ready to analyze health symptoms!

**Local Testing:**
- Interact through Agentverse inspector
- Send Chat Protocol messages from another agent
- Test all features locally before deploying

---

## Deployment to Agentverse

### 1. Register Agent
1. Log in to [Agentverse](https://agentverse.ai)
2. Click "Create Agent"
3. Paste `health_guardian.py` code
4. Configure settings:
   - **Name**: `health_guardian`
   - **Category**: Innovation Lab    - **Enable Chat Protocol** 
### 2. Enable ASI:One Integration
- Verify Chat Protocol is enabled in settings
- Agent becomes discoverable through ASI:One interface
- Users can interact via natural language chat

### 3. Test Your Deployed Agent
Test with various queries:
- "Hello" - Friendly greeting
- "I have a headache" - Symptom analysis
- "I have fever and cough" - Multi-symptom
- "chest pain" - Emergency detection

---

## Usage Examples

### Example 1: Greeting
**User:** "Hello"

**Response:**
- Friendly welcome
- Brief explanation of capabilities
- Prompt to describe symptoms

---

### Example 2: Single Symptom Analysis
**User:** "I have a headache"

**Response:**
```
Medical Analysis & Recommendations

Symptom: HEADACHE

Possible Conditions:
   1. Tension headache
   2. Migraine
   3. Cluster headache
   4. Dehydration
   5. Eye strain
   6. Sinus infection

Recommended Actions:
   ✓ Rest in a quiet, dark room
   ✓ Apply cold or warm compress to head
   ✓ Stay well hydrated with water
   [... more detailed guidance ...]

Warning: Seek immediate care if headache is sudden and severe...
```

---

### Example 3: Multi-Symptom Analysis
**User:** "I have a fever and cough"

**Response:**
- Analysis of both fever AND cough
- Conditions like Common cold, Flu, COVID-19
- Comprehensive treatment for both symptoms
- Combined warning signs

---

### Example 4: Emergency Detection
**User:** "I have severe chest pain"

**Response:**
```
EMERGENCY ALERT 

Based on your symptoms, you may be experiencing a medical emergency.

IMMEDIATE ACTIONS:
1. Call emergency services (911) NOW
2. Do NOT drive yourself
3. Take emergency medication if prescribed
4. Stay calm, sit or lie down
5. Inform someone immediately

Do not wait! Professional help is critical!
```

---

### Example 5: Unknown Symptom
**User:** "My back hurts"

**Response:**
- Acknowledges the concern
- Provides general health guidance
- Asks for more specific details
- Suggests related symptoms to describe
- Safety recommendations

---

## Project Structure

```
asi-health-guardian-agent/
├── agents/
│   ├── __init__.py              # Python package initialization
│   └── health_guardian.py       # Main agent with integrated medical knowledge
├── knowledge/
│   └── medical_knowledge.metta  # MeTTa knowledge graph structure
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not in git)
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## Demo Video

**Watch the full demonstration:** [Health Guardian AI Demo](YOUR_VIDEO_LINK_HERE)

**Demo Highlights:**
- Agent deployment on Agentverse
- Real-time symptom analysis
- Multi-symptom handling
- Emergency detection system
- Medical knowledge reasoning
- ASI:One Chat Protocol integration
- Natural language interaction
- Professional medical guidance

---

## Testing Scenarios

The system has been thoroughly tested with:

**Single Symptom Queries:**
- Headache, Fever, Cough, Fatigue, Nausea, Sore throat, Dizziness

**Multi-Symptom Analysis:**
- Fever + Cough (Common cold, Flu)
- Headache + Nausea (Migraine)
- Multiple concurrent symptoms

**Emergency Detection:**
- Chest pain → Immediate emergency protocol
- Difficulty breathing → Critical alert
- Severe bleeding → Emergency response

**Edge Cases:**
- Unknown symptoms → Helpful general guidance
- Greetings → Appropriate friendly responses
- Non-medical queries → Polite redirection

**Integration Testing:**
- Chat Protocol functionality
- ASI:One interface
- Agentverse deployment
- Context preservation

---

## Medical Disclaimer

**IMPORTANT LEGAL NOTICE:**

This system provides **general health information for educational purposes only** and is **NOT** a substitute for professional medical advice, diagnosis, or treatment.

**Critical Points:**
- ❌ Not a licensed medical professional
- ❌ Not for actual medical diagnosis
- ❌ Not for treatment decisions
- Educational demonstration only
- Always consult qualified healthcare providers
- Call emergency services (911) for emergencies

**User Responsibility:**
- Always seek professional medical care for health concerns
- This is a technology demonstration project
- Do not rely solely on this system for medical decisions
- In case of emergency, contact emergency services immediately

---

## ASI Alliance Hackathon Submission

This project is submitted for the **ASI Alliance Hackathon: Build Autonomous AI Agents**.

### Judging Criteria Alignment:

#### **Functionality & Technical Implementation (25%)**
- Fully functional agent system with comprehensive features
- Real-time symptom analysis with intelligent reasoning
- Robust error handling and edge case management
- Extensive medical knowledge base with 8 symptoms, dozens of conditions
- Emergency detection algorithms
- Professional response generation

#### **Use of ASI Alliance Tech (20%)**
- **Fetch.ai uAgents Framework**: Core agent implementation
- **Chat Protocol**: Full ASI:One integration for natural language interaction
- **Agentverse**: Deployed and discoverable on the platform
- **MeTTa Knowledge Graph**: Structured medical knowledge (see `knowledge/` folder)
- **Agent Discovery**: Registered in Innovation Lab category
- **Autonomous Processing**: Independent symptom analysis and response generation

#### **Innovation & Creativity (20%)**
- Novel approach to healthcare accessibility through AI
- Modular integrated architecture (best of both worlds)
- Intelligent emergency detection system
- Context-aware conversation handling
- Smart query routing (greetings, symptoms, emergencies, unknown)
- Comprehensive medical disclaimers for user safety

#### **Real-World Impact & Usefulness (20%)**
- **Healthcare Accessibility**: 24/7 immediate health guidance
- **Global Reach**: Available to anyone with internet access
- **Cost Reduction**: Could reduce unnecessary ER visits
- **Decision Support**: Helps people know when to seek care
- **Safety First**: Emergency detection prioritizes user wellbeing
- **Educational**: Democratizes access to basic health information

#### **User Experience & Presentation (15%)**
- Clean, natural language interface
- Clear, structured, actionable responses
- Professional formatting and medical terminology
- Comprehensive documentation
- Easy deployment process
- Intuitive interaction patterns
- Well-organized information hierarchy

---

## Future Enhancements

### **Phase 1: Enhanced Coverage**
- Expand to 50+ symptoms and conditions
- Specialized knowledge for chronic conditions
- Mental health support and guidance
- Nutritional advice and wellness tips

### **Phase 2: Advanced AI Integration**
- Claude/GPT integration for more natural conversations
- Personalized responses based on user history
- Learning from user interactions
- Multi-turn diagnostic conversations

### **Phase 3: Global Accessibility**
- Multi-language support (Spanish, Hindi, Mandarin, etc.)
- Cultural sensitivity in health advice
- Region-specific medical guidelines
- Localized emergency contact information

### **Phase 4: Healthcare Integration**
- Appointment scheduling with healthcare providers
- Telemedicine video call integration
- Electronic health record (EHR) connectivity
- Prescription reminder system
- Medication interaction checking

### **Phase 5: Personal Health Tracking**
- Symptom tracking over time
- Health trend analysis
- Personalized wellness plans
- Preventive care recommendations
- Health goal setting and monitoring

### **Phase 6: Blockchain & Decentralization**
- Secure health data storage on blockchain
- User-owned health records
- Privacy-preserving data sharing
- Decentralized medical knowledge validation
- Token incentives for health data contribution

---

## Contributing

Contributions are welcome! This project is open source and community-driven.

### How to Contribute:
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Ideas:
- Add more symptoms and conditions
- Improve emergency detection algorithms
- Enhance natural language understanding
- Add multi-language support
- Create unit tests
- Improve documentation
- Fix bugs

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Key Points:**
- Free to use, modify, and distribute
- Commercial use allowed
- Attribution required
- No warranty provided

---

## Author

**Sachita Sigdel**
- GitHub: [@Sachita92](https://github.com/Sachita92)
- Email: sachitasigdel0713@gmail.com
- Project: [ASI Health Guardian Agent](https://github.com/Sachita92/asi-health-guardian-agent)

**Developed for:** ASI Alliance Hackathon 2024  
**Built with:** Love and commitment to accessible healthcare

---

## Acknowledgments

- **ASI Alliance** - For hosting this hackathon and building the decentralized AI ecosystem
- **Fetch.ai** - For the powerful and intuitive uAgents framework
- **SingularityNET** - For MeTTa and advanced reasoning capabilities
- **Agentverse Team** - For the deployment platform and developer tools
- **Open Source Community** - For inspiration, tools, and support
- **Healthcare Workers** - For their dedication that inspired this project

---

## Support & Resources

### Official Documentation:
- [Fetch.ai Documentation](https://docs.fetch.ai) - uAgents framework guides
- [SingularityNET MeTTa Docs](https://metta-lang.dev) - Knowledge graph reasoning
- [Agentverse Platform](https://agentverse.ai) - Agent deployment
- [ASI Alliance Website](https://asi.ai) - Decentralized AI ecosystem

### Project Resources:
- **GitHub Repository**: [asi-health-guardian-agent](https://github.com/Sachita92/asi-health-guardian-agent)
- **Demo Video**: [Watch on YouTube](YOUR_VIDEO_LINK)
- **Issues & Bug Reports**: [GitHub Issues](https://github.com/Sachita92/asi-health-guardian-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Sachita92/asi-health-guardian-agent/discussions)

### Getting Help:
- Open an issue on GitHub
- Check existing documentation
- Review demo video for examples
- Consult ASI Alliance community

---

## Project Vision

**Mission:**  
Making quality healthcare guidance accessible to everyone, everywhere, through the power of autonomous AI agents.

**Vision:**  
A world where anyone can instantly access reliable health information, understand their symptoms, and make informed decisions about their wellbeing - regardless of location, income, or access to traditional healthcare.

**Values:**
- **Accessibility**: Healthcare information should be free and available to all
- **Safety**: User wellbeing is the top priority
- **Privacy**: Health data must be protected
- **Accuracy**: Information must be evidence-based and reliable
- **Empowerment**: People should be empowered to understand their health

---

**Built with love for accessible healthcare using ASI Alliance technology**

*Making health guidance accessible to everyone, everywhere, through the power of autonomous AI agents.*

---

© 2024 Sachita Sigdel. Licensed under MIT License.