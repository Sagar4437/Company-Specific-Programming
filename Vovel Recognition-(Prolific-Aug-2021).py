'''
Que:
    The task is to find the presence of vowels in all possible substrings of the given string

Input:
    'baceb'

Output:
    16

Discription:
   Posible substrings:['b', 'ba', 'bac', 'bace', 'baceb', 'a', 'ac', 'ace', 'aceb', 'c', 'ce', 'ceb', 'e', 'eb', 'b']

   Resultant string = "bbabacbacebacebaacaceacebccecebeebb"

   Total vowels in string are 16 hence output is 16.

'''




def fun(s):
	s = s.lower()
	vo = 'aeiou'
	arr1 = [s[i:j] for i in range(len(s)) for j in range(i,len(s)+1)]

	count = 0
	string = ''.join(arr1)
	for i in string:
		if i in vo :
			count += 1

	print(count)

s = input('Enter a string ')
fun('baceb')
