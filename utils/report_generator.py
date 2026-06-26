from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    filename,
    project_name,
    plan,
    requirements,
    tasks,
    sprints,
    roadmap,
    risk_report
):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"<b>{project_name}</b>",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    sections = [
        ("Project Plan", plan),
        ("Requirements", requirements),
        ("Tasks", tasks),
        ("Sprint Plan", sprints),
        ("Risk Analysis", risk_report),
        ("Roadmap", roadmap)
    ]

    for title, text in sections:

        content.append(
            Paragraph(
                f"<b>{title}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(text).replace(
                    "\n",
                    "<br/>"
                ),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

    pdf.build(content)