class Panting:
	def __init__(self,Id,price,name,pType):
		self.Id = Id
		self.price = price
		self.name = name
		self.pType = pType

class ShowRoom:
	def __init__(self,obj_list_of_panting):
		self.obj_list_of_panting = obj_list_of_panting

	def getPrice(self,pType):
		c = 0
		for paint in self.obj_list_of_panting:
			if paint.pType.lower() == pType.lower():
				c += paint.price

		if c == 0:
			return None
		else:
			return c 

	def getNameOfPainter(self):
		d = {}
		arr = []
		for paint in self.obj_list_of_panting:
			if paint.name in d:
				d[paint.name] += 1
			else:
				d[paint.name] = 1

		maxVal = max(d.values())

		for key,val in d.items():
			if val == maxVal:
				arr.append(key)

		arr.sort()
		return arr[0]

		
if __name__ == '__main__':
	obj_list_of_panting = []
	n = int(input())
	for i in range(n):
		Id = input()
		name = input()
		price = int(input())
		pType = input()
		obj_list_of_panting.append(Panting(Id,price,name,pType))

	#output code
	pType = input()
	obj = ShowRoom(obj_list_of_panting)

	val = obj.getPrice(pType)
	print(val)

	result = obj.getNameOfPainter()
	print(result)
	


