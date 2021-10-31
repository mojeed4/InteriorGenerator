import GeneratorEngine as GE
import PdfCreator as PC
from GeneratorEngine import puzzle_grid


#List of words for puzzles
word_list = ["DATA", "ANALYST", "TABLEAU", "POWERBI", "PYTHON", "SQL", "VISUALIZATION", "STATISTICS", "PANDAS", "NUMPY",
         "NORMALIZATION", "ANALYTICS", "MATPLOTLIB", "LIBRARY"]

if __name__ == "__main__":
    solution, puzzle, words = GE.generate_wordsearch_puzzle(20, word_list)
    puzzle1 = puzzle_grid("First puzzle", puzzle, solution, words)
    #GE.print_grid(puzzle1.get_solution())
    pdf = PC.create_standard_book()
    pdf = PC.front_maters(pdf)
    pdf = PC.create_puzzle_page(pdf, puzzle1.get_puzzle(), puzzle1.get_words())
    pdf.output('01. Test.pdf')