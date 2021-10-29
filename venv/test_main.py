import GeneratorEngine as GE
from GeneratorEngine import puzzle_grid


#List of words for puzzles
word_list = ["DATA", "ANALYST", "TABLEAU", "POWERBI", "PYTHON", "SQL", "VISUALIZATION", "STATISTICS", "PANDAS", "NUMPY",
         "NORMALIZATION", "ANALYTICS", "MATPLOTLIB", "LIBRARY"]

if __name__ == "__main__":
    solution, puzzle, words = GE.generate_wordsearch_puzzle(20, word_list)
    puzzle1 = puzzle_grid("First puzzle", puzzle, words, solution)
    GE.print_grid(puzzle1.get_solution())