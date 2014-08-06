import sys

x1 = int(sys.argv[1])
x2 = int(sys.argv[2])
x3 = int(sys.argv[3])
x4 = int(sys.argv[4])

z = (x1 + x2 + x3 + x4) / 4

print "The average score is:",z

if z >= 90:
	g = "A"
elif z >= 80:
	g = "B"
elif z >= 70:
	g = "C"
elif z >= 60:
	g = "D"
else:
	g = "F"

print "Letter Grade:",g