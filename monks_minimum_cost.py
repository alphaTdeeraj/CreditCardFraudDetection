class Manager():
	def calling(self):
		return self.get_name()
		


class model():
	def __init__(self, name , place):
		self.name = name 
		self.place = place
		self.objects = Manager()

	def get_name(self):
		return self.name


deeru = model('deeraj', 'bangalore')
print(deeru.objects.calling())