import urllib2
import curses
import sys
import os

def get_param(prompt_string):
  """Brings up new screen asking user to enter a single parameter.
 
  Args:
      prompt_string: Prompt which asks/tells user what to enter (string).
  """
  screen.clear()
  screen.border(0)
  screen.addstr(2, 2, prompt_string)
  screen.refresh()
  input = screen.getstr(10, 10, 60)
  return input
  

def file(types,session,username):
	print "\n"
	f=open('list.txt','r')
	print "Starting...\n"
	for dic in f:
		#print dic

		try:	
			req = urllib2.Request('http://%s.persiangig.com/%s%s/download?%s'%(str(username),(dic).rsplit()[0],str(types),str(session)))
			response = urllib2.urlopen(req)
			the_page = response.read()


			if "pg100.png" not in the_page:
				if "&#1776; b" not in the_page:
					print "File  ["+dic.rsplit()[0]+types+"]  Found !"
					ff=open('success.txt','a')
					ff.write(dic.rsplit()[0]+types+'\n')
					ff.close()
			else:
				print '[',dic.rsplit()[0],'] Session expired'
				session=raw_input("session: ").rsplit()[0] 
		except:
			print "err url"	
			
def dir(username):
	print "\n"
	f=open('list.txt','r')
	print "Starting...\n"
	for dic in f:
		#print dic

		try:	
			req = urllib2.Request('http://%s.persiangig.com/%s'%(str(username),(dic).rsplit()[0]))
			response = urllib2.urlopen(req)
			the_page = response.read()

		
			if "pg100.png" not in the_page:
				print "Directory  ["+dic.rsplit()[0]+"]  Found !"
				ff=open('success-dir.txt','a')
				ff.write(dic.rsplit()[0]+'\n')
				ff.close()
		except:
			print "err url"	

def info():
	os.system('cls')
	print "Persiangig file and directory finder trough the list!"
	print "\n\t"
	print "you have URL like : \nhttp://hacker.persiangig.com/file.rar/download?010d\n\n"
	print "value will be  :\nhttp://[username].persiangig.com/[file type]/download?[session]"
	print "\n\t\t\t\t\t\n"

			
x = 0

while x != ord('4'):
	screen = curses.initscr()
	curses.start_color()       # Must call this before creating pairs.
	
	# Create hardcoded color pairs (foreground/background) to use:
	#curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	#curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
	#curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	screen.clear()
	screen.border(0)
	screen.addstr(screen.getmaxyx()[0]-1,1,"Copyright ITSecZone co. (http://www.nezami.info)")
	screen.addstr(2, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Directory Finder")
	screen.addstr(5, 4, "2 - File Finder")
	screen.addstr(6, 4, "3 - Usage")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
	
		try:
			username = get_param('Enter your username of persiangig: ').rsplit()[0]
		except:
			sys.exit("err user input!")
		curses.endwin()
		dir(username)
		raw_input('Press enter (to return to main)')
		
	if x == ord('2'):
	
		try:
			types = get_param('Enter your types of file name:\n Example : .rar or .zip ... ').rsplit()[0]
			session = get_param('Enter your session name:\n Session must be in 4 digit end of url ').rsplit()[0]
			username = get_param('Enter your username:\nUsername of persiangig. ').rsplit()[0]
		except:
			sys.exit("err user input!")
		curses.endwin()
		file(types,session,username)
		raw_input('Press enter (to return to main)')
	if x == ord('3'):
		curses.endwin()
		info()
		raw_input('Press enter (to return to main)')
		
curses.endwin()
