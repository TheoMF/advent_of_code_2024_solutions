def reports_line_is_safe_part1(splitted_reports_line: list[int]) -> bool:
    """
    Return true if reports line is safe with conditions of the first part of the puzzle,
    False otherwise.
    """
    is_increasing = splitted_reports_line[1] > splitted_reports_line[0]
    for idx in range(len(splitted_reports_line) - 1):
        value_gap = splitted_reports_line[idx + 1] - splitted_reports_line[idx]
        if is_increasing and (value_gap < 1 or value_gap > 3):
            return False
        elif not is_increasing and (value_gap < -3 or value_gap > -1):
            return False
    return True


def reports_line_is_safe_without_val_at_idx(
    splitted_reports_line: list[int], idx_to_remove: int
) -> bool:
    """
    Return true if reports line is safe with conditions of the first part of the puzzle,
    but without a value at a chosen index, False otherwise.
    """
    del splitted_reports_line[idx_to_remove]
    return reports_line_is_safe_part1(splitted_reports_line)


def reports_line_is_safe_without_val_at_one_of_idxs(
    splitted_reports_line: list[int], idxs_to_remove: list[int]
) -> bool:
    """
    Return true if reports line is safe with conditions of the first part of the puzzle,
    but without the value at one of the index inside a list of indexes, False otherwise.
    """
    for idx_to_remove in idxs_to_remove:
        if reports_line_is_safe_without_val_at_idx(
            splitted_reports_line.copy(), idx_to_remove
        ):
            return True
    return False


def reports_line_is_safe_part2(splitted_reports_line: list[int]) -> bool:
    """
    Return true if reports line is safe with conditions of the second part of the puzzle,
    False otherwise.
    """
    is_increasing = splitted_reports_line[1] > splitted_reports_line[0]
    for idx in range(len(splitted_reports_line) - 1):
        value_gap = splitted_reports_line[idx + 1] - splitted_reports_line[idx]
        if is_increasing and (value_gap < 1 or value_gap > 3):
            idxs_to_remove = [max(idx - 1, 0), idx, idx + 1]
            return reports_line_is_safe_without_val_at_one_of_idxs(
                splitted_reports_line, idxs_to_remove
            )
        if not is_increasing and (value_gap < -3 or value_gap > -1):
            idxs_to_remove = [max(idx - 1, 0), idx, idx + 1]
            return reports_line_is_safe_without_val_at_one_of_idxs(
                splitted_reports_line, idxs_to_remove
            )
    return True


if __name__ == "__main__":
    with open("input_data.txt", "r") as f:
        reports_lines = f.read().splitlines()
    result_part1 = 0
    result_part2 = 0
    for reports_line in reports_lines:
        splitted_reports_line = reports_line.split(" ")
        splitted_reports_line = [int(value) for value in splitted_reports_line]
        if reports_line_is_safe_part1(splitted_reports_line):
            result_part1 += 1
        if reports_line_is_safe_part2(splitted_reports_line):
            result_part2 += 1
    print("result part1 ", result_part1)
    print("result part2 ", result_part2)
