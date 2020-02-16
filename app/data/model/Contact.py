# from data.DatabaseHandler import DatabaseHandler as DBH

class Contact:

	def __init__(self):
		self.uid = 0
		self.name = "empty"
		self.phoneNumber = "empty"

	def getId(self):
		return self.uid

	def setId(self,uid):
		# this.id = id == reference to context
		return Contact.uid

	def getName(self):
		return self.name

	def setName(self,name):
		# this.name = name
		return Contact.name

	def getPhoneNumber(self):
		return self.phoneNumber

	def setPhoneNumber(self,phoneNumber):
		return Contact.phoneNumber

contact = Contact()

if __name__ == '__main__':
    contact = Contact()


##class ContactLong(Contact):
##
##	def __init__(self,id,name,phoneNumber):
##		self.id = id
##		self.name = name
##		self.phoneNumber = phoneNumber
##
##
##class ContactMain(Contact):
##
##	def __init__(self):
##		super().__init__(self)
##
##class ContactStandard(Contact):
##	def __init__(self,name,setPhoneNumber):
##		self.name = name
##		self.phoneNumber = phoneNumber
##
##	
