#!/usr/bin/env python 
import json
import sys
import os
import string

scriptpath = os.path.dirname(os.path.realpath(sys.argv[0]))

with open(scriptpath + '/mpi.json') as data_file:    
	mpi_interface = json.load(data_file)


IFACE=""

for f in mpi_interface:
	fd = mpi_interface[f]
	rtype=""
	if(f=="MPI_Wtime"):
		rtype = "double"
	else:
		rtype = "int"
	IFACE+= "snippet " + f + "\n"
	IFACE+= f + "("
	for i in range(0, len(fd)):
		arg=fd[i]
		name = arg[1];
		ctype = arg[0];
		#ARRAY CASE
		array=""
		try:
			idx=ctype.index("[")
		except ValueError:
			idx=-1
		if idx!=-1:
			array=ctype[idx:]
   			ctype=ctype[0:idx]
		IFACE+=" ${" + str(i+1) + ":" + ctype + " " + name + array + "} "
		if i < (len(fd) - 1):
			IFACE += ","

	IFACE+= ");\n"
	IFACE+= "endsnippet\n"

#This is the static part
IFACE += """
snippet mainmpi
#include <mpi.h>

int main( int argc, char *argv[])
{
	MPI_Init(&argc, &argv);

	${1:}

	MPI_Finalize();

	return 0;
}
endsnippet

snippet CS
MPI_COMM_SELF
endsnippet

snippet CW
MPI_COMM_WORLD
endsnippet
"""



f = open("./UltiSnips/c.snippets", "w" )

f.write( IFACE );

f.close()


