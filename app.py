import streamlit as st

from agents.planner_agent import (
    create_project_plan
)

from agents.requirements_agent import (
    generate_requirements
)

from agents.task_breakdown_agent import (
    generate_tasks
)

from agents.sprint_planner_agent import (
    create_sprint_plan
)

from agents.roadmap_agent import (
    create_roadmap
)

from utils.memory_manager import (
    get_project,
    save_project,
    get_all_projects,
    get_project_names
)

from utils.report_generator import (
    generate_pdf_report
)

from agents.risk_agent import (
    analyze_risks
)

def calculate_complexity(tasks_text):

    task_count = tasks_text.count(
        "Task"
    )

    if task_count < 10:
        return "Easy"

    elif task_count < 25:
        return "Medium"

    return "Hard"

st.set_page_config(
    page_title="Autonomous AI Project Manager",
    page_icon="🚀",
    layout="wide"
)

st.title(
    "🚀 Autonomous AI Project Manager"
)

st.caption(
    "AI-Powered Multi-Agent Project Planning Platform"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title(
    "🚀 About the Creator"
)

st.sidebar.markdown("""
### Shubh Beniwal

AI Engineer | Software Developer

VIT Chennai Graduate

Passionate about:

- AI Engineering
- LLM Systems
- Autonomous Agents
- Software Engineering

---
GitHub:
https://github.com/shubhbeniwal

LinkedIn:
https://www.linkedin.com/in/shubhbeniwal/
""")


# ---------------- ANALYTICS ----------------

all_projects = get_all_projects()

project_history = get_project_names()

total_projects = len(all_projects)

latest_project = "None"

if total_projects > 0:

    latest_project = list(
        all_projects.keys()
    )[-1]
    
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Projects Generated",
        total_projects
    )

with col2:
    st.metric(
        "Stored Projects",
        len(project_history)
    )

with col3:
    st.metric(
        "Latest Project",
        latest_project
    )

st.sidebar.markdown("---")

st.subheader(
    "⚡ Platform Health"
)

st.success(
    f"""
✅ Agents Online: 5

✅ Stored Projects: {len(project_history)}

✅ Memory Layer: Active

✅ PDF Reports: Active

✅ Archive System: Active
"""
)

st.sidebar.subheader(
    "📂 Project Archive"
)

selected_project = st.sidebar.selectbox(
    "Previous Projects",
    ["Select Project"] + project_history
)


st.sidebar.info("""
Planner Agent

↓

Requirements Agent

↓

Task Agent

↓

Sprint Agent

↓

Roadmap Agent

↓

Risk Analysis Agent
""")


# ---------------- INPUT ----------------
st.markdown("---")

st.subheader(
    "🤖 Agent Workflow"
)

st.info("""
Planner Agent
↓
Requirements Agent
↓
Task Breakdown Agent
↓
Sprint Planner Agent
↓
Roadmap Agent
↓
Risk Analysis Agent
""")

st.markdown("---")

st.subheader(
    "📂 Project Workspace"
)


project_idea = st.text_area(
    "Enter Your Project Idea",
    height=150,
    placeholder="Example: Build a Netflix Clone"
)

run_button = st.button(
    "🚀 Generate Project Plan"
)


# ---------------- GENERATE ----------------



if selected_project != "Select Project":

    archived_project = get_project(
        selected_project
    )

    st.markdown("---")

    st.header(
        f"📂 {selected_project}"
    )

    with st.expander(
        "🧠 Planner Agent"
    ):
        st.write(
            archived_project["plan"]
        )

    with st.expander(
        "📋 Requirements Agent"
    ):
        st.write(
            archived_project["requirements"]
        )

    with st.expander(
        "🛠 Task Agent"
    ):
        st.write(
            archived_project["tasks"]
        )

    with st.expander(
        "🏃 Sprint Agent"
    ):
        st.write(
            archived_project["sprints"]
        )
        
    with st.expander(
        "⚠️ Risk Analysis Agent"
    ):
        st.write(
            archived_project.get(
                "risk_report",
                "Risk analysis not available for older projects."
            )
        )

    with st.expander(
        "🗺 Roadmap Agent"
    ):
        st.write(
            archived_project["roadmap"]
        )

    pdf_file = "project_report.pdf"

    generate_pdf_report(
        pdf_file,
        selected_project,
        archived_project["plan"],
        archived_project["requirements"],
        archived_project["tasks"],
        archived_project["sprints"],
        archived_project["roadmap"],
        archived_project.get(
            "risk_report",
            "Not Available"
        )
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Archived Project PDF",
            data=file,
            file_name=f"{selected_project}.pdf",
            mime="application/pdf"
        )


if run_button and project_idea:
    
    cached_project = get_project(
        project_idea
    )

    if cached_project:

        st.success(
            "🧠 Project Found In Memory"
        )

        with st.expander(
            "🧠 Planner Agent"
        ):
            st.write(
                cached_project["plan"]
            )

        with st.expander(
            "📋 Requirements Agent"
        ):
            st.write(
                cached_project["requirements"]
            )

        with st.expander(
            "🛠 Task Agent"
        ):
            st.write(
                cached_project["tasks"]
            )

        with st.expander(
            "🏃 Sprint Agent"
        ):
            st.write(
                cached_project["sprints"]
            )

        with st.expander(
            "⚠️ Risk Analysis Agent"
        ):
            st.write(
                cached_project.get(
                    "risk_report",
                    "Risk analysis not available for older projects."
                )
            )
        
        with st.expander(
            "🗺 Roadmap Agent"
        ):
            st.write(
                cached_project["roadmap"]
            )

        pdf_file = "project_report.pdf"

        generate_pdf_report(
            pdf_file,
            project_idea,
            cached_project["plan"],
            cached_project["requirements"],
            cached_project["tasks"],
            cached_project["sprints"],
            cached_project["roadmap"],
            cached_project.get(
                "risk_report",
                "Not Available"
            )
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download Executive PDF",
                data=file,
                file_name=f"{project_idea}.pdf",
                mime="application/pdf"
            )
            
        st.stop()
    
    planner_status = st.empty()
    requirements_status = st.empty()
    tasks_status = st.empty()
    sprint_status = st.empty()
    roadmap_status = st.empty()
    risk_status = st.empty()

    # Planner

    planner_status.info(
        "🧠 Planner Agent Running..."
    )

    plan = create_project_plan(
        project_idea
    )

    planner_status.success(
        "✅ Planner Complete"
    )

    # Requirements

    requirements_status.info(
        "📋 Requirements Agent Running..."
    )

    requirements = generate_requirements(
        plan
    )

    requirements_status.success(
        "✅ Requirements Complete"
    )

    # Tasks

    tasks_status.info(
        "🛠 Task Agent Running..."
    )

    tasks = generate_tasks(
        requirements
    )

    complexity = calculate_complexity(
        tasks
    )
    
    tasks_status.success(
        "✅ Tasks Complete"
    )

    # Sprints

    sprint_status.info(
        "🏃 Sprint Agent Running..."
    )

    sprints = create_sprint_plan(
        tasks
    )

    sprint_status.success(
        "✅ Sprint Planning Complete"
    )

    # Roadmap

    roadmap_status.info(
        "🗺 Roadmap Agent Running..."
    )

    roadmap = create_roadmap(
        plan,
        sprints
    )
    
    roadmap_status.success(
        "✅ Roadmap Complete"
    )
    
    risk_status.info(
        "⚠️ Risk Analysis Agent Running..."
    )

    risk_report = analyze_risks(
        plan,
        requirements,
        tasks,
        roadmap
    )

    risk_status.success(
        "✅ Risk Analysis Complete"
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Project Complexity",
            complexity
        )

    with col2:

        st.metric(
            "Estimated Sprints",
            sprints.count("Sprint")
        )
    
    save_project(
        project_idea,
        plan,
        requirements,
        tasks,
        sprints,
        roadmap,
        risk_report
    )

    st.markdown("---")

    st.header(
        "📈 Project Overview"
    )

    st.success(
        f"""
    Complexity: {complexity}

    Estimated Sprints: {sprints.count("Sprint")}

    Status: Ready For Development
    """
    )

    st.header(
        "🧠 Agent Outputs"
    )

    with st.expander(
        "🧠 Planner Agent"
    ):
        st.write(plan)

    with st.expander(
        "📋 Requirements Agent"
    ):
        st.write(requirements)

    with st.expander(
        "🛠 Task Agent"
    ):
        st.write(tasks)

    with st.expander(
        "🏃 Sprint Planner Agent"
    ):
        st.write(sprints)

    with st.expander(
        "⚠️ Risk Analysis Agent"
    ):
        st.write(
            risk_report
        )

    with st.expander(
        "🗺 Roadmap Agent"
    ):
        st.write(
            roadmap
        )

    pdf_file = "project_report.pdf"

    generate_pdf_report(
        pdf_file,
        project_idea,
        plan,
        requirements,
        tasks,
        sprints,
        roadmap,
        risk_report
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Executive PDF",
            data=file,
            file_name=f"{project_idea}.pdf",
            mime="application/pdf"
        )
            
st.markdown("---")

st.caption(
    "🚀 About the Creator — Shubh Beniwal, AI Engineer | Software Developer, VIT Chennai Graduate | Passionate about AI, LLMs, NLP, and Software Engineering."
)