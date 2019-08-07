
class Tree():
	"""A class to modet a basic tree."""
	
	def __init__(self,tree_type,height,age,color,location,health):
		self.tree_type = tree_type
		self.height = height #in feet
		self.age = age
		self.color = color
		self.location = location
		self.health = health #0 = dead, 100 = healthy
		
	def strike_lightning(self,intensity):
		print('you were struck by lightning')
		self.health -= intensity
		self.color = 'grey'
	
	def age_healthy_season(self):
		self.health += 15 
		if self.health > 100:
			self.health = 100
		self.age += 1
		self.height += 2
		self.color = 'green'
	def print_tree_des(self):
		print("This is a " + self.tree_type + " tree that has lived through" + 
				self.age + " and is " + self.height + " feet tall. It lives on" + 
				self.location + ", it's color is " + self.color + ", and it's health is "
				 + self.health + "."
				 )		
		
		
my_first_tree = Tree('pine', 8, 5, 'green', 'Mt. Helena', 96)
my_first_tree.print_tree_des()
my_first_tree.strike_lightning(20)
my_first_tree.print_tree_des()
my_first_tree.age_healthy_season
my_first_tree.print_tree_des()
		
