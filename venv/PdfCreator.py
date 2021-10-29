from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 20)
        pdf.set_text_color(42, 127, 255)
        self.cell(0, 10, 'My puzzle book', ln=1, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = PDF('P', 'mm', 'A4')
pdf.alias_nb_pages()

def front_maters():
