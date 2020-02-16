class UserLogin:

        """ login with user account based on email and password """

	def __init__(self,user_id,user_email,user_pass):
		self.userId = user_id
		self.userEmail = user_email
		self.userPass = user_pass

	def getId(self):
		return self.userId

	def setId(self,useId):
		return UserLogin.userId

	def getName(self):
		return self.userEmail

	def setName(self,userEmail):
		return UserLogin.userEmail

	def getUserPass(self):
		return self.userPass

	def setUserPass(self,userPass):
		return UserLogin.userPass
