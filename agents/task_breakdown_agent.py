from utils.groq_client import client


def generate_tasks(requirements):

    prompt = f"""
You are a Senior Engineering Manager.

Using the software requirements below,
create a detailed development task list.

Requirements:

{requirements}

Create:

1. Epics

2. Development Tasks

3. Priority Level
   (High / Medium / Low)

4. Estimated Complexity
   (Easy / Medium / Hard)

Keep tasks clear and actionable.

Return only the task breakdown.
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