import cmd
from room import get_room
from pprint import pprint


class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)

		self.loc = get_room(1)
		self.look()

	def move(self, dir):
		pprint(self.loc)
		newsroom = self.loc._neighbors(dir)
		if newsroom is None:
			print("You stumble into a wall")
		else:
			self.loc = get_room(newsroom)

	def look(self):
		print(self.loc.name)
		print("")
		print(self.loc.description)

	def do_n(self, args):
		"""Go north"""
		self.move('n')

	def do_e(self, args):
		"""Go east"""
		self.move('e')

	def do_s(self, args):
		"""Go south"""
		self.move('s')

	def do_w(self, args):
		"""Go west"""
		self.move('w')

	def do_quit(self, args):
		"""Leaves the game"""
		print("Thank you for playing")
		return True

if __name__ == "__main__":
	g = Game()
	g.cmdloop()