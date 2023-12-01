

mur0 : mur0.c winsuport.o winsuport.h
	gcc -Wall mur0.c winsuport.o -o mur0 -lcurses


mur1 : mur1.c winsuport.o winsuport.h
	gcc -Wall mur1.c winsuport.o -o mur1 -lcurses -lpthread


mur2 : mur2.c winsuport.o winsuport.h
	gcc -Wall mur2.c winsuport.o -o mur2 -lcurses -lpthread

mur3 : mur3.c winsuport2.o memoria.o pilota3
	gcc -Wall mur3.c winsuport2.o memoria.o -o mur3 -lcurses -lpthread 

pilota3 : pilota3.c winsuport2.o memoria.o
	gcc -Wall pilota3.c winsuport2.o  memoria.o -o pilota3 -lcurses

winsuport.o : winsuport.c winsuport.h
	gcc -Wall -c winsuport.c -o winsuport.o

clean : 
	rm -f winsuport.o mur0 mur1 mur2

