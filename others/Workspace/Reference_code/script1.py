T=12000  # nomer nulya

import os
import sys
#print sys.argv[1]

# input mod chara ntheta level size bits
inpfile=sys.argv[1]
modulo=int(sys.argv[2])
chara=int(sys.argv[3])
ntheta=int(sys.argv[4])
level=int(sys.argv[5])
size=int(sys.argv[6])
bits=int(sys.argv[7])


proc=int(sys.argv[8])

pref=sys.argv[9]

index=proc
#index = os.environ.get('SGE_TASK_ID')
index1 = os.environ.get('PBS_JOBID')
#print index

#index1=int(index)


S = "./tridiagonal "
S2 = "echo "
Sout="tridiag/out"
Soutsuf=".trig"
SPref="~/Short/determinant/eigen/"
P1=" -real "
P2=" -fftmult"
P2=" -directmult"
P2=" -fastmult"
#directmult


for m in range(1, 2):
	n=m+index-1
	leveln=level+n-1
	S2=S+ ' -infile "' +inpfile + '" -outfile "'+pref+Sout+str(modulo).zfill(3)+"_"+str(chara).zfill(3)+"_"+str(size).zfill(6)+"_"+str(n).zfill(2)+Soutsuf+ '" -modulus '+str(modulo)+ " -character " + str(chara)+ " -ntheta " + str(ntheta)+ " -level " + str(leveln)+ " -size "+ str(size) +  " -numbits "+ str(bits) +P1 +P2;
#+" > /dev/null 2>&1"; 
	os.system(S2);
#	print(S2);

