#  Autonomous AI Project Manager

### AI-Powered Multi-Agent Project Planning Platform

**Live Demo:** [https://ai-autonomous-project-manager-fg4xkor9u5dhhdhevscpuu.streamlit.app/](https://ai-autonomous-project-manager-fg4xkor9u5dhhdhevscpuu.streamlit.app/)

---

## Screenshots

<img width="775" height="368" alt="image" src="https://github.com/user-attachments/assets/22fc0068-ff5e-45f4-82a6-efa4c0641113" />
<img width="570" height="369" alt="image" src="https://github.com/user-attachments/assets/77f9fb81-6b50-464b-a3fc-ebd989ae67dd" />

---

## 📌 Overview

Autonomous AI Project Manager is a multi-agent AI platform that transforms a simple project idea into a complete execution blueprint.

The platform uses specialized AI agents working together to generate:

* Project Plans
* Requirements Documentation
* Task Breakdown Structures
* Sprint Plans
* Risk Analysis Reports
* Product Roadmaps
* Executive PDF Reports

The goal is to simulate how an experienced project manager would analyze, structure, and plan a software project from idea to execution.

---

## 🎯 Problem Statement

Early-stage founders, developers, students, and product teams often struggle with:

* Defining project scope
* Creating requirements documents
* Breaking work into tasks
* Planning sprints
* Identifying risks
* Building realistic roadmaps

This platform automates the planning process using multiple AI agents.

---

## 🏗️ System Architecture

```text
User Project Idea
        │
        ▼
┌─────────────────────┐
│  Planner Agent      │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Requirements Agent  │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Task Breakdown      │
│ Agent              │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Sprint Planner      │
│ Agent              │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Risk Analysis Agent │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Roadmap Agent       │
└─────────────────────┘
        │
        ▼
 Executive Report
        │
        ▼
     PDF Export
```

---

## 🤖 Multi-Agent Architecture

### 🧠 Planner Agent

Responsible for:

* Understanding the project idea
* Defining project goals
* Creating high-level project plans
* Identifying major deliverables

---

### 📋 Requirements Agent

Responsible for:

* Functional requirements
* Non-functional requirements
* User stories
* Technical requirements

---

### 🛠️ Task Breakdown Agent

Responsible for:

* Breaking requirements into actionable tasks
* Organizing implementation work
* Creating development workflows

---

### 🏃 Sprint Planner Agent

Responsible for:

* Sprint allocation
* Task scheduling
* Agile planning structure
* Development milestones

---

### ⚠️ Risk Analysis Agent

Responsible for:

* Technical risks
* Product risks
* Team risks
* Scalability concerns
* Deployment challenges

---

### 🗺️ Roadmap Agent

Responsible for:

* Development roadmap creation
* Timeline generation
* Long-term planning
* Future enhancements

---

## ✨ Features

### Multi-Agent Planning

* Multiple specialized AI agents
* Modular architecture
* Independent agent workflows

### Project Archive

* View previous projects
* Access historical project plans
* Reopen generated reports

### Risk Assessment

* Technical risk analysis
* Business risk identification
* Mitigation recommendations

### Executive PDF Reports

Generate downloadable project reports containing:

* Plans
* Requirements
* Tasks
* Sprint schedules
* Roadmaps

### Analytics Dashboard

Track:

* Total projects generated
* Stored projects
* Latest project activity

### Complexity Estimation

Projects are automatically classified as:

* Easy
* Medium
* Hard

Based on generated workload.

---

## 🖥️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Layer

* Groq API
* Llama Models

### PDF Generation

* ReportLab

### Storage

* Local JSON Memory Layer

### Utilities

* JSON
* OS
* Python Standard Library

---

## 📂 Project Structure

```text
AI-Autonomous-Project-Manager/

│
├── agents/
│   ├── planner_agent.py
│   ├── requirements_agent.py
│   ├── task_breakdown_agent.py
│   ├── sprint_planner_agent.py
│   ├── roadmap_agent.py
│   └── risk_agent.py
│
├── utils/
│   ├── memory_manager.py
│   └── report_generator.py
│
├── memory/
│   └── projects_memory.json
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/shubhbeniwal/ai-autonomous-project-manager.git

cd ai-autonomous-project-manager
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

Autonomous AI Project Manager is deployed on Streamlit Cloud:

[https://ai-autonomous-project-manager-fg4xkor9u5dhhdhevscpuu.streamlit.app/](https://ai-autonomous-project-manager-fg4xkor9u5dhhdhevscpuu.streamlit.app/)

---

## 📈 Example Workflow

### Input

```text
Build an AI Resume Analyzer
```

### Output

* Project Plan
* Requirements Document
* Development Tasks
* Sprint Breakdown
* Risk Assessment
* Product Roadmap
* PDF Report

---

## 🔮 Future Improvements

Potential production-grade enhancements:

* Supabase Integration
* User Authentication
* Team Collaboration
* Kanban Boards
* Cost Estimation Agent
* Resource Planning Agent
* Jira Integration
* GitHub Integration
* Automated Sprint Tracking
* Vector Database Memory
* Agent-to-Agent Communication Framework

---

## 🚀 About the Creator

**Shubh Beniwal**

AI Engineer | Software Developer

VIT Chennai Graduate

Passionate about:

* Artificial Intelligence
* Multi-Agent Systems
* LLM Applications
* NLP
* Software Engineering

GitHub:
[https://github.com/shubhbeniwal](https://github.com/shubhbeniwal)

LinkedIn:
[https://www.linkedin.com/in/shubhbeniwal/](https://www.linkedin.com/in/shubhbeniwal/)

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🚀 Build upon it

📢 Share it with others

---

## License

This project is intended for educational, research, and portfolio purposes.

This README matches the architecture and features of your current locally working project, including the deployed Streamlit link.
