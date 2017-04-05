"""create a function called binary_conveter. inside the funtion, implement an 
algorithm to convert binary numbers between 0 and 255 to their binary equivalents.
For any invalid input return invalid input."""
def binary_conveter(n):
	if n == 0:
		return 0
	elif n < 0:
		return "invalid input"
	elif n > 255:
		return "invalid input"
	else:
		answer = ""
		while n > 0:
			temp = n % 2
			answer = str(temp) + answer
			n = n/2
		return answer
