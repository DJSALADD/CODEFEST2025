from fpdf import FPDF

def get_summary(chat) -> str:
    summary = chat.send_message("Generate summary of discussed content without preposition using only ASCII characters")
    return summary.text

def generate_pdf(chat, subject : str = " Summary"):
    pdf = FPDF()

    pdf.add_page()


    pdf.set_font("Times", size=15)

    # create a cell
    pdf.cell(200, 10, subject.capitalize(),
             ln=1, align='C')

    pdf.multi_cell(200, 10, get_summary(chat))

    pdf.output("summary.pdf")
