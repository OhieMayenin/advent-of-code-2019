import math

components_URL = 'https://adventofcode.com/2019/day/1/input'


def calculate_fuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel


def calculate_fuel_pt2(mass):
    fuel = math.floor(mass/3) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + calculate_fuel_pt2(fuel)


total_fuel = 0


with open('components.txt', 'r') as components:
    for line in components:
        total_fuel += calculate_fuel_pt2(int(line))


print("Total fuel required: ", total_fuel)

