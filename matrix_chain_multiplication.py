#!/bin/python

#The i/p matrices are :
#A1=30*35
#A2=35*15
#A3=15*5
#A4=5*10
#A5=10*20
#A6=20*25

#Representing the i/p matrices as a sequence
#TO-DO : Create this sequence as per user i/p
p={0:30, 1:35, 2:15, 3:5, 4:10 , 5:20 , 6: 25}
print p

def print_parens(s, i, j ):
	if( i==j ) :
		print "\bA[", i, "]",
	else :
		print '\b (',
		#print ( '( ', end=""),
		print_parens(s, i, s[i][j] )
		print_parens(s, s[i][j]+1, j)
		print '\b) ',
		#print ( ') ', end=''),
	
def main():
    n=( len(p.keys())-1 )

    #Taking one extra row in matrix, intentionally.
    #The algo has assumed matrices starting from 1, so instead of changing the algo,
    #I have taken one extra row.
    m=[[0 for x in xrange(n+1)] for x in xrange(n+1)]
    s=[[0 for x in xrange(n+1)] for x in xrange(n+1)]

    for l in range(2,n+1) : #l=chain length
	    for i in range(1,n-l+2) :
		    j=i+l-1
		    m[i][j]=999999999 #infinity
		    for k in range(i,j):
			    q=m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
			    if(q<m[i][j]) :
				    m[i][j]=q
				    s[i][j]=k

    #Now lets print the output with parentheses				    
    print_parens(s,1, n)

main()
