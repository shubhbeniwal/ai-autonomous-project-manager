from utils.groq_client import client


def create_roadmap(project_plan, sprint_plan):

    prompt = f"""
You are a Senior Product Director.

Using the project plan and sprint plan below,
create a professional project roadmap.

Project Plan:

{project_plan}

Sprint Plan:

{sprint_plan}

Include:

1. Phase 1
2. Phase 2
3. Phase 3

For each phase include:

- Objective
- Deliverables
- Estimated Timeline
- Milestones

Keep the roadmap realistic and professional.

Return only the roadmap.
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