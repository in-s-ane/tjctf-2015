'''
This is the output of python -x polandball_mess.py, which had the exec("".join(c))
statement switched to print "".join(c) to get this code
'''

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

import sys



def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == ".": sys.stdout.write(chr(cells[cellptr]))
    if command == ",": cells[cellptr] = ord(getch())
      
    codeptr += 1


def cleanup(code):
  return filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code)


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap




def genFile(): 
	code = ""
	f = open(__file__,"rb").read().split("%f")[1]
	for b in f:
		if b == "\xb0":
			code += "+"
		elif b == "\xb1":
			code += "-"
		elif b == "\xb2":
			code += ">"
		elif b == "\xb3":
			code += "<"
		elif b == "\xb4":
			code += "["
		elif b == "\xb5":
			code += "]"
		elif b == "\xb6":
			code += "."
		elif b == "\xb7":
			code += ","
	evaluate(code)


def main():
	genFile()

main()


