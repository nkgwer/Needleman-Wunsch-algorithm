import sys
import numpy as np
import os
PGAP = 1
AlignmentsX=[]
AlignmentsY=[]
def getAlignment(x,y,str1,str2):
	global AlignmentsX
	global AlignmentsY
	if(x==0 and y==0):
		AlignmentsX.append(str1)
		AlignmentsY.append(str2)
	else:
		for arrow in arrow_matrix[y][x]:
			
			if(arrow=="D"):
				getAlignment(x-1,y-1,DNA[0][x-1]+str1,DNA[1][y-1]+str2)
			if(arrow=="U"):
				getAlignment(x,y-1,"_"+str1,DNA[1][y-1]+str2)
			if(arrow=="L"):
				getAlignment(x-1,y,DNA[0][x-1]+str1,"_"+str2)
			

def score(s1,s2):
	if(s1==s2):
		return 1
	else:
		return -1

def readfile(filename):
	f = open(filename, 'r')
	ret = f.readlines()[1]
	f.close()
	return ret


def calcF(diag,up,left,s1,s2):
	return max(diag+score(s1,s2),up-PGAP,left-PGAP)
def calcF_arrow(diag,up,left,s1,s2):
	diag=diag+score(s1,s2)
	up=up-PGAP
	left=left-PGAP
	maxvalue=max(diag,left,up)
	ret=[]
	if(diag==maxvalue):
		ret.append("D")
	if(up==maxvalue):
		ret.append("U")
	if(left==maxvalue):
		ret.append("L")
	return ret


def show(DNA1,DNA2,matrix):
	print "     ",
	for char in DNA1:
		print '{0:>3}'.format(char),
	print
	for i,r in enumerate(matrix):
		if(i>=1):
			print DNA2[i-1],
		else:
			print " ",
		for num in r:
			print '{0:>3}'.format(str(num)),
		print




args = sys.argv
DNA = []
for i,file in enumerate(args[1:3]):
	DNA.append(readfile(file))
lenA=len(DNA[0])
lenB=len(DNA[1])

matrix=np.zeros((lenB+1,lenA+1), dtype=int)
arrow_matrix=[[0 for i in range(lenA+1)]for i in range(lenB+1)]
for x in range(1,lenA+1):
	matrix[0][x]=-x*PGAP
	arrow_matrix[0][x]=["L"]
for y in range(1,lenB+1):
	matrix[y][0]=-y*PGAP
	arrow_matrix[y][0]=["U"]

for y in range(1,lenB+1):
	for x in range(1,lenA+1):
		matrix[y][x]=calcF(matrix[y-1][x-1],matrix[y-1][x],matrix[y][x-1],DNA[0][x-1],DNA[1][y-1])
		arrow_matrix[y][x]=calcF_arrow(matrix[y-1][x-1],matrix[y-1][x],matrix[y][x-1],DNA[0][x-1],DNA[1][y-1])
		#os.system('clear')
		#show(DNA[0],DNA[1],matrix)
show(DNA[0],DNA[1],matrix)
#show(DNA[0],DNA[1],arrow_matrix)
getAlignment(lenA,lenB,"","")
print DNA[0]+":",
print AlignmentsX
print DNA[1]+":",
print AlignmentsY

