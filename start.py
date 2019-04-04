import time
import os
import sys

def all():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)

	# Start Tickerplant
	os.system("start cmd /c q tick.q schema journal -p 5010")
	time.sleep(5)

	# Start HDB
	os.system("start cmd /c q hdb -p 5012")
	time.sleep(5)

	# Start RDB 1
	os.system("start cmd /c q tick/r.q -p 5011")
	time.sleep(5)

	# Start RDB 2
	os.system("start cmd /c q tick/r.q -p 5013")
	time.sleep(5)
	
	# Start feedhandler
	os.system("start cmd /c q tick/feedhandler.q -p 5014")
	time.sleep(5)
	
def tickerplant():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)

	# Start Tickerplant
	os.system("start cmd /c q tick.q schema journal -p 5010")
	time.sleep(5)

def rdb1():
	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)
	
	# Start RDB 1
	os.system("start cmd /c q tick/r.q -p 5011")
	time.sleep(5)

def	rdb2():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)
	
	# Start RDB 2
	os.system("start cmd /c q tick/r.q -p 5013")
	time.sleep(5)

def hdb():

	# Assuming Python 3
	dir=input("Enter tick directory: ")
	
	os.chdir(dir)

	# Start HDB
	os.system("start cmd /c q hdb -p 5012")
	time.sleep(5)
	
def feedhandler():

	# Assuming Python 3
	dir=input("Enter tick directory: ")
	
	os.chdir(dir)

	# Start feedhandler
	os.system("start cmd /c q tick/feedhandler.q -p 5014")
	time.sleep(5)


	
options = {"tickerplant" : tickerplant,
           "hdb" : hdb,
           "rdb1" : rdb1,
           "rdb2" : rdb2,
		   "all" : all,
		   "feedhandler":feedhandler,
	}
	
session=sys.argv[1]
	
options[session]()
	


	

