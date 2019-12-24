#!/usr/bin/env python3

INPUT_FILE = "input.txt" 

class IntcodeProgram:

	def __init__(self, intcode):
		self.intcode = intcode.copy()
		opcode_indices = range(0, len(self.intcode), 4)

		for idx in opcode_indices:
			opcode = self.intcode[idx]

			if opcode == 1:
				self._opcode_add(idx)
			elif opcode == 2:
				self._opcode_mul(idx)
			elif opcode == 99:
				break

	def _opcode_add(self, pos):
		left, right, dest = self.intcode[pos+1:pos+4]
		self.intcode[dest] = self.intcode[left] + self.intcode[right]
	
	def _opcode_mul(self, pos):
		left, right, dest = self.intcode[pos+1:pos+4]
		self.intcode[dest] = self.intcode[left] * self.intcode[right]

	def __getitem__(self, key):
		return self.intcode[key]

	def __str__(self):
		return str(self.intcode)

if __name__ == "__main__":

	with open(INPUT_FILE) as file:
		code = list(map(int, file.readline().split(',')))

		# restore "1202 program alarm" state
		code[1] = 12
		code[2] = 2

		program = IntcodeProgram(code)

		print(program[0])
