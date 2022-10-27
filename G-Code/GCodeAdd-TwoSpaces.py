# Script para inserir dois espaços no inicio do arquivo de cada linha

with open('outputPlus2Spaces.gcode', 'a') as fileOutput:

    fileInput = open('motog60_v3.gcode', 'r')
    Lines = fileInput.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        newline = '  ' + line
        fileOutput.write(newline)

print("FINISHED OK!")
        
