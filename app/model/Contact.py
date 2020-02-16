# from data.DatabaseHandler import DatabaseHandler as DBH

class Contact:

	def __init__(self,id,name,phoneNumber):
		self.id = id
		self.name = name
		self.phoneNumber = phoneNumber

	def getId(self):
		return self.id

	def setId(self,id):
		# this.id = id == reference to context
		return Contact.id

	def getName(self):
		return self.name

	def setName(self,name):
		# this.name = name
		return Contact.name

	def getPhoneNumber():
		return self.phoneNumber

	def setPhoneNumber(self,phoneNumber):
		return Contact.phoneNumber



class ContactLong(Contact):

	def __init__(self,id,name,phoneNumber):
		self.id = id
		self.name = name
		self.phoneNumber = phoneNumber


class ContactMain(Contact):

	def __init__(self):
		super().__init__(self)

class ContactStandard(Contact):
	def __init__(self,name,setPhoneNumber):
		self.name = name
		self.phoneNumber = phoneNumber

	
