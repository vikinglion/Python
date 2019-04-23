class User():
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		
	def describe_user(self):
		print("Name: " + self.firstname.title() + ' ' + self.lastname.title())
		
	def greet_user(self):
		print("Hello there, Mr." + self.firstname.title() + "!")

assassin = User('ezio', 'auditore')
stan = User('stan', 'marsh')

assassin.describe_user()
assassin.greet_user()

stan.describe_user()
stan.greet_user()
