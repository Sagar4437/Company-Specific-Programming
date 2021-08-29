'''
	Q: Find runnig Tax.

	Ip : [1000,2000,3000,4000,5000]

	Op : 1000

	Discription:
		val = 0 + 100.0 + 200.0 + 300.0 + 400.0 = 1000
		return val
'''


def calTotalTAx(input1,input2):
	arr = []
	for i in input2:
		if i > 1000:
			arr.append((i-1000)*0.1)

	print(arr)

	return(int(sum(arr)))



# Driver Code
if __name__ == '__main__':
	arr = [1000,2000,3000,4000,5000] # arr of amount
	l = len(arr)

	# find runningtax if amount is more than 1000
	
	val = calTotalTAx(l,arr)
	print(val)
