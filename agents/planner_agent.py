from utils.groq_client import client


def create_project_plan(project_idea):

    prompt = f"""
You are an expert Product Manager.

Analyze the following project idea:

{project_idea}

Create a structured project plan.

Include:

1. Project Overview

2. Main Features

3. Technical Requirements

4. User Stories

5. Success Criteria

Keep the response clear and structured.

Return only the project plan.
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