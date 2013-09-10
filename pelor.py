#!/usr/bin/python

import MySQLdb as mysql
import cmd, sys

# Open database connection
db = mysql.Connection(host="localhost", user="root", passwd="root", db="dnd35")
cursor = db.cursor()

# class for command-line interpreter
class PelorShell(cmd.Cmd):

	# Queries the database for the columns of a table
	def queryTableColumns(_table):
		global db
		global cursor
		sql = "SHOW columns FROM " + _table
		columns = []
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				columns.append(row[0])
		except:
		   print "Error: unable to fetch data."
		return columns

	# Queries the database
	def query(_select, _from, _name):
		global db
		global cursor
		sql = "SELECT "
		for col in _select:
			sql += col + ", "
		sql = sql[:-2]
		sql += " FROM " + _from
		sql += " WHERE name = \"" + _name + "\";";
		print sql
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for row in results:
				for col in row:
					print col
		except:
		   print "Error: unable to fetch data."

	# Example queries
	#query(["name", "hit_dice", "armor_class"], "monster", "Yrthak");
	#print queryTableColumns("class")

	intro = "\nHail Pelor!\nType 'help' or '?' to list commands.\nType 'quit' or 'exit' to escape.\n"
	prompt = "pelor ~ $ "
	ruler = "-"
		
	# ----- Commands -----
	#| class           |
	#| class_table     |
	#| domain          |
	#| equipment       |
	#| feat            |
	#| item            |
	#| monster         |
	#| power           |
	#| skill           |
	#| spell           |
	
	# class
	def do_class(self, arg):
		if arg == "":
			print "Enter class."
		else:
			print str(arg)
	def help_class(self):
		print "Prints the name of a class."
	def complete_class(self, text, line, begidx, endidx):
		#print queryTableColumns("class")
		options = ["cat", "dog"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options

	# class_table
	def do_class_table(self, arg):
		if arg == "":
			print "Enter class_table."
		else:
			print str(arg)
	def help_class_table(self):
		print "Prints the name of a class_table."
	def complete_class_table(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# domain
	def do_domain(self, arg):
		if arg == "":
			print "Enter domain."
		else:
			print str(arg)
	def help_domain(self):
		print "Prints the name of a domain."
	def complete_domain(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# equipment
	def do_equipment(self, arg):
		if arg == "":
			print "Enter equipment."
		else:
			print str(arg)
	def help_equipment(self):
		print "Prints the name of a equipment."
	def complete_equipment(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# feat
	def do_feat(self, arg):
		if arg == "":
			print "Enter feat."
		else:
			print str(arg)
	def help_feat(self):
		print "Prints the name of a feat."
	def complete_feat(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# item
	def do_item(self, arg):
		if arg == "":
			print "Enter item."
		else:
			print str(arg)
	def help_item(self):
		print "Prints the name of a item."
	def complete_item(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# monster
	def do_monster(self, arg):
		if arg == "":
			print "Enter monster."
		else:
			print str(arg)
	def help_monster(self):
		print "Prints the name of a monster."
	def complete_monster(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# power
	def do_power(self, arg):
		if arg == "":
			print "Enter power."
		else:
			print str(arg)
	def help_power(self):
		print "Prints the name of a power."
	def complete_power(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# skill
	def do_skill(self, arg):
		if arg == "":
			print "Enter skill."
		else:
			print str(arg)
	def help_skill(self):
		print "Prints the name of a skill."
	def complete_skill(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options
			
	# spell
	def do_spell(self, arg):
		if arg == "":
			print "Enter spell."
		else:
			print str(arg)
	def help_spell(self):
		print "Prints the name of a spell."
	def complete_spell(self, text, line, begidx, endidx):
		options = ["blue", "green", "yellow", "red", "black"]
		if text:
			return [i for i in options if i.startswith(text)]
		else:
			return options

	# exit
	def do_exit(self, s):
		return True
	def help_exit(self):
		print "Quit the interpreter."
		
	# quit
	do_quit = do_exit
	help_quit= help_exit

	# ----- Properties -----
	
	# If empty line is entered just ignore it
	def emptyline(self):
		pass
		
	# Allows exiting from shell
	def can_exit(self):
		# disconnect from server
		db.close()
		return True

if __name__ == "__main__":
	shell = PelorShell()
	shell.cmdloop()
