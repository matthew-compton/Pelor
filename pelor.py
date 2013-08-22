#!/usr/bin/python

import sqlite3 as db
import cmd, sys

# class for command-line interpreter
class PelorShell(cmd.Cmd):

	con = None
	try:
		con = db.connect('test.db')
		cur = con.cursor()    
		cur.execute('SELECT SQLITE_VERSION()')
		data = cur.fetchone()
		print "SQLite version: %s" % data                

	except db.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close()

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
