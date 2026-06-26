from config import client


def estimate_resources(
    plan,
    requirements,
    tasks,
    roadmap
):

    prompt = f"""
You are a Senior Technical Project Manager.

Analyze the project below.

Return:

1. Recommended Team Structure
2. Required Roles
3. Estimated Development Timeline
4. MVP Cost Estimate
5. Production Cost Estimate
6. Cloud Infrastructure Requirements
7. Monthly Operating Cost
8. Scaling Recommendations

PROJECT PLAN:
{plan}

REQUIREMENTS:
{requirements}

TASKS:
{tasks}

ROADMAP:
{roadmap}
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