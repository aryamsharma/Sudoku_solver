
def display(grid):
    for i in range(81):
        if i != 80 and (i + 1) % 27 == 0:
            print(grid[i], end="\n------+-------+------\n")
            continue
        if (i + 1) % 9 == 0:
            print(grid[i])
            continue
        if (i + 1) % 3 == 0:
            print(grid[i], end=" | ")
            continue
        print(grid[i], end=" ")

def get_row(grid, index): # Index
    start = int(index / 9) * 9
    return grid[start:start + 9]

def get_column(grid, index): # index
    return "".join(grid[i] for i in range(index % 9, 81, 9))

def get_box(grid, index): # index
    start = (int(index / 27) * 27) + int(index / 3) % 3 * 3
    final = ""
    for i in range(0, 19, 9):
        final += grid[start + i: start + i + 3]
    return final

def test(grid, i=28):
    print(f"Val: {grid[i]}")
    print(f"Row vals: {get_row(grid, i)}")
    print(f"Col vals: {get_column(grid, i)}")
    print(f"Boxes vals: {get_box(grid, i)}")

def fill(grid: str):
    if grid.count("."):
        index = grid.index(".")
        for i in range(1, 10):
            i = str(i)
            if i in get_row(grid, index) or i in get_column(grid, index) or i in get_box(grid, index):
                continue
            grid = grid[:index] + i + grid[index + 1:]
            tmp = fill(grid)
            if tmp:
                return tmp
        return False
    else:
        return grid

def parser():
    sudoku = ""
    every = []
    with open("MyTest.txt", "r") as f:
        for line in f.readlines():
            if line[0] == "=":
                every.append(sudoku)
                sudoku = ""
                continue
            sudoku += line.strip()
    return every

def solve_all():
    every = parser()
    i = 1
    for grid in every:
        print(i)
        i += 1
        display(grid)
        display(fill(grid))
        fill(grid)

def solve_one():
    grid = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    display(fill(grid))

if __name__ == "__main__":
    solve_one()