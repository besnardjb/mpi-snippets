MPI Snippets
============

This repository contains vim snippets for MPI and their meta-description. 
These definitions are to be used with a VIM snippet implementations such as
[ultisnips](github.com/SirVer/ultisnips) or through a bundle such as 
[vim-snippets](https://github.com/honza/vim-snippets).

Install
-------

Considering that you use [UltiSnips](https://github.com/SirVer/ultisnips.git).
Then add the following to your ~/.vimrc to load the project with Vundle plugin:

```vi
Plugin 'besnardjb/mpi-snippets'
```

Use
---

Once installed you may try to type MPI_Send and then use your completion key
(most of the time TAB) to trigger the Snippet. MPI snippers are done
such as all parametters are successively highlighted to be replaced, acting
as both a snipped and a cheatcheat of what is where.

The following nonMPI-function-ish snipets are defined:

CW -> MPI_COMM_WORLD
CS -> MPI_COMM_SELF

mpimain -> A main with INIT and FINALIZE


Demo
----

See a small demo here : https://www.youtube.com/watch?v=oo4NmVQ69Qk

Licence
-------

This code is CeCILL-C a fully LGPL compatible licence.
