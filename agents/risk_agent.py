from utils.groq_client import client


def analyze_risks(
    plan,
    requirements,
    tasks,
    roadmap
):

    prompt = f"""
You are a senior project management consultant.

Analyze the project and identify:

1. Technical Risks
2. Timeline Risks
3. Resource Risks
4. Security Risks
5. Scalability Risks

Then provide:

Overall Risk Score:
LOW / MEDIUM / HIGH

Project Information:

PLAN:
{plan}

REQUIREMENTS:
{requirements}

TASKS:
{tasks}

ROADMAP:
{roadmap}

Return only the risk analysis report.
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