**🎙️ Autonomous AI Voice Agent (Local, Open-Source)**
**📌 Project Overview**

This project implements an autonomous AI voice agent designed to handle goal-oriented phone conversations in a controlled and realistic way.
The agent can initiate a call, follow a pre-defined objective, adapt to user responses, handle objections, and conclude the interaction without human intervention.

Primary use case:
Simulated customer support call to cancel a subscription, including retention attempts and confirmations.

✅ Fully local
✅ Open-source models only
✅ No paid or hosted APIs

///////////////////////////////////////////////////////////////////////////////////////////////////

**✨ Key Capabilities**

🗣️ Speech-to-Text (STT)
Converts user audio into text using a local transcription model.

🔊 Text-to-Speech (TTS)
Generates spoken responses from agent text output.

🧠 Conversation Memory
Maintains dialogue history to ensure context-aware responses.

🎯 Intent Handling
Detects user intent (confirmation, objection, offer) via rule-based logic.

///////////////////////////////////////////////////////////////////////////////////////////////////

**🏗️ System Architecture**

|High-Level Flow

|User Speech
   ↓
|Speech-to-Text (Whisper)
   ↓
|Intent Detection + Dialogue State Manager
   ↓
|Response Selection (Rule-Based Logic)
   ↓
|Text-to-Speech
   ↓
|Agent Speech Output

Data Flow Explanation

User audio is captured locally.

STT converts speech to text.

1.)Dialogue manager evaluates:

2.)Current state

3.)Detected intent

4.)Conversation history

5.)Agent selects the next response.

6.)TTS converts text to speech.

7.)Loop continues until a terminal state is reached.

////////////////////////////////////////////////////////////////////////////////////////////////////////////

**🔄 Dialogue Control Logic**

The agent is controlled using a finite state machine (FSM).

Example States

--INITIATE_CALL

--REQUEST_CANCELLATION

--HANDLE_RETENTION_OFFER

--CONFIRM_CANCELLATION

--END_CALL

**Adaptive Behavior**

--💬 User offers a discount → agent rejects politely

--✅ User confirms cancellation → agent closes call

--❓ Unexpected response → fallback logic keeps conversation on track

This ensures predictable behavior with controlled flexibility.

///////////////////////////////////////////////////////////////////////////////////////////////////

**🧩 Model & Tooling Choices**
--Speech-to-Text — Faster-Whisper

--Open-source and optimized for local inference

--Good balance between speed and accuracy

--Suitable for near real-time transcription

--Text-to-Speech — Local TTS Engine

--Fully offline synthesis

--No external service dependency

--Sufficient quality for demonstration and evaluation

--Dialogue Control — Rule-Based FSM

--Transparent and deterministic

--Easy to debug and explain

--Ideal for constrained, goal-driven conversations

**🔁 Scripted + Adaptive Dialogue**
Follows a fixed goal while adapting to real-time user responses.

//////////////////////////////////////////////////////////////////////////////////////////////////

**🤖 Autonomy Explanation**

**The agent is autonomous within defined boundaries:**

--Decides responses based on:

--Dialogue state

--Detected user intent

--Conversation memory

--No manual intervention once the conversation starts

--Autonomy is intentionally bounded to:

--Prevent unsafe behavior

--Ensure task completion

--Reflect real-world customer support systems

/////////////////////////////////////////////////////////////////////////////////////////////////

**📁 Project Structure**

voice_agent_submission/
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
├── README.md
├── demo/
│   └── sample_conversation.txt
├── stt/
│   └── stt.py               # Speech-to-text module
├── tts/
│   └── tts.py               # Text-to-speech module
├── dialogue/
│   └── manager.py           # FSM dialogue logic
├── intent/
│   └── handler.py           # Intent detection
└── utils/
    └── audio.py             # Audio utilities

/////////////////////////////////////////////////////////////////////////////////////////////////

**▶️ How to Run Locally**

**--Environment--**

**🐍 Python 3.10 (recommended)**

**💻 Windows / Linux / macOS**

**--Setup--**
--python -m venv venv
--venv\Scripts\activate   # Windows
--pip install -r requirements.txt

**--Run the Agent--**
--python main.py
    

    

