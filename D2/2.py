ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

WIN = "win"
LOOSE = "loose"
DRAW = "draw"

WINNING_SHAPE = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}


def get_shape_from_input(A: str) -> str:
    shape_converter = {
        "A": ROCK,
        "X": ROCK,
        "B": PAPER,
        "Y": PAPER,
        "C": SCISSORS,
        "Z": SCISSORS,
    }
    return shape_converter[A]


def get_winning_shape(shape: str) -> str:
    return WINNING_SHAPE[shape]


def get_loosing_shape(shape: str) -> str:
    loosing_shape = {v: k for k, v in WINNING_SHAPE.items()}
    return loosing_shape[shape]


def get_points_from_shape(shape: str) -> int:
    pts_from_shape = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }
    return pts_from_shape[shape]


def get_outcome_from_input(X: str) -> str:
    outcomes = {"X": LOOSE, "Y": DRAW, "Z": WIN}
    return outcomes[X]


def get_shape_from_outcome(elf_shape: str, outcome: str) -> str:
    if outcome == WIN:
        return get_winning_shape(elf_shape)
    if outcome == LOOSE:
        return get_loosing_shape(elf_shape)
    return elf_shape


def get_points_from_outcome(outcome: str) -> int:
    pts_from_outcome = {
        LOOSE: 0,
        DRAW: 3,
        WIN: 6,
    }
    return pts_from_outcome[outcome]


def get_outcome_from_shapes(elf_shape: str, my_shape: str) -> str:
    winning_shape = get_winning_shape(elf_shape)
    loosing_shape = get_loosing_shape(elf_shape)
    if my_shape == winning_shape:
        return WIN
    elif my_shape == loosing_shape:
        return LOOSE
    return DRAW


p1_points = 0
p2_points = 0
for line in open("2.txt"):
    line = line.strip()
    A = line[0]
    X = line[-1]
    elf_shape = get_shape_from_input(A)

    p1_shape = get_shape_from_input(X)
    p1_outcome = get_outcome_from_shapes(elf_shape, p1_shape)

    p2_outcome = get_outcome_from_input(X)
    p2_shape = get_shape_from_outcome(elf_shape, p2_outcome)

    p1_points += get_points_from_outcome(p1_outcome) + get_points_from_shape(p1_shape)
    p2_points += get_points_from_outcome(p2_outcome) + get_points_from_shape(p2_shape)

print(f"P1: {p1_points}")
print(f"P2: {p2_points}")
