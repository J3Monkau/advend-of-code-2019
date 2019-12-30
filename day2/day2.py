#!/usr/bin/env python3
from itertools import permutations

INPUT_FILE = "input.txt" 

class IntcodeProgram:

	def __init__(self, intcode):
		self.values = intcode.copy()
		instr_indices = range(0, len(self.values), 4)

		for idx in instr_indices:
			instruction = self.values[idx]

			if instruction == 1:
				self._opcode_add(idx)
			elif instruction == 2:
				self._opcode_mul(idx)
			elif instruction == 99:
				break

	@property
	def output(self):
		return self.values[0]

	def _opcode_add(self, pos):
		_, noun_addr, verb_addr, dest_addr = self.values[pos:pos+4]

		self.values[dest_addr] = \
				self.values[noun_addr] + \
				self.values[verb_addr]
	
	def _opcode_mul(self, pos):
		_, noun_addr, verb_addr, dest_addr = self.values[pos:pos+4]

		self.values[dest_addr] = \
				self.values[noun_addr] * \
				self.values[verb_addr]
	
	def __getitem__(self, key):
		return self.values[key]

	def __str__(self):
		return str(self.values)

if __name__ == "__main__":

	with open(INPUT_FILE) as file:
		code = list(map(int, file.readline().split(',')))

	print("---- DAY 2 ----")

	# --------- Part 1 ---------
	code_part1 = code.copy()

	code_part1[1:3] = 12, 2	# restore "1202 program alarm" state
	program_part1 = IntcodeProgram(code_part1)
	print("Answer part 1: %s" % program_part1.output)

	# --------- Part 2 ---------
	PART2_PROGRAM_OUTPUT = 19690720

	code_part2 = code.copy()
	search_range = range(len(code_part2))

	# search for params at 1 and 2 that produce the target ouput
	for verb, noun in permutations(search_range, r=2):
			code_part2[1:3] = verb, noun  # setting params
			program = IntcodeProgram(code_part2)
			if program.output == PART2_PROGRAM_OUTPUT:
				print("Answer part 2: verb=%s, noun=%s" % (verb, noun))
				exit(0)

	print("Failed to find noun and verb that cause the program to produce output %s" % PART2_PROGRAM_OUTPUT)
