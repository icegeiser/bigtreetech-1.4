# Script para transformar as coordenadas Z que iniciam em '0', para 'TOP', pois em algumas
# impressoras a cama inicia imprimindo do alto para baixo.
# Cura Slicer

# Primeiro argumento, arquivo de entrada
# Segundo argumento, arquivo de saída

import re
import sys

print('cmd entry:', sys.argv)

InputFileName = sys.argv[1];
OutputFileName = sys.argv[2]+'.gcode';

print(InputFileName)
print(OutputFileName)

AlturaEixoZ = 116.6  # Altura em mm da mesa calibrada.

with open(OutputFileName, 'a') as fileOutput:

    fileInput = open(InputFileName, 'r')
    Lines = fileInput.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        #print("Line{}: {}".format(count, line.strip()))
        #print(line)
        x = re.search("Z...", line)
        x2 = line[-6:]
        #print(x)
        if x == None:
            #fileOutput.write(line)  # Do nothing
            #print(x2)
            #print(len(x2))
            if len(x2) > 4:
                if x2[3] == 'Z':
                    #print("Primeira")
                    #print(x2[4:])
                    x3 = x2[4:]
                    AlturaMesaAtual=float(x3)
                    #print(AlturaMesaAtual)
                    AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                    #print(AlturaMesaImpressora)
                    #print(line[:-3])
                    newline = line[:-3] + 'Z' + str(AlturaMesaImpressora) + '\n'
                    #print(newline)
                    fileOutput.write(newline)
                elif x2[2] == 'Z':    
                    #print("Segunda")
                    #print(x2[3:])
                    x3 = x2[3:]
                    AlturaMesaAtual=float(x3)
                    #print(AlturaMesaAtual)
                    AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                    #print(AlturaMesaImpressora)
                    #print(line[:-4])
                    newline = line[:-4] + 'Z' + str(AlturaMesaImpressora) + '\n'
                    #print(newline)
                    fileOutput.write(newline)
                else:
                    fileOutput.write(line)  # Do nothing
            else:
                fileOutput.write(line)  # Do nothing
            #print("lastChar")
        else: # Found at final string.
            # Teste if is in format ZXX.Y
            #print(line)
            #print(x2)
            if x2[0] == 'Z':
                #print("Primeira letra Z")
                if x2[1] == ':':
                    fileOutput.write(line) # Do nothing
                else:
                    #print("É Z")
                    #print(x2[1:])

                    if type(x2[1:]) == int or float:
                        x3 = x2[1:]
                        #print(x3)
                        AlturaMesaAtual=float(x3)
                        #print('The variable a number')
                        AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                        #print(AlturaMesaImpressora)
                        #print(AlturaMesaImpressora)
                        #print(line[:-6])
                        newline = line[:-6] + 'Z' + str(AlturaMesaImpressora) + '\n'
                        #print(newline)
                        fileOutput.write(newline)
                    else:
                        fileOutput.write(line)
                        print('The variable is not a number')
            elif x2[0] == ' ':
                #print(x2[1])
                if x2[1] == 'Z':
                    if type(x2[2:]) == int or float:
                        #print("Em branco1")
                        x3 = x2[2:]
                        AlturaMesaAtual=float(x3)
                        #print('The variable a number')
                        AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                        #print(AlturaMesaImpressora)
                        #print(line[:-5])
                        newline = line[:-5] + 'Z' + str(AlturaMesaImpressora) + '\n'
                        #print(newline)
                        fileOutput.write(newline)
            else:
                if x2[0] == ':':
                    #Do nothing is a invalid measure
                    fileOutput.write(line)
                else:
                    #print(x2)
                    #print(len(x2))
                    if type(x2) == int or float:
                        AlturaMesaAtual=float(x2)
                        ##print('The variable a number')
                        AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                        #print(AlturaMesaImpressora)
                        #print(line)
                        #print(line[:-len(x2)]) #Removing the last number Z (que seria o x2)
                        newline = line[:-len(x2)] + str(AlturaMesaImpressora) + '\n'
                        #print(newline)
                        fileOutput.write(newline)
       
print("FINISHED OK!")
        
