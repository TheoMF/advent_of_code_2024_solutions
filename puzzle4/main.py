class WordFinder:
    """Class that finds words inside letters grid."""

    def __init__(self, letters_grid):
        """Initialize the class with a letters grid as input."""
        self.letters_grid = letters_grid
        self.grid_size = len(letters_grid)

        # possible directions to search words for the two parts of the puzzle
        self.directions_part1 = [
            (1, 1),
            (1, 0),
            (1, -1),
            (0, 1),
            (0, -1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]
        self.directions_part2 = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

    def get_possible_directions_part1(self, line_idx: int, col_idx: int) -> list[int]:
        """
        Return the possible directions to look for words at the given place of the
        grid for the first part of the puzzle.
        """
        possible_directions = []
        for line_dir, col_dir in self.directions_part1:
            if (
                line_idx + 3 * line_dir >= 0
                and line_idx + 3 * line_dir <= self.grid_size - 1
                and col_idx + 3 * col_dir >= 0
                and col_idx + 3 * col_dir <= self.grid_size - 1
            ):
                possible_directions.append(((line_dir, col_dir)))
        return possible_directions

    def get_nb_xmas_part1(self, line_idx: int, col_idx: int) -> int:
        """
        Return how many XMAS word there is at the given place at the grid, supposing
        the letter we're at is an X.
        """
        directions = self.get_possible_directions_part1(line_idx, col_idx)
        nb_xmas_found = 0
        for line_dir, col_dir in directions:
            if (
                self.letters_grid[line_idx + line_dir][col_idx + col_dir] == "M"
                and self.letters_grid[line_idx + line_dir * 2][col_idx + col_dir * 2]
                == "A"
                and self.letters_grid[line_idx + line_dir * 3][col_idx + col_dir * 3]
                == "S"
            ):
                nb_xmas_found += 1
        return nb_xmas_found

    def get_possible_directions_part2(self, line_idx: int, col_idx: int) -> list[int]:
        """
        Return the possible directions to look for words at the given place of the
        grid for the second part of the puzzle.
        """
        possible_directions = []
        for line_dir, col_dir in self.directions_part2:
            if (
                line_idx + line_dir >= 0
                and line_idx - line_dir >= 0
                and line_idx + line_dir <= self.grid_size - 1
                and line_idx - line_dir <= self.grid_size - 1
                and col_idx + col_dir >= 0
                and col_idx - col_dir >= 0
                and col_idx + col_dir <= self.grid_size - 1
                and col_idx - col_dir <= self.grid_size - 1
            ):
                possible_directions.append(((line_dir, col_dir)))
        return possible_directions

    def get_nb_xmas_part2(self, line_idx, col_idx) -> int:
        """
        Return 1 if there's an X-MAS at the given place at the grid, supposing
        the letter we're at is an A, 0 otherwise.
        """
        directions = self.get_possible_directions_part2(line_idx, col_idx)
        nb_mas_found = 0
        nb_xmas_found = 0
        for line_dir, col_dir in directions:
            if (
                self.letters_grid[line_idx + line_dir][col_idx + col_dir] == "M"
                and self.letters_grid[line_idx - line_dir][col_idx - col_dir] == "S"
            ):
                nb_mas_found += 1
        if nb_mas_found >= 2:
            nb_xmas_found = 1
        return nb_xmas_found

    def get_nb_words(self, is_part1: bool = True) -> int:
        """Returns number of occurrences of either XMAS or X-MAS on a letters grid."""
        nb_words = 0
        if is_part1:
            letter_to_search = "X"
        else:
            letter_to_search = "A"
        for line_idx, grid_line in enumerate(letters_grid):
            grid_line_start_col_idx = 0
            while grid_line.find(letter_to_search) != -1:
                col_idx = grid_line.find(letter_to_search) + grid_line_start_col_idx
                if is_part1:
                    nb_words += word_finder.get_nb_xmas_part1(line_idx, col_idx)
                else:
                    nb_words += word_finder.get_nb_xmas_part2(line_idx, col_idx)
                column_shift = grid_line.find(letter_to_search) + 1
                grid_line = grid_line[column_shift:]
                grid_line_start_col_idx += column_shift
        return nb_words


if __name__ == "__main__":
    with open("input_data.txt", "r") as f:
        letters_grid = f.read().splitlines()
    word_finder = WordFinder(letters_grid)
    result_part1 = word_finder.get_nb_words(is_part1=True)
    result_part2 = word_finder.get_nb_words(is_part1=False)
    print("result part1 ", result_part1)
    print("result part2 ", result_part2)
