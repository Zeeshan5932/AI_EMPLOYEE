from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def handle_document(task):
    task_type = task.get("type")

    if task_type == "create_word":
        filename = task.get("filename", "document.docx")
        content = task.get("content", "")

        doc = Document()
        doc.add_paragraph(content)
        doc.save(filename)

        return f"Word document {filename} created."

    elif task_type == "create_pdf":
        filename = task.get("filename", "document.pdf")
        content = task.get("content", "")

        pdf = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()
        elements = [Paragraph(content, styles["Normal"])]
        pdf.build(elements)

        return f"PDF {filename} created."

    return "Document task not supported."