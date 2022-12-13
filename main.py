"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 2
Author: Diego Marmsoler
"""
import sys
import re

#Alice
rightsalice = {}
alicemaxprio = ''
alicemaxcat = []
alicecurrentprio = ''
alicecurrentcat = []

file1 = open('alice.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsalice[1]=result.group(1)
rightsalice[2]=result.group(2)
rightsalice[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicecurrentcat.append(c)

#Bob
rightsbob = {}
bobmaxprio = ''
bobmaxcat = []
bobcurrentprio = ''
bobcurrentcat = []

file1 = open('bob.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsbob[1]=result.group(1)
rightsbob[2]=result.group(2)
rightsbob[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobmaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobmaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobcurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobcurrentcat.append(c)

#Charlie
rightscharlie = {}
charliemaxprio = ''
charliemaxcat = []
charliecurrentprio = ''
charliecurrentcat = []

file1 = open('charlie.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightscharlie[1]=result.group(1)
rightscharlie[2]=result.group(2)
rightscharlie[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliecurrentcat.append(c)

#MAIN

def ssc(alice, bob, charlie):
	print(bob)
	satisfy=0
	#Check for alice
	count=3
	if not alice:
		count=count-1

	if not bob:
		count=count-1

	if not charlie:
		count=count-1


	if alice.get('1',"NO")!="NO":
		if (alice.get('1')=='r' or alice.get('1')=='w'):
			satisfy=satisfy+1
		if (alice.get('1')=='a'):
			satisfy=satisfy+1
	elif alice.get('2',"NO")!="NO":
		if (alice.get('2')=='r' or alice.get('1')=='w'):
			if (alice.get('2')=='a'):
				satisfy=satisfy+1
	elif alice.get('3', "NO") != "NO":
		if (alice.get('3') == 'r' or alice.get('3') == 'w'):
			satisfy=satisfy+1
		if (alice.get('3') == 'a'):
			satisfy = satisfy + 1

	if bob.get('1',"NO")!="NO":
		if (bob.get('1')=='r' or bob.get('1')=='w'):
			satisfy=satisfy+1
		if (bob.get('1')=='a'):
			satisfy=satisfy+1
	elif bob.get('2',"NO")!="NO":
		if (bob.get('2')=='r' or bob.get('1')=='w'):
			if (bob.get('2')=='a'):
				satisfy=satisfy+1
	elif bob.get('3', "NO") != "NO":
		if (bob.get('3') == 'r' or bob.get('3') == 'w'):
			satisfy=satisfy+1
		if (bob.get('3') == 'a'):
			satisfy=satisfy+1

	if charlie.get('1',"NO")!="NO":
		if (charlie.get('1')=='r' or charlie.get('1')=='w'):
			satisfy=satisfy+1
		if (charlie.get('1')=='a'):
			satisfy=satisfy+1
	elif charlie.get('2',"NO")!="NO":
		if (charlie.get('2')=='r' or charlie.get('1')=='w'):
			if (charlie.get('2')=='a'):
				satisfy=satisfy+1
	elif charlie.get('3', "NO") != "NO":
		if (charlie.get('3') == 'r' or charlie.get('3') == 'w'):
			satisfy=satisfy+1
		if (charlie.get('3') == 'a'):
			satisfy=satisfy+1

	if(count == satisfy):
		return True
	else:
		return False

def star(alice, bob, charlie):
	satisfy = 0
	# Check for alice
	count = 3
	if not alice:
		count = count - 1

	if not bob:
		count = count - 1

	if not charlie:
		count = count - 1

	if alice.get('1', "NO") != "NO":
		if (alice.get('1') == 'r'):
			satisfy = satisfy
		if (alice.get('1') == 'a'):
			satisfy = satisfy + 1
		if (alice.get('1') == 'w'):
			satisfy = satisfy
	elif alice.get('2', "NO") != "NO":
		if (alice.get('2') == 'r'):
			satisfy=satisfy
		if (alice.get('2') == 'a'):
			satisfy = satisfy
		if (alice.get('1') == 'w'):
			satisfy = satisfy
	elif alice.get('3', "NO") != "NO":
		if (alice.get('3') == 'r'):
			satisfy = satisfy
		if (alice.get('3') == 'a'):
			satisfy = satisfy
		if (alice.get('1') == 'w'):
			satisfy = satisfy

	if bob.get('1', "NO") != "NO":
		if (bob.get('1') == 'r'):
			satisfy = satisfy
		if (bob.get('1') == 'a'):
			satisfy = satisfy + 1
		if (bob.get('1') == 'w'):
			satisfy = satisfy
	elif bob.get('2', "NO") != "NO":
		if (bob.get('2') == 'r'):
			satisfy=satisfy
		if (bob.get('2') == 'a'):
			satisfy = satisfy
		if (bob.get('1') == 'w'):
			satisfy = satisfy
	elif bob.get('3', "NO") != "NO":
		if (bob.get('3') == 'r'):
			satisfy = satisfy
		if (bob.get('3') == 'a'):
			satisfy = satisfy
		if (bob.get('1') == 'w'):
			satisfy = satisfy

	if charlie.get('1', "NO") != "NO":
		if (charlie.get('1') == 'r'):
			satisfy = satisfy
		if (charlie.get('1') == 'a'):
			satisfy = satisfy + 1
		if (charlie.get('1') == 'w'):
			satisfy = satisfy
	elif charlie.get('2', "NO") != "NO":
		if (charlie.get('2') == 'r'):
			satisfy = satisfy
		if (charlie.get('2') == 'a'):
			satisfy = satisfy
		if (charlie.get('1') == 'w'):
			satisfy = satisfy
	elif charlie.get('3', "NO") != "NO":
		if (charlie.get('3') == 'r'):
			satisfy = satisfy
		if (charlie.get('3') == 'a'):
			satisfy = satisfy
		if (charlie.get('1') == 'w'):
			satisfy = satisfy

	if (count == satisfy):
		return True
	else:
		return False

def ds(alice, bob, charlie):
	satisfy = 0
	# Check for alice
	count = 3
	if not alice:
		count = count - 1

	if not bob:
		count = count - 1

	if not charlie:
		count = count - 1

	if alice.get('1', "NO") != "NO":
		if (alice.get('1') == 'r'):
			satisfy = satisfy
		if (alice.get('1') == 'a'):
			satisfy = satisfy
		if (alice.get('1') == 'w'):
			satisfy = satisfy+1
	elif alice.get('2', "NO") != "NO":
		if (alice.get('2') == 'r'):
			satisfy = satisfy+1
		if (alice.get('2') == 'a'):
			satisfy = satisfy
		if (alice.get('1') == 'w'):
			satisfy = satisfy
	elif alice.get('3', "NO") != "NO":
		if (alice.get('3') == 'r'):
			satisfy = satisfy
		if (alice.get('3') == 'a'):
			satisfy = satisfy+1
		if (alice.get('1') == 'w'):
			satisfy = satisfy

	if bob.get('1', "NO") != "NO":
		if (bob.get('1') == 'r'):
			satisfy = satisfy
		if (bob.get('1') == 'a'):
			satisfy = satisfy
		if (bob.get('1') == 'w'):
			satisfy = satisfy+1
	elif bob.get('2', "NO") != "NO":
		if (bob.get('2') == 'r'):
			satisfy = satisfy
		if (bob.get('2') == 'a'):
			satisfy = satisfy
		if (bob.get('1') == 'w'):
			satisfy = satisfy+1
	elif bob.get('3', "NO") != "NO":
		if (bob.get('3') == 'r'):
			satisfy = satisfy
		if (bob.get('3') == 'a'):
			satisfy = satisfy+1
		if (bob.get('1') == 'w'):
			satisfy = satisfy

	if charlie.get('1', "NO") != "NO":
		if (charlie.get('1') == 'r'):
			satisfy = satisfy
		if (charlie.get('1') == 'a'):
			satisfy = satisfy
		if (charlie.get('1') == 'w'):
			satisfy = satisfy+1
	elif charlie.get('2', "NO") != "NO":
		if (charlie.get('2') == 'r'):
			satisfy = satisfy+1
		if (charlie.get('2') == 'a'):
			satisfy = satisfy
		if (charlie.get('1') == 'w'):
			satisfy = satisfy
	elif charlie.get('3', "NO") != "NO":
		if (charlie.get('3') == 'r'):
			satisfy = satisfy
		if (charlie.get('3') == 'a'):
			satisfy = satisfy+1
		if (charlie.get('1') == 'w'):
			satisfy = satisfy

	if (count == satisfy):
		return True
	else:
		return False

alice = {}
bob = {}
charlie = {}
c = re.compile('^([ABC]):([123]):([rwa])$')
args=sys.argv[1:]
while (len(args)>0):
	input=args.pop(0)
	result=c.search(input)
	if (not result):
		raise SystemExit("Usage: blpcheck.py [ABC]:[123]:[rwa] ...")
	if (result.group(1)=='A'):
		if result.group(2) in alice:
			raise SystemExit("duplicate entry")
		alice[result.group(2)]=result.group(3)
	if (result.group(1)=='B'):
		if result.group(2) in bob:
			raise SystemExit("duplicate entry")
		bob[result.group(2)]=result.group(3)
	if (result.group(1)=='C'):
		if result.group(2) in charlie:
			raise SystemExit("duplicate entry")
		charlie[result.group(2)]=result.group(3)

print ("SSC: ", "Yes" if ssc(alice, bob, charlie) else "No")
print ("Star: ", "Yes" if star(alice, bob, charlie) else "No")
print ("DS: ", "Yes" if ds(alice, bob, charlie) else "No")