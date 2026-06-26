import json
import os


MEMORY_FILE = "memory/projects_memory.json"


def load_memory():

    os.makedirs(
        os.path.dirname(MEMORY_FILE),
        exist_ok=True
    )

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_memory(memory):

    os.makedirs(
        os.path.dirname(MEMORY_FILE),
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )


def get_project(project_name):

    memory = load_memory()

    return memory.get(project_name)


def save_project(
    project_name,
    plan,
    requirements,
    tasks,
    sprints,
    roadmap,
    risk_report
):

    memory = load_memory()

    memory[project_name] = {
        "plan": plan,
        "requirements": requirements,
        "tasks": tasks,
        "sprints": sprints,
        "roadmap": roadmap,
        "risk_report": risk_report
    }

    save_memory(memory)


def get_all_projects():

    return load_memory()

def get_project_names():

    memory = load_memory()

    return list(memory.keys())