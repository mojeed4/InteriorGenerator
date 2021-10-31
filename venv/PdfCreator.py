from fpdf import FPDF
import qrcode


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', '', 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, -10, 'Puzzles from PuzzleLabs.com', ln=1, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(80, 80, 80)
        if self.page_no() > 2:
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

def inches_to_mm(inches):
    return inches * 25.4

def create_standard_book():
    pdf = PDF('P', 'mm', (inches_to_mm(8.5),inches_to_mm(11)))
    pdf.alias_nb_pages()
    pdf.add_page()
    return pdf

def create_multiple_puzzle(pdf, puzzle_list):
    for puzzle in puzzle_list:
        pdf = create_puzzle_page(pdf, puzzle.get_title(), puzzle.get_puzzle(), puzzle.get_words())

    return pdf

def create_puzzle_page(pdf, title, puzzle, words):
    pdf.add_page()

    pdf.set_font('helvetica', '', 20)
    pdf.cell(0, 10, title, align='C')
    pdf.ln(10)

    cell_size = 9
    pdf.set_font('helvetica', '', 14)
    pdf.set_text_color(0,0,0)

    for row in puzzle:
        pdf.cell(cell_size, cell_size, "", ln = True)
        pdf.cell(cell_size, cell_size, "", border=False, align='C')
        for unit in row:
            pdf.cell(cell_size, cell_size, unit, border = True, align = 'C')

    pdf.ln(25)
    pdf.cell(0,10, ", ".join(words), align = 'C')

    return pdf

def create_multiple_solution(pdf, puzzle_list):
    for puzzle in puzzle_list:
        pdf = create_solution_page(pdf, puzzle.get_title(), puzzle.get_solution(), puzzle.get_puzzle())

    return pdf

def create_solution_page(pdf, title, solution, puzzle):
    pdf.add_page()
    pdf.ln(8)

    pdf.set_font('helvetica', '', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, title + " Solution", align='C')
    pdf.ln(10)

    cell_size = 9
    pdf.set_font('helvetica', '', 14)

    for solution_row, puzzle_row in zip(solution, puzzle):
        pdf.cell(cell_size, cell_size, "", ln = True)
        pdf.cell(cell_size, cell_size, "", border=False, align='C')

        for solution_unit, puzzle_unit in zip(solution_row, puzzle_row):
            if solution_unit == '_':
                pdf.set_font('helvetica', '')
                pdf.set_text_color(130, 130, 130)
                pdf.cell(cell_size, cell_size, puzzle_unit, border = True, align = 'C')
            else:
                pdf.set_font('helvetica', 'B')
                pdf.set_text_color(0, 0, 0)
                pdf.cell(cell_size, cell_size, solution_unit, border = True, align = 'C')

    return pdf


def front_maters(pdf):
    LARGE = 27
    REGULAR = 20
    SMALL = 12
    pdf.set_font('helvetica', 'B', LARGE)
    pdf.set_text_color(0,0,0)
    pdf.ln(15)
    pdf.cell(0,5, "Majid Creatives", ln = 1, align = 'C')
    pdf.set_font('helvetica', '', LARGE)
    pdf.cell(0,20, "100+ Word Search Puzzles for Adults", ln = 1, align = 'C')
    pdf.ln(80)
    pdf.set_font('helvetica', 'BU', 15)
    pdf.cell(0,10, " "*90, ln = 1, align = 'C')
    pdf.set_font('helvetica', '', REGULAR)
    pdf.cell(0,10, "Created with PuzzleLabs", ln = 1, align = 'C')

    img = qrcode.make("https://leedigital.net")
    pdf.image(img.get_image(), 75, 160,60)

    pdf.add_page()
    pdf.set_font('helvetica', '', SMALL)
    pdf.cell(0, 5, "Copyrights (c) 2021 by Puzzle Labs", ln=1, align='C')
    pdf.cell(0, 5, "All rights reserved", ln=1, align='C')
    pdf.ln(40)
    pdf.set_font('helvetica', '', REGULAR)
    pdf.cell(0, 10, "Book Cover Design from Bookkreatives", ln=1, align='C')
    pdf.ln(140)
    pdf.set_font('helvetica', 'BU', REGULAR)
    pdf.cell(0, 15, "SPECIAL REQUEST", ln=1, align='C')
    pdf.set_font('helvetica', '', SMALL)
    pdf.cell(0, 5, "We will love to hear your honest feedback. This will help us serve you better and", ln=1, align='C')
    pdf.cell(0, 5, "help others make decision on purchasing our books.", ln=1, align='C')
    pdf.cell(0, 5, "Head over to bookkreatives.com/review31", ln=1, align='C')


    return pdf

