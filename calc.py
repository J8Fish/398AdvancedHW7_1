import sys

def func(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == "/":
		return a / b

if len(sys.argv) != 4:
	print("Wrong number of args: <num> <op> <num>")
	exit(1)

a = sys.argv[1]
op = sys.argv[2]
b = sys.argv[3]

print(func(int(a), int(b), op))