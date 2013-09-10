#!/usr/bin/python

import MySQLdb as mysql
import cmd, sys

# Open database connection
db = mysql.Connection(host="localhost", user="root", passwd="root", db="dnd35")
cursor = db.cursor()

# Queries the database for monster information
def queryMonster(_table, _name):
	global db
	global cursor
	sql = "SELECT name, hit_dice, armor_class FROM " + _table + " WHERE name = \"" + _name + "\";"
	columns = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			for stat in row:
				columns.append(str(stat))
	except:
	   print "Error: unable to fetch data."
	return columns


# Queries the database for the columns of a table
def queryColumns(_table):
	global db
	global cursor
	sql = "SHOW columns FROM " + _table + ";"
	columns = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			columns.append(str(row[0]))
	except:
	   print "Error: unable to fetch data."
	return columns

# Queries the database for the names of a table
def queryList(_table):
	global db
	global cursor
	sql = "SELECT name FROM " + _table + ";"
	names = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			names.append(str(row[0]))
	except:
	   print "Error: unable to fetch data."
	return names

# class for command-line interpreter
class PelorShell(cmd.Cmd):

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
	
	# monster
	def do_monster(self, arg):
		if arg == "":
			print "\n".join(queryList("monster"))
		else:
			print "\n".join(queryMonster("monster", str(arg)))
	def help_monster(self):
		print "Queries for information about monsters."
	def complete_monster(self, text, line, begidx, endidx):
		options = queryList("monster")
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
