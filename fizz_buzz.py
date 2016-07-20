#tackling the fiz_buzz_problem
a = range(1,100)
for number in a:
	if (number%3 ==0) and (number%5 == 0):
			 print 'fizz_buzz'
	 elif number%3 == 0:
			 print 'fizz'
	 elif number%5 == 0:
			 print 'buzz'
	 else:
			 print number
