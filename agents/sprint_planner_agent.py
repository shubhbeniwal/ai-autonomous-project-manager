from utils.groq_client import client


def create_sprint_plan(tasks):

    prompt = f"""
You are an experienced Agile Project Manager.

Using the development tasks below:

{tasks}

Organize them into development sprints.

Create:

1. Sprint 1
2. Sprint 2
3. Sprint 3
4. Sprint Goals

Rules:

- High priority tasks should appear first.
- Group related tasks together.
- Keep sprint workloads balanced.

Return only the sprint plan.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content