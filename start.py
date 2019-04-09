import time
import os
import sys
import psutil
from subprocess import PIPE, Popen
from psutil import process_iter
from signal import SIGTERM

def all_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)
	
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200

	# Start Tickerplant
	p = Popen(["q", "tick.q","schema","journal", "-p", "5010"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

	# Start HDB
	p = Popen(["q", "hdb", "-p", "5012"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

	# Start RDB 1
	p = Popen(["q", "tick/r.q", "-p", "5011"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

	# Start RDB 2
	p = Popen(["q", "tick/r.q", "-p", "5013"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)
	
	# Start CEP
	p = Popen(["q", "tick/r.q","-p", "5015"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)
	
	# Start feedhandler
	p = Popen(["q", "tick/feedhandler.q","-p", "5014"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)
	
	
def tickerplant_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)

	# Start Tickerplant
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "tick.q","schema","journal", "-p", "5010"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

def rdb1_start():
	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)
	
	# Start RDB 1
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "tick/r.q", "-p", "5011"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

def	rdb2_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")

	os.chdir(dir)
	
	# Start RDB 2
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "tick/r.q", "-p", "5013"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

def hdb_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")
	
	os.chdir(dir)

	# Start HDB
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "hdb", "-p", "5012"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)
	
def feedhandler_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")
	
	os.chdir(dir)

	# Start feedhandler
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "tick/feedhandler.q","-p", "5014"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)

def cep_start():

	# Assuming Python 3
	dir=input("Enter tick directory: ")
	
	os.chdir(dir)

	# Start CEP
	DETACHED_PROCESS = 0x00000008
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	p = Popen(["q", "tick/r.q","-p", "5015"], stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
	time.sleep(1)
	
def rename_keys(d, keys):
	return ([(keys.get(k), v) for k, v in d.items()])

	
def start():

		options = {"tickerplant" : tickerplant_start,
					"hdb" : hdb_start,
					"rdb1" : rdb1_start,
					"rdb2" : rdb2_start,
					"all" : all_start,
					"feedhandler":feedhandler_start,
					"cep":cep_start,
		}
		options[sys.argv[2]]()
		
		
def stop():
	
	s=sys.argv[2]
	dict =	{"tickerplant": 5010,
				 "hdb": 5012,
				 "rdb1": 5011,
				 "feedhandler":5014,
				 "rdb2":5013,
				 "cep":5015		
	}
	if s=="all":
		for proc in process_iter():
			for conns in proc.connections(kind='inet'):
				if conns.laddr[1] in dict.values():
					 try:
							proc.send_signal(SIGTERM)
					 except psutil.NoSuchProcess:
							continue
	else:
		port=dict[s]
		for proc in process_iter():
				for conns in proc.connections(kind='inet'):
					if conns.laddr[1] == port:
						proc.send_signal(SIGTERM)
	
		

def test():

	v1=sys.argv[2]

	dictAll =	{5010:"",
				 5012:"",
				 5011:"",
				 5014:"",
				 5013:"",
				 5015:"",		
		}
		
	dictRename =	{ 5010:"tickerplant",
				 5012:"hdb",
				 5011:"rdb1",
				 5014:"feedhandler",
				 5013:"rdb2",
				 5015:"cep",		
	}
	
	dictSingle =	{"tickerplant": 5010,
				 "hdb": 5012,
				 "rdb1": 5011,
				 "feedhandler":5014,
				 "rdb2":5013,
				 "cep":5015		
	}
	
	if v1=="all":
		for s in dictAll.keys():
			for proc in process_iter():	
				for conns in proc.connections(kind='inet'):
					if conns.laddr[1] == s:
						dictAll[s]="UP"
						
		for s in dictAll.keys():
			if dictAll[s]=="":
				dictAll[s]="DOWN"
				
		dictNew=rename_keys(dictAll, dictRename)
		for s in dictNew:
			print(s[0]+" : "+s[1]+"\n")
			
	else:
		i=0
		for proc in process_iter():
			for conns in proc.connections(kind='inet'):
				if conns.laddr[1] == dictSingle[v1]:
					print(v1+" : UP")
					i=1
		
		if i==0:
			print(v1+" : DOWN")


options = {"start" : start,
		   "stop" : stop,
		   "test" : test,
	}

	

session=sys.argv[1]
	
options[session]()
	


	

