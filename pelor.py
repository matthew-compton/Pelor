#!/usr/bin/python

import MySQLdb as mysql
import cmd, sys

# class for command-line interpreter
class PelorShell(cmd.Cmd):

	# Open database connection
	db = mysql.Connection(host="localhost", user="root", passwd="root", db="dnd35")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = '''SELECT name, hit_dice FROM monster ORDER BY name''';
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
		  name = row[0]
		  hp = row[1]
		  # Now print fetched result
		  print "name=%s,hp=%s" % (name, hp)
	except:
	   print "Error: unable to fetch data."
	   
	# disconnect from server
	db.close()

	intro = "Hail Pelor!\nType 'help' or '?' to list commands.\nType 'quit' or 'exit' to escape.\n"
	prompt = "pelor ~ $ "
	ruler = "-"
		
	# ----- Commands -----
	
	# color
	def do_color(self, arg):
		if arg == "":
			print "Enter color."
		else:
			print str(arg)
	def help_color(self):
		print "Prints the name of a color."
	def complete_color(self, text, line, begidx, endidx):
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
		return True

if __name__ == "__main__":
	shell = PelorShell()
	shell.cmdloop()
