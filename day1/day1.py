#!/usr/bin/env python3

INPUT_FILE = "input.txt"

def fuel_required(module_mass):
	return int(module_mass / 3) - 2

def fuel_required_for_fuel(module_mass):
	fuel_mass = fuel_required(module_mass)
	result = 0

	while fuel_mass > 0:
		result += fuel_mass
		fuel_mass = fuel_required(fuel_mass)

	return result


if __name__ == "__main__":
	with open(INPUT_FILE) as file:
		module_masses = [int(line) for line in file.readlines()]

	total_fuel_required = sum(map(fuel_required, module_masses))

	print("--- Part One ---")
	print("The sum of the fuel requirements for all of the modules is %s.\n" % total_fuel_required)

	total_fuel_required_for_fuel = sum(map(fuel_required_for_fuel, module_masses))

	print("--- Part Two ---")
	print("Fuel required for fuel is %s" % total_fuel_required_for_fuel)
