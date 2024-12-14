from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Equation:
    button_a: Point
    button_b: Point
    prize: Point


def parse_line(line: str, symbol: str, offset: int = 0):
    return Point(
        *(int(v.split(symbol)[1]) + offset for v in line.split(": ")[1].split(", "))
    )


def parse_button(line: str):
    return parse_line(line, "+")


def parse_prize(line: str, offset: int):
    return parse_line(line, "=", offset)


def parse_equation(lines: list[str], offset: int):
    button_a, button_b, prize = lines
    return Equation(
        parse_button(button_a),
        parse_button(button_b),
        parse_prize(prize, offset),
    )


def parse_equations(input: str, offset: int = 0):
    return [parse_equation(lines.split("\n"), offset) for lines in input.split("\n\n")]


def solve(e: Equation):
    a = Fraction(
        Fraction(e.prize.y, e.button_b.y) - Fraction(e.prize.x, e.button_b.x),
        Fraction(e.button_a.y, e.button_b.y) - Fraction(e.button_a.x, e.button_b.x),
    )
    b = Fraction(
        Fraction(e.prize.y, e.button_a.y) - Fraction(e.prize.x, e.button_a.x),
        Fraction(e.button_b.y, e.button_a.y) - Fraction(e.button_b.x, e.button_a.x),
    )
    if a.is_integer() and b.is_integer():
        return 3 * a + b
    return 0


input = (Path(__file__).parent / "input.txt").read_text().strip()
print(sum(solve(equation) for equation in parse_equations(input)))
print(sum(solve(equation) for equation in parse_equations(input, 10000000000000)))
