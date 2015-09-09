import re

__author__ = 'Jeffrey'


class BobSeger(object):
    def __init__(self):
        pass

    def find_longest_with_knight_moves(self, grid, search_words):
        if len(grid) != 8 and sum([len(x) for x in grid]) != 64:
            raise AttributeError('Grid is not 8x8.')

        def test_char(letter, x, y):
            return letter.lower() == grid[x][y].lower()

        longest_word = ''

        for word in search_words:
            length = len(word)
            filtered_word = ''.join([x for x in word if re.match('[a-zA-Z]', x)])

            if length < len(longest_word):
                continue

            for grid_x, line in enumerate(grid):
                for grid_y, _ in enumerate(line):
                    i = 0
                    x = grid_x
                    y = grid_y
                    found = True

                    while not found:

                        if test_char(filtered_word[i], x, y):
                            i += 1

                            for move in [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]:
                                if 0 <= x + move[0] <= 7 and 0 <= y + move[1] <= 7:
                                    x += int(move[0])
                                    y += int(move[1])

                                if test_char(filtered_word[i], x, y):
                                    i += 1

                                    if i > length:
                                        found = True
                                        break
                            else:
                                break

                    if found:
                        longest_word = filtered_word

        return longest_word
