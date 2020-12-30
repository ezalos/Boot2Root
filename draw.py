import turtle
import re
colors = ['blue', 'red', 'green', 'magenta']
NB_COLORS = len(colors)
if __name__ == '__main__':
	s = turtle.getscreen()
	t = turtle.Turtle()
	color_index = -1
	with open('turtle') as f:
		for line in f.readlines():
			match = re.search('Avance ([0-9]+) spaces', line)
			if (match):
				t.forward(int(match.group(1)))
				continue
			match = re.search('Recule ([0-9]+) spaces', line)
			if match:
				t.backward(int(match.group(1)))
				continue
			match = re.search('Tourne droite de ([0-9]+) degrees', line)
			if match:
				t.right(int(match.group(1)))
				continue
			match = re.search('Tourne gauche de ([0-9]+) degrees', line)
			if match:
				t.left(int(match.group(1)))
				continue
			if line == '\n':
				color_index += 1
				t.pencolor(colors[color_index % NB_COLORS])
	turtle.exitonclick()