# Script para inserir dois espaços no inicio do arquivo de cada linha

with open('outputReadyPrint.gcode', 'a') as fileOutput:

    fileInput = open('outputPlus2SpacesChanged.gcode', 'r')
    Lines = fileInput.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        newline =line.lstrip('  ')
        fileOutput.write(newline)

print("FINISHED OK!")
        
