import GeneratorEngine as GE
import PdfCreator as PC
from GeneratorEngine import puzzle_grid
import csv

#List of words for puzzles

file = open('sample.csv', 'r')
csv_reader = csv.reader(file)

word_list = []
for row in csv_reader:
    word_list.append(row)

word_list1 = ["ANGEL", "BIRTH", "TREE", "BELLS", "BLIZZARD", "BOOTS", "CANDLE", "CANDY", "CELEBRATION", "CEREMONY",
         "CANDY", "CHILL", "CHILLY", "CHRISTMAS", "EVE", "CHRISTMASTIDE", "COOKIE", "CRECHE, CAROLING", "CAROL", "DECEMBER",
             "FESTIVAL", "REUNION", "FIREWOOD", "FRUITCAKE", "FROSTY", "FELIZ" "NAVIDAD", "FEAST", "FESTIVE", "SNOWMAN",
             "GARLAND", "GIFT", "GINGERBREAD", "GOODWILL", "GREETINGS", "GOLD", "GREEN"]

if __name__ == "__main__":
    puzzle_list = []
    list_length = len(word_list)
    for i in range(50):
        words = word_list[i%list_length]
        solution, puzzle, words = GE.generate_wordsearch_puzzle(20, words)
        puzzle1 = puzzle_grid("Puzzle: " + str(i+1), puzzle, solution, words)
        puzzle_list.append(puzzle1)


    #GE.print_grid(puzzle1.get_solution())
    pdf = PC.create_standard_book()
    pdf = PC.front_maters(pdf)
    #pdf = PC.create_solution_page(pdf, puzzle_list[0].get_title(), puzzle_list[0].get_solution(), puzzle_list[0].get_puzzle())
    #pdf = PC.create_puzzle_page(pdf, puzzle1.get_puzzle(), puzzle1.get_words())
    pdf = PC.create_multiple_puzzle(pdf, puzzle_list)
    pdf = PC.create_multiple_solution(pdf, puzzle_list)
    pdf.output('02. Test.pdf')
    print("done!")