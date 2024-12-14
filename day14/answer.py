from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from statistics import variance

from PIL import Image


@dataclass
class Vector:
    x: int
    y: int


@dataclass
class Robot:
    position: Vector
    velocity: Vector


def parse_point(point: str):
    return Vector(*map(int, point.split("=")[1].split(",")))


def parse_robot(line: str):
    return Robot(*map(parse_point, line.split(" ")))


def parse_robots(input: str):
    return list(map(parse_robot, input.split("\n")))


input = (Path(__file__).parent / "input.txt").read_text().strip()

robots = parse_robots(input)

width = 101
height = 103
duration = 100

quadrants = [0] * 4
for robot in robots:
    x = (robot.position.x + (robot.velocity.x + width) * duration) % width
    y = (robot.position.y + (robot.velocity.y + height) * duration) % height
    if x < width // 2 and y < height // 2:
        quadrants[0] += 1
    elif x > width // 2 and y < height // 2:
        quadrants[1] += 1
    elif x < width // 2 and y > height // 2:
        quadrants[2] += 1
    elif x > width // 2 and y > height // 2:
        quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

min_var_x = float("inf")
min_var_y = float("inf")

loop_x = -1
loop_y = -1

for i in range(duration):
    for robot in robots:
        robot.position.x = (robot.position.x + robot.velocity.x + width) % width
        robot.position.y = (robot.position.y + robot.velocity.y + height) % height

    var_x = variance(robot.position.x for robot in robots)
    if var_x < min_var_x:
        min_var_x = var_x
        loop_x = i

    var_y = variance(robot.position.y for robot in robots)
    if var_y < min_var_y:
        min_var_y = var_y
        loop_y = i

y = 0
while True:
    x = Fraction(loop_y - loop_x + y * height, width)
    if x.is_integer() and x > 0:
        break
    y += 1
duration = int(loop_x + x * width + 1)
print(duration)

image = Image.new("1", (width, height))
for robot in parse_robots(input):
    x = (robot.position.x + (robot.velocity.x + width) * duration) % width
    y = (robot.position.y + (robot.velocity.y + height) * duration) % height
    image.putpixel((x, y), 1)
image.show()
