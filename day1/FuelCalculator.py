import math
from requests import get

components_URL = 'https://adventofcode.com/2019/day/1/input'


def calculate_fuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel


total_fuel = 0

with open('components.txt', 'r') as components:
    for line in components:
        # print(line)
        total_fuel += calculate_fuel(int(line))

print("Total fuel required: ", total_fuel)
