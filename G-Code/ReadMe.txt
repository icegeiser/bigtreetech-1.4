Para colocar um arquivo G-Code para imprimir.

1 - Substituir no GCODE gerado pelo PRUSASLICER

DE: G1 Z.
POR: G1 Z0.

2 - Após isso, adicionar dois espaços em branco em cada linha;
Script python: GCodeAdd-TwoSpaces.py

3 - Alterar a altura inicial do desenho:
Script python: GCode.py

4 - Remover os dois espaços em branco gerados no passo 2.
Script python: GCodeRemove-TwoSpaces.py

5 - Passar o arquivo de saída para a impressora.
outputReadyPrint.gcode


========================
Tutorial para Cura:
========================
1 - Executar o script:

 python .\GCode-Cura.py <Arquivo de entrada.gcode> <Arquivo de saida>

 O Arquivo de entrada é gerado no Cura.
 Arquivo de saida tera a extensão '.gcode' adicionada.