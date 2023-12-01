
#! /usr/bin/env python3

import getopt
import sys
import os

#INICIALITZAR VARIABLES 

existFila=0
existColumna=0
existPorteria=0
existPosPaleta=0
existMidaPaleta=0
existPosPilota=0

fila=-99
columna=-99
porteria=-99
posPaleta='-99,-99'
midaPaleta=-99
pilota='-99,-99,-99,-99'

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'n:f:c:p:0:m:1:')

for opt, arg in options:
    if opt in ('-n'):
        nomfitxer = arg
    elif opt in ('-f'):
        fila = arg
        existFila=1
    elif opt in ('-c'):
        columna = arg
        existColumna=1
    elif opt in ('-p'):
        porteria = arg
        existPorteria=1
    elif opt in ('-0'):
        posPaleta = arg
        posPal = posPaleta.replace(","," ")
        existPosPaleta=1
    elif opt in ('-m'):
        midaPaleta = arg
        existMidaPaleta=1
    elif opt in ('-1'):
        pilota = arg
        pil = pilota.replace(","," ")
        existPosPilota=1

#COMPROVAR SI EXISTEIX EL FITXER
existFitxer=(os.path.isfile(nomfitxer))

#SI EL FITXER EXISTEIX
if (existFitxer == True):
    fit=open(nomfitxer, 'r')
    filaFitxer=0
    for linia in fit:
        columnaFitxer = linia.split(" ")

#SEPARAR LES DADES I INTRODUIR-LES EN VARIABLES
        if filaFitxer == 0 and int(fila) == -99:
            newFila = columnaFitxer[0]
            limitNewFila=0
        elif filaFitxer == 0 and int(fila) != -99:
            if (int(fila) < 10) or (int(fila) > 120):
                print("El numero de les files ha de ser entre 10 i 120")
                limitNewFila=0
            else:
                newFila = fila
                limitNewFila=1

        if filaFitxer == 0 and int(columna) == -99:
            newColumna = columnaFitxer[1]
            limitNewColumna=0
        elif filaFitxer == 0 and int(columna) != -99:
            if (int(columna) < 10) or (int(columna) > 36):
                print("El numero de les columnes ha de ser entre 10 i 36")
                limitNewColumna=0
            else:
                newColumna = columna
                limitNewColumna=1

        if filaFitxer == 0 and int(porteria) == -99:
            newPorteria = columnaFitxer[2].rstrip()
            limitNewPorteria=0
        elif filaFitxer == 0 and int(porteria) != -99:
            newNumFila = int(newFila)-1
            if (int(porteria) < 8) or (int(porteria) > newNumFila):
                limitNewPorteria=0
                print("El numero de la mida de la porteria ha de ser entre 8 i",newNumFila)
            else:
                newPorteria = porteria
                limitNewPorteria=1

        if filaFitxer == 1 and posPaleta == '-99,-99':
            newFilaPaleta = columnaFitxer[0]
            newColumnaPaleta = columnaFitxer[1]
            limitNewPosPalFila=0
            limitNewPosPalColumna=0
        elif filaFitxer == 1 and posPaleta != '-99,-99':
            posicioPaleta=posPal.split(" ")
            if (int(posicioPaleta[0]) < 2) or (int(posicioPaleta[0]) > 118):
                print("El numero de la fila de la paleta ha de ser entre 2 i 118")
                limitNewPosPalFila=0
            else:
                newFilaPaleta = posicioPaleta[0]
                limitNewPosPalFila=1
            if (int(posicioPaleta[1]) < 2) or (int(posicioPaleta[1]) > 35):
                print("El numero de la columna de la paleta ha de ser entre 2 i 35")
                limitNewPosPalColumna=0
            else:
                newColumnaPaleta = posicioPaleta[1]
                limitNewPosPalColumna=1

        if filaFitxer == 1 and int(midaPaleta) == -99:
            newMidaPaleta = columnaFitxer[2].rstrip()
            limitNewMidaPaleta=0
        elif filaFitxer == 1 and int(midaPaleta) != -99:
            newNumFila = int(newFila)-1
            if (int(midaPaleta) < 3) or (int(midaPaleta) > newNumFila):
                print("El numero de la mida de la paleta ha de ser entre 3 i",newNumFila)
                limitNewMidaPaleta=0
            else:
                newMidaPaleta = midaPaleta
                limitNewMidaPaleta=1   
      
        if filaFitxer == 2 and pilota == '-99,-99,-99,-99':
            newFilaPosPilota = columnaFitxer[0]
            newColumnaPosPilota = columnaFitxer[1]    
            newFilaVelPilota = columnaFitxer[2]
            newColumnaVelPilota = columnaFitxer[3]
            limitNewPosPilFila=0
            limitNewPosPilColumna=0
            limitNewVelPilFila=0
            limitNewVelPilColumna=0
        elif filaFitxer == 2 and pilota != '-99,-99,-99,-99':
            PosVelPilota=pil.split(" ")
            if (int(PosVelPilota[0]) < 2) or (int(PosVelPilota[0]) > 118):
                print("El numero de la fila de la pilota ha de ser entre 2 i 118")
                limitNewPosPilFila=0
            else:
                newFilaPosPilota = PosVelPilota[0]
                limitNewPosPilFila=1
            if (int(PosVelPilota[1]) < 2) or (int(PosVelPilota[1]) > 35):
                print("El numero de la columna de la pilota ha de ser entre 2 i 35")
                limitNewPosPilColumna=0
            else:
                newColumnaPosPilota = PosVelPilota[1]   
                limitNewPosPilColumna=1
            if (float(PosVelPilota[2]) < -1.0) or (float(PosVelPilota[2]) > 1.0):
                print("El numero de la velocitat fila de la pilota ha de ser entre -1.0 i 1.0")
                limitNewVelPilFila=0
            else:
                newFilaVelPilota = PosVelPilota[2]
                limitVelPilFila=1
            if (float(PosVelPilota[3]) < -1.0) or (float(PosVelPilota[3]) > 1.0):
                print("El numero de la velocitat columna de la pilota ha de ser entre -1.0 i 1.0")
                limitNewVelPilColumna=0
            else:
                newColumnaVelPilota = PosVelPilota[3]
                limitNewVelPilColumna=1

        filaFitxer=filaFitxer+1
    fit.close()

#INTRODUIR LES DADES AL FITXER
    fitxer=open(nomfitxer, 'w')
    fitxer.write(str(newFila)+' '+str(newColumna)+' '+str(newPorteria)+'\n'+str(newFilaPaleta)+' '+str(newColumnaPaleta)+' '+str(midaPaleta)+'\n'+str(newFilaPosPilota)+' '+str(newColumnaPosPilota)+' '+str(newFilaVelPilota)+' '+str(newColumnaVelPilota))
    fitxer.close()

#LLEGIR EL FITXER
    f=open(nomfitxer, 'r')
    for linea in f:
        print(linea.rstrip())
    f.close()    

#SI NO EXISTEIX
else:
    if (existFila == 0):
        fila=int(input("Has d'introduïr un valor per a -f: "))
    if (existColumna == 0):
        columna=int(input("Has d'introduïr un valor per a -c: "))
    if (existPorteria == 0):
        porteria=int(input("Has d'introduïr un valor per a -p: "))
    if (existPosPaleta == 0):
        posPaleta=input("Has d'introduïr un valor per a -0: ")
        posPal = posPaleta.replace(","," ")
    if (existMidaPaleta == 0):
        midaPaleta=int(input("Has d'introduïr un valor per a -m: "))
    if (existPosPilota == 0):
        pilota=input("Has d'introduïr un valor per a -1: ")
        pil = pilota.replace(","," ")

#SEPARAR LES DADES AMB 2 O MES NUMEROS
    numFila=int(fila)-1
    posicioPaleta=posPal.split(" ")
    posPalFila=posicioPaleta[0]
    posPalColumna=posicioPaleta[1]
    Pilota=pil.split(" ")
    posPilFila=Pilota[0]
    posPilColumna=Pilota[1]
    velPilFila=Pilota[2]
    velPilColumna=Pilota[3] 

#COMPROVAR ELS LIMITS
    if (int(fila) < 10) or (int(fila) > 120):
        #FILA INCORRECTA
        limitFila=0
    else:
        #FILA CORRECTA
        limitFila=1

    if (int(columna) < 10) or (int(columna) > 120):
        #COLUMNA INCORRECTA
        limitColumna=0
    else:
        #COLUMNA CORRECTA
        limitColumna=1

    if (int(porteria) < 8) or (int(porteria) > numFila):
        #PORTERIA INCORRECTA
        limitPorteria=0
    else:
        #PORTERIA CORRECTA
        limitPorteria=1

    if (int(posPalFila) < 2) or (int(posPalFila) > 118):
        #FILA PALETA INCORRECTA
        limitFilaPaleta=0
    else:
        #FILA PALETA CORRECTA
        limitFilaPaleta=1

    if (int(posPalColumna) < 2) or (int(posPalColumna) > 35):
        #COLUMNA PALETA INCORRECTA
        limitColumnaPaleta=0
    else:
        #COLUMNA PALETA CORRECTA
        limitColumnaPaleta=1

    if (int(midaPaleta) < 3) or (int(midaPaleta) > numFila):
        #MIDA PALETA INCORRECTA
        limitMidaPaleta=0
    else:
        #MIDA PALETA CORRECTA
        limitMidaPaleta=1

    if (int(posPilFila) < 2) or (int(posPilFila) > 118):
        #POSICIO FILA PILOTA INCORRECTA
        limitPosicioPilotaFila=0
    else:
        #POSICIO FILA PILOTA CORRECTA
        limitPosicioPilotaFila=1

    if (int(posPilColumna) < 2) or (int(posPilColumna) > 35):
        #POSICIO COLUMNA PILOTA INCORRECTA
        limitPosicioPilotaColumna=0
    else:
        #POSICIO COLUMNA PILOTA CORRECTA
        limitPosicioPilotaColumna=1

    if (float(velPilFila) < -1.0) or (float(velPilFila) > 1.0):
        #VELOCITAT FILA PILOTA INCORRECTA
        limitVelocitatPilotaFila=0
    else:
        #VELOCITAT FILA PILOTA CORRECTA
        limitVelocitatPilotaFila=1

    if (float(velPilColumna) < -1.0) or (float(velPilColumna) > 1.0):
        #VELOCITAT COLUMNA PILOTA INCORRECTA
        limitVelocitatPilotaColumna=0
    else:
        #VELOCITAT COLUMNA PILOTA CORRECTA
        limitVelocitatPilotaColumna=1

#MISSATGE DE FORA DEL LIMIT
    if (limitFila != 1 or limitColumna != 1 or limitPorteria != 1 or limitFilaPaleta != 1 or limitColumnaPaleta != 1 or limitMidaPaleta != 1 or limitPosicioPilotaFila != 1 or limitPosicioPilotaColumna != 1 or limitVelocitatPilotaFila != 1 or limitVelocitatPilotaColumna != 1):
        nFit=0
        if (limitFila == 0):
            print("El numero de les files ha de ser entre 10 i 120")
        else:
            if (limitPorteria == 0):
                print("El numero de la mida de la porteria ha de ser entre 8 i",numFila)
            if (limitMidaPaleta == 0):
                print("El numero de la mida de la paleta ha de ser entre 3 i",numFila)
        if (limitColumna == 0):
            print("El numero de les columnes ha de ser entre 10 i 120")
        if (limitFilaPaleta == 0):
            print("El numero de la fila de la paleta ha de ser entre 2 i 118")
        if (limitColumnaPaleta == 0):
            print("El numero de la columna de la paleta ha de ser entre 2 i 35")
        if (limitPosicioPilotaFila == 0):
            print("El numero de la fila de la pilota ha de ser entre 2 i 118")
        if (limitPosicioPilotaColumna == 0):
            print("El numero de la columna de la pilota ha de ser entre 2 i 35")
        if (limitVelocitatPilotaFila == 0):
            print("El numero de la velocitat fila de la pilota ha de ser entre -1.0 i 1.0")
        if (limitVelocitatPilotaColumna == 0):
            print("El numero de la velocitat columna de la pilota ha de ser entre -1.0 i 1.0")

#INTRODUIR LES DADES AL FITXER
    else:
        nFit=1
        from io import open
        f=open(nomfitxer, 'w')
        f.write(str(fila)+' '+str(columna)+' '+str(porteria)+'\n'+str(posPal)+' '+str(midaPaleta)+'\n'+str(pil))
        for x in remainder:
            f.write("\n"+str(x.replace(","," ")))
        f.close

#LIMIT DE PILOTES(MAX 9)
    if (nFit == 1):
        f=open(nomfitxer, 'r')
        n=0
        for linea in f:
            n+=1
        f.close

        if (n > 11):
            print("El nombre maxim de pilotes es 9")
            os.remove(nomfitxer)
        else:
            f=open(nomfitxer, 'r')
            for linea in f:
                print(linea.rstrip())   
            f.close    



