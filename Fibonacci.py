def fibonacci(num):
	x = 0
	y = 1
	z = 0
	ans = ""
	
	if num == 0:
		print 0
	while x + z <= num:
		x += z
		z = y
		y = x
		if ans != "":
			ans = ans + ", " + str(x)
		else:
			ans = str(x)
	print ans
	
	
def main():
	fNum = input("What is the maximum number? ")
	
	if fNum <= 0:
		print("Please enter a number greater than 0.")
	fibonacci(fNum)

if __name__ == '__main__':
    main()