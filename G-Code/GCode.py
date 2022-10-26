# Script para transformar as coordenadas Z que iniciam em '0', para 'TOP', pois em algumas
# impressoras a cama inicia imprimindo do alto para baixo.
# Prusa Slicer

AlturaEixoZ = 107  # Altura em mm.



with open('outputGCode.gcode', 'a') as fileOutput:

    fileInput = open('FangLeFurieux-Original.gcode', 'r')
    Lines = fileInput.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
        #print(line)
        x = line.find('G1 Z')
        #print(x)
        if x > 1:
            y= line
            # X1 Removendo a String inicial e final para ficar apenas com o número do eixo Z
            x1 = line[6:]
            x2 = x1[:5]

            #print(x2)

            try:
                AlturaMesaAtual = float(x2)
                AlturaMesaImpressora = AlturaEixoZ - AlturaMesaAtual
                #print(AlturaMesaImpressora)
            
                #G1 Z3.05 F7800
                newline = '  G1 Z' + str(AlturaMesaImpressora) + ' F7800\n'
                #print(newline)
                fileOutput.write(newline)

            except ValueError:
                #print("nao é numero")
                fileOutput.write(line)
        else:
            fileOutput.write(line)

print("FINISHED OK!")
        
