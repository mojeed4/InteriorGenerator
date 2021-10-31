import GeneratorEngine as GE
import PdfCreator as PC
from GeneratorEngine import puzzle_grid


#List of words for puzzles
word_list = ["DATA", "ANALYST", "TABLEAU", "POWERBI", "PYTHON", "SQL", "VISUALIZATION", "STATISTICS", "PANDAS", "NUMPY",
         "NORMALIZATION", "ANALYTICS", "MATPLOTLIB", "LIBRARY"]

if __name__ == "__main__":
    puzzle_list = []
    for i in range(50):
        solution, puzzle, words = GE.generate_wordsearch_puzzle(20, word_list)
        puzzle1 = puzzle_grid("Puzzle: " + str(i+1), puzzle, solution, words)
        puzzle_list.append(puzzle1)


    #GE.print_grid(puzzle1.get_solution())
    pdf = PC.create_standard_book()
    pdf = PC.front_maters(pdf)
    #pdf = PC.create_solution_page(pdf, puzzle_list[0].get_title(), puzzle_list[0].get_solution(), puzzle_list[0].get_puzzle())
    #pdf = PC.create_puzzle_page(pdf, puzzle1.get_puzzle(), puzzle1.get_words())
    pdf = PC.create_multiple_puzzle(pdf, puzzle_list)
    pdf = PC.create_multiple_solution(pdf, puzzle_list)
    pdf.output('01. Test.pdf')