import sys
import numpy as np
import os
PGAP = 2 

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



def main():
	args = sys.argv
	DNA = []
	for i,file in enumerate(args[1:3]):
		DNA.append(readfile(file))
	lenA=len(DNA[0])
	lenB=len(DNA[1])

	matrix=np.zeros(
		(lenB+1,lenA+1), dtype=int)
	for x in range(lenA+1):
		matrix[0][x]=-x*PGAP
	for y in range(lenB+1):
		matrix[y][0]=-y*PGAP
	
	for y in range(1,lenB+1):
		for x in range(1,lenA+1):
			matrix[y][x]=calcF(matrix[y-1][x-1],matrix[y][x-1],matrix[y-1][x],DNA[0][x-1],DNA[1][y-1])
			#os.system('clear')
			#show(DNA[0],DNA[1],matrix)
	show(DNA[0],DNA[1],matrix)



	

if __name__ == '__main__':
	main()