import cmd, sys

class PelorShell(cmd.Cmd):
	intro = "Hail Pelor!\nType 'help' or '?' to list commands.\nType 'quit' or 'exit' to escape.\n"
	prompt = 'pelor ~ $ '
	ruler = '-'
    
	# ----- Commands -----
	
	# color
	_AVAILABLE_COLORS = ('blue', 'green', 'yellow', 'red', 'black')
	def do_color(self, arg):
		if arg == "":
			print "Enter color."
		else:
			print str(arg)
	def help_color(self):
		print 'Prints the name of a color.'
	def complete_color(self, text, line, begidx, endidx):
		return [i for i in _AVAILABLE_COLORS if i.startswith(text)]

	# exit
	def do_exit(self, s):
		return True
	def help_exit(self):
		print "Exit the interpreter."
		
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

if __name__ == '__main__':
	shell = PelorShell()
    shell.cmdloop()
