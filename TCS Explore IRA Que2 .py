class Doctor:
	def __init__(self,id,drName,deptName,fee,availability):
		self.id = id
		self.drName = drName
		self.deptName = deptName
		self.fee = fee
		self.availability = availability

class Hospital:
	def __init__(self,objList):
		self.objList = objList

	def getDrList(self,deptName):
		d = {}
		for dr in self.objList:
			if dr.deptName == deptName and dr.availability == "available":
				d[dr.id] = dr.drName
		return d

	def selectDr(self,fee):
		d = {}
		for dr in self.objList:
			if dr.availability == 'available':
				# self.objList.remove(dr)
				result = str(dr.id) + ' ' + dr.drName
				d[dr.fee] = result
		return d 



if __name__ == '__main__':
	objList = []
	for i in range(5):
		id = int(input())
		drName = input()
		deptName = input()
		fee = int(input())
		availability = input()
		objList.append(Doctor(id,drName.lower(),deptName.lower(),fee,availability.lower()))

	obj = Hospital(objList)

	deptName = input().lower()
	fee = int(input())

	#task1
	d1 = obj.getDrList(deptName)
	if len(d1) == 0:
		print("Dr not found")

	else:
		for key,val in d1.items():
			print(key,val,sep=' ')

	#task 2
	d2 = obj.selectDr(fee)
	for key in sorted(d2.keys()):
		val = d2[key]
		print(val,key,sep=' ')

