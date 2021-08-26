#coding: utf-8
import os

countArq = 1
countLinha = 1
estado = "Q0"
buffer = ""
linhaCoMF = 1
space = False #O que acontece se não sair do Q0
skip = False #Usado para pular linha
pre = ["algoritmo","variaveis","constantes","registro","funcao","retorno","vazio","se","senao","enquanto","para","leia","escreva","inteiro","real","booleano","char","cadeia","verdadeiro","falso"]
erros = []
siglaErro = ["SIB","SII","CMF","NMF","CaMF","CoMF","OpMF"]

# Abertura do arquivo
def input():
    global countArq
    try:
        f = open ("input/entrada%d.txt" %countArq, "r")        
    except: 
        print("Arquivo nao encontrado!")
    return f	

# Escreve uma nova linha no arquivo de saída
def output(linha, code, buffer):
    global countArq, erros, siglaErro
    try:
        os.mkdir("output")        
    except:
        print("Diretorio ja existe!")
    f = open("output/saida%d.txt" %countArq,"a")
    if(code == "ERRO"): 
        f.write("\n")
        if erros:
            for x in erros:
                f.write(x)
                f.write("\n")
        else:
            f.write("SUCESSO!")
    else:
        if(linha<10):
            linhaSaida = "0" + str(linha) + " " + code +" " + buffer
        else:
            linhaSaida = str(linha) + " " + code +" " + buffer
        flagER = False
        for x in siglaErro:
            if(x==code):
                flagER = True
        if(flagER):
            erros.append(linhaSaida)
        else:
            f.write(linhaSaida)
            f.write("\n")
    f.close()

# Verifica se é uma palavra reservada ou identificador
def PREouIDE(palavra, linha):
    global pre
    flagPRE = False
    for x in pre:
        if(x==palavra):
            flagPRE = True
    if(flagPRE):
        output(linha,"PRE",buffer)
    else:
        output(linha,"IDE",buffer)

########################################## Máquina de Estados Finitas ###########################################
def maqEstados(caractere,entrada, linha):
    global buffer, estado
    
    if(estado =="Q0"):
        estadoQ0(caractere, entrada, linha)
    elif(estado == "Q1"):
        estadoQ1(caractere, entrada, linha)
    elif(estado == "Q2"):
        estadoQ2(linha)
    elif(estado == "Q3"):
        estadoQ3(caractere, entrada, linha)
    elif(estado == "Q4"):
        estadoQ4(caractere, entrada, linha)
    elif(estado == "Q5"):
        estadoQ5(caractere, entrada, linha)
    elif(estado == "Q6"):
        estadoQ6(linha)
    elif(estado == "Q7"):
        estadoQ7(caractere, entrada, linha)
    elif(estado == "Q8"):
        estadoQ8(linha)
    elif(estado == "Q9"):
        estadoQ9(caractere, entrada, linha)
    elif(estado == "Q10"):
        estadoQ10(linha)
    elif(estado == "Q11"):
        estadoQ11(caractere, entrada, linha)
    elif(estado == "Q12"):
        estadoQ12(linha)
    elif(estado == "Q13"):
        estadoQ13(linha)
    elif(estado == "Q14"):
        estadoQ14(linha)
    elif(estado == "Q15"):
        estadoQ15(caractere, entrada, linha)
    elif(estado == "Q16"):
        estadoQ16(linha)
    elif(estado == "Q17"):
        estadoQ17(caractere, entrada,linha)
    elif(estado == "Q18"):
        estadoQ18(linha)
    elif(estado == "Q19"):
        estadoQ19()   
    elif(estado == "Q20"):
        estadoQ20(caractere, entrada, linha)   
    elif(estado == "Q21"):
        estadoQ21(caractere, entrada)  
    elif(estado == "Q22"):
        estadoQ22(caractere, entrada)  
    elif(estado == "Q23"):
        estadoQ23()  
    elif(estado == "Q27"):
        estadoQ27(caractere, entrada, linha)   
    elif(estado == "Q28"):
        estadoQ28(caractere, entrada, linha)   
    elif(estado == "Q29"):
        estadoQ29(caractere, entrada, linha)   
    elif(estado == "Q30"):
        estadoQ30(linha)  
    elif(estado == "Q32"):
        estadoQ32(caractere, entrada, linha)
    elif(estado == "Q33"):
        estadoQ33(linha)
    elif(estado == "Q34"):
        estadoQ34(caractere, entrada, linha)   
    elif(estado == "Q35"):
        estadoQ35(caractere, entrada, linha)   
    elif(estado == "Q36"):
        estadoQ36(caractere, entrada, linha)   
    elif(estado == "Q37"):
        estadoQ37(caractere, entrada, linha)   
    elif(estado == "Q38"):
        estadoQ38(linha)
    else:
        print("Bugou o estado")

############################################### Estados ######################################################
def estadoQ0(caractere,entrada, linha):
    global buffer, estado, space
    buffer=buffer+entrada
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122):
        print ("LETRA")
        estado = "Q1" 
    elif(caractere == 44 or caractere == 40 or caractere == 41 or caractere == 46 or caractere == 59 or caractere == 91 or caractere == 93 or caractere == 125):
        estado = "Q2"
    elif(caractere >= 48 and caractere <= 57):
        print("NRO")
        estado = "Q3"
    elif(caractere == 36 or caractere == 92 or caractere == 126 or caractere == 58 or caractere == 63 or caractere == 64 or caractere >=94 and caractere <= 96):
        print("SIB")
        estado = "Q6"
    elif(caractere == 124):
        print("SIB !")
        estado = "Q7"
    elif(caractere == 38):
        print("SIB &")
        estado = "Q9"
    elif (caractere >=60 and caractere <= 62 ):
        print("REL" + str(linha))
        estado = "Q11"
    elif(caractere == 47):
        print("ART barra")
        estado = "Q13"    
    elif(caractere == 42):
        print("ART *")
        estado = "Q14"
    elif(caractere == 45):
        print("ART -")
        estado = "Q15"
    elif(caractere == 43):
        print("ART +")
        estado = "Q17"    
    elif(caractere == 37):
        print("CoM Linha %")
        estado = "Q19" 
    elif(caractere == 123):
        print("DEL {")
        estado = "Q20" 
    elif(caractere == 34):
        print("Cadeia de caractere")
        estado = "Q27" 
    elif(caractere == 33):
        print ("LOG !")
        estado = "Q32"
    elif(caractere == 39):
        print ("CAR INIT")
        estado = "Q34"    
    else:
        if(caractere != 10 and caractere != 194 and caractere != 195 and caractere != 32 and caractere != 3):
            print (caractere)
            print ("SII "+ buffer)
            estado = "Q33"
        else:
            print("Travou no Q0")
            buffer=""
            space = True

def estadoQ1(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95):
        print("IDE ou PRE")
        buffer=buffer+entrada
        estado = "Q1"
    else:
        estado = "Q0"
        PREouIDE(buffer, linha)
        buffer=""

def estadoQ2(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "DEL", buffer)
    buffer=""

def estadoQ3(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        print("NRO" + buffer)
        buffer = buffer + entrada
        estado = "Q3"
    elif(caractere == 46):
        print("Float" + buffer)
        buffer = buffer + entrada
        estado = "Q4"
    else:
        estado = "Q0"
        output(linha, "NRO", buffer)
        buffer="" 

def estadoQ4(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    else:
        output(linha, "NMF", buffer)
        estado = "Q0"
        buffer = ""

def estadoQ5(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    else:
        estado = "Q0"
        output(linha,"NRO",buffer)
        buffer = ""
 
def estadoQ6(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"SIB",buffer)
    buffer=""

def estadoQ7(caractere,entrada, linha):
    global buffer, estado
    if(caractere == 124):
        print("LOG !")
        buffer=buffer+entrada
        estado = "Q8"
    else:
        estado = "Q0"
        print("OpMF |")
        output(linha,"OpMF",buffer)
        buffer=""

def estadoQ8(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"LOG",buffer)
    buffer=""

def estadoQ9(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 38):
        print ("SIB &")
        buffer = buffer+entrada
        estado = "Q10"
    else:
        estado = "Q0"
        print("OpMF &")
        output(linha,"OpMF",buffer)
        buffer=""

def estadoQ10(linha):
    global buffer, estado
    estado = "Q0"
    print("LOG &&")
    output(linha,"LOG",buffer)
    buffer=""

def estadoQ11(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=60 and caractere <= 62):
        print("REL" + str(linha))
        buffer=buffer+entrada
        estado = "Q12"
    else:
        estado = "Q0"
        output(linha,"REL",buffer)
        buffer=""

def estadoQ12(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"REL",buffer)
    buffer=""

def estadoQ13(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

def estadoQ14(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

def estadoQ15(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 45):
        print("ART -")
        buffer=buffer+entrada
        estado = "Q16"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

def estadoQ16(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

def estadoQ17(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 43):
        print("ART +")
        buffer=buffer+entrada
        estado = "Q18"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

def estadoQ18(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

def estadoQ19():
    global buffer, estado, skip
    estado = "Q0"
    buffer=""
    skip = True

def estadoQ20(caractere, entrada, linha):
    global buffer, estado, linhaCoMF
    if(caractere == 35):
        linhaCoMF = linha
        buffer=buffer+entrada
        estado = "Q21"
    else:
        estado = "Q0"
        output(linha,"DEL",buffer)
        buffer=""

def estadoQ21(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q22"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q21"
        else:
            buffer=buffer+entrada
            estado = "Q21"

def estadoQ22(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q22"
    elif(caractere == 125):
        buffer=buffer+entrada
        estado = "Q23"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q21"
        else:
            buffer=buffer+entrada
            estado = "Q21"

def estadoQ23():
    global buffer, estado
    estado = "Q0"
    buffer=""

def estadoQ27(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q30"
    elif(caractere == 92):
        buffer=buffer+entrada
        estado = "Q28"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39)):
        buffer=buffer+entrada
        estado = "Q27"
    else:
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""

def estadoQ28(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q29"
    elif(caractere == 92):
        buffer=buffer+entrada
        estado = "Q28"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39)):
        buffer=buffer+entrada
        estado = "Q27"
    else:
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""

def estadoQ29(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q30"
    elif(caractere == 92):
        buffer=buffer+entrada
        estado = "Q28"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39)):
        buffer=buffer+entrada
        estado = "Q27"
    else:
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""

def estadoQ30(linha):
    global buffer, estado
    output(linha,"CAD",buffer)
    estado = "Q0"
    buffer=""

def estadoQ32(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 61):
        print("LOG !")
        buffer=buffer+entrada
        estado = "Q12"
    else:
        estado = "Q0"
        output(linha,"LOG",buffer)
        buffer=""

def estadoQ33(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "SII", buffer)
    buffer=""

def estadoQ34(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 92):
        buffer=buffer+entrada
        estado = "Q36"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39) and not(caractere == 34)):
        buffer=buffer+entrada
        estado = "Q35"
    else:
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""

def estadoQ35(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""

def estadoQ36(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q37"
    else:
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""

def estadoQ37(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""

def estadoQ38(linha):
    global buffer, estado
    output(linha,"CAR",buffer)
    estado = "Q0"
    buffer=""

'''def estadoQ39(caractere, entrada, linha):
    global buffer, estado
    if(not(caractere == 32 or caractere == 10)):
        buffer = buffer + entrada
        estado = "Q39"
    else:
        output(linha, "NMF", buffer)
        estado = "Q0"
        buffer = "" '''

###############################################################################################################

#Verifica se a existe a pasta input
flag = True
pastas = os.listdir()
for x in pastas:
	if(x == "input"):
		flag = False
if(flag):
	print("Pasta input nao encontrada")
	


################################################# MAIN #######################################################
entrada = input()
while 1:
    linha = entrada.readline()	
    i = 0
    if linha=='':
        countLinha-=1
        maqEstados(3, " ", countLinha)
        break
    while i+1<=len(linha):
        caractere = ord(linha[i])
        maqEstados(caractere, linha[i], countLinha)
        if(not(estado=="Q0") or space):
            i+=1
            space = False
        if(skip):
            skip = False
            break
    countLinha+=1
output(0,"ERRO","")