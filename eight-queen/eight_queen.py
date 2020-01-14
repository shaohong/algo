RESULT = [-1] * 8
SOLUTION_COUNT = 0


def cal_eight_queen(row):
    if row == 8:
        printResult()
        return  # game over
    else:
        for column in range(0, 8):
            # check if it is OK to put the queen at (row, column)
            if isOK(row, column):
                RESULT[row] = column
                cal_eight_queen(row + 1)


def isOK(row, column):
    checking_row = row - 1
    while checking_row >= 0:
        # check if existing queens are on the same column
        if RESULT[checking_row] == column:
            return False
        # check if existing queeens are on the same diagnal.
        row_diff = row - checking_row
        col_diff = abs(column - RESULT[checking_row])
        if row_diff == col_diff:
            return False
        checking_row -= 1
    return True

def printResult():
    global SOLUTION_COUNT
    SOLUTION_COUNT += 1
    print(f"solution #{SOLUTION_COUNT}")
    for row in range(0, 8):
        for column in range(0, 8):
            if RESULT[row] == column:
                print('Q ', end='')
            else:
                print('* ', end='')
        # move to the next line
        print()


def main():
    cal_eight_queen(0)


if __name__ == '__main__':
    main()
