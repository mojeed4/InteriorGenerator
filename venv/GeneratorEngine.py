import random
import string
from pprint import pprint


#This function is used for printing the grid and visualizing the puzzle.
def print_grid(grid):
    grid_size = len(grid)
    for x in range(grid_size):
        print("\t" * 1 + " ".join(grid[x]))

 #This is a collection of the ways words can appear in the wordsearch engine.
orientations = [1, 2, 3, 4]
#1 For words spanning left to right
#2 For words spanning from up to down
#3 For words going diagonally upwards
#4 For words going diagonally downwards

#This class holds a complete puzzle with its solution.
class puzzle_grid:

    def __init__(self, title, puzzle, solution, words):
        self.title = title
        self.puzzle = puzzle
        self.words = words
        self.solution = solution

    def print_puzzle(self):
        #print title
        print("\t\tTitle:", self.title)
        print("--"*20)

        #print puzzle
        grid_size = len(self.puzzle)
        for x in range(grid_size):
            print("\t" * 1 + " ".join(self.puzzle[x]))

        print("\n")
        #print solution title
        print("\t\tSolution:", self.title)
        print("--"*25)

        #print solution
        grid_size = len(self.solution)
        for x in range(grid_size):
            print("\t" * 1 + " ".join(self.solution[x]))

    def get_puzzle(self):
        return self.puzzle

    def get_title(self):
        return self.title

    def get_solution(self):
        return self.solution

    def get_words(self):
        return self.words



def generate_wordsearch_puzzle(size, word_list):
    words = []
    while len(words) < 5:
        new_word = random.choice(word_list)
        if new_word not in words:
            if new_word != '':
                words.append(new_word)

    grid_size = size
    grid = [['_' for i in range(grid_size)] for j in range(grid_size)]

    for word in words:
        word_length = len(word)
        placed = False

        while not placed:
            orientation = random.choice(orientations)

            if orientation == orientations[0]:
                x_increment = 1
                y_increment = 0
            elif orientation == orientations[1]:
                x_increment = 0
                y_increment = 1
            elif orientation == orientations[2]:
                x_increment = 1
                y_increment = 1
            else:
                x_increment = 1
                y_increment = -1

            if x_increment == 0:
                x_position = random.randint(0, grid_size)
            else:
                x_position = random.randint(0, (grid_size - word_length))

            if y_increment == 1:
                y_position = random.randint(0, (grid_size - word_length))
            elif y_increment == 0:
                y_position = random.randint(0, grid_size)
            else:
                y_position = random.randint(word_length, grid_size)

            # Checking if the selected size will work.
            x_extreme = x_position + word_length * x_increment
            y_extreme = y_position + word_length * y_increment

            if x_extreme < 0 or x_extreme >= grid_size:
                continue
            if x_extreme < 0 or x_extreme >= grid_size:
                continue

            failed = False

            try:
                for i in range(word_length):
                    character = word[i]

                    new_position_x = x_position + i * x_increment
                    new_position_y = y_position + i * y_increment

                    character_at_new_position = grid[new_position_x][new_position_y]

                    if character_at_new_position != '_':
                        if character_at_new_position == character:
                            continue
                        else:
                            failed = True
                            break
            except:
                failed = True
                break

            if failed:
                continue
            else:
                for i in range(word_length):
                    character = word[i]

                    new_position_x = x_position + i * x_increment
                    new_position_y = y_position + i * y_increment

                    grid[new_position_x][new_position_y] = character

                placed = True

    solution = [['_' for i in range(grid_size)] for j in range(grid_size)]

    for x in range(grid_size):
        for y in range(grid_size):
            temp = grid[x][y]
            solution[x][y] = temp

    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == '_':
                grid[x][y] = random.choice(string.ascii_uppercase)

    return (solution, grid, words)
