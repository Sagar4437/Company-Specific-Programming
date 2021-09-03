#https://www.computerdeveloper.in/2021/04/tcs-xplore-ira-08-mar-2021-python-coding-question.html

class Employee:
	def __init__ (self,name,designation,salary,leaveDict):
		self.name = name
		self.designation = designation
		self.salary = salary
		self.leaveDict = leaveDict



class Organisation:
	def __init__(self,empObj_list,):
		self.empObj_list = empObj_list

	def checkLeave(self,name,leaveType,days):
		leaveType = leaveType.upper()
		for emp in self.empObj_list:
			if emp.name == name and emp.leaveDict[leaveType] > days:
				emp.leaveDict[leaveType] -= days
				return True
		if emp.name != name:
		    return 'not found'
		return False

	def show(self,name):
		for emp in self.empObj_list:
			if emp.name == name:
				for i in emp.leaveDict:
					print(i,emp.leaveDict[i],sep =':')

if __name__ == '__main__':
	n = int(input())
	empObj_list = []
	for i in range(n):
		name = input()
		designation = input()
		salary = int(input())
		pair = int(input())
		leaveDict = {}
		for j in range(pair):
			leaveType = input()
			days = int(input())
			leaveDict[leaveType] = days

		obj = Employee(name,designation,salary,leaveDict)
		empObj_list.append(obj)

	name = input()
	leaveType = input()
	days = int(input())
	
	obj = Organisation(empObj_list)

	#output:
	if obj.checkLeave(name,leaveType,days) == True:
		print('leave granted')
		obj.show(name)


	elif obj.checkLeave(name,leaveType,days) == False :
		print('leave not granted')
		obj.show(name)
		
	else:
	    print('leave not granted')
	    print("Employee not found")	    


