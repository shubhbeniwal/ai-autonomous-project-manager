from utils.groq_client import client


def generate_requirements(project_plan):

    prompt = f"""
You are a Senior Business Analyst.

Using the project plan below, create a detailed
Software Requirements Specification.

Project Plan:

{project_plan}

Include:

1. Functional Requirements

2. Non-Functional Requirements

3. System Requirements

4. Technical Constraints

5. Acceptance Criteria

Keep the output structured and professional.

Return only the requirements document.
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