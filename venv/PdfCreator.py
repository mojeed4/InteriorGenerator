from fpdf import FPDF
import qrcode

#Extention of the FPDF module to edit the header and footer.
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

#function to convert inches to millimeters
def inches_to_mm(inches):
    '''
    :param inches:
    :return: millimeters
    '''
    return inches * 25.4

#function to initialize book
def create_standard_book():
    '''
    This takes no parameters
    :return: it returns a pdf object to start adding pages
    '''
    pdf = PDF('P', 'mm', (inches_to_mm(8.5),inches_to_mm(11)))
    pdf.alias_nb_pages()
    pdf.add_page()
    return pdf

#function to create puzzle book with multiple pages
def create_multiple_puzzle(pdf, puzzle_list):
    '''
    This function adds multiple puzzle pages to a pdf object.

    :param pdf: A pdf object to add the multiple puzzle pages
    :param puzzle_list: a list containing puzzle_grids objects.
    :return: a pdf object with the mutiple puzzle pages added to it
    '''
    for puzzle in puzzle_list:
        pdf = create_puzzle_page(pdf, puzzle.get_title(), puzzle.get_puzzle(), puzzle.get_words())

    return pdf

#function to create single puzzle page
def create_puzzle_page(pdf, title, puzzle, words):
    '''
    This function creates a single page of word search puzzle and takes the parameters described below
    :param pdf: the pdf object into which the puzzle will be added
    :param title: the title of the puzzle
    :param puzzle: the puzzle itself containing the characters
    :param words: the words contained in the word search puzzle to which participants are expected to find within the puzzle search.
    :return: pdf: this function returns the pdf object inputted with the new puzzle page added to it.
    '''
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
    pdf.multi_cell(0,10, ", ".join(words), align = 'C')

    return pdf

#function to create multiple solution
def create_multiple_solution(pdf, puzzle_list):
    '''

    :param pdf: The pdf document object to which solution pages will be added.
    :param puzzle_list: A list containing puzzle_list objects for which solution will be extracted.
    :return: A pdf object document with which the solution pages have been appended.
    '''
    for puzzle in puzzle_list:
        pdf = create_solution_page(pdf, puzzle.get_title(), puzzle.get_solution(), puzzle.get_puzzle())

    return pdf

#function to create single solution page
def create_solution_page(pdf, title, solution, puzzle):
    '''

    :param pdf: The pdf document object to which solution pages will be added.
    :param title: The title of the puzzle solution
    :param solution: The actual solution puzzle itself
    :param puzzle: the actual puzzle itself.
    :return:
    '''

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

#function to create front matters.
def front_maters(pdf):
    '''

    :param pdf: The pdf object to which the front matters will be added.
    :return: This returns the pdf object after the front matters have been added successfully.
    '''
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

