def imprime_tabuleiro(t):
    print(chr(27) + "[2J" + "\n        |     |      \n     "+t[0][0]+"  |  "+t[0][1]+"  | "+t[0][2] +" \n   _____|_____|_____ \n        |     |      \n     "+t[1][0] +"  |  "+t[1][1] +"  |  "+t[1][2] +"   \n   _____|_____|_____ \n        |     |      \n     "+t[2][0] +"  |  "+t[2][1] +"  |  "+t[2][2] +"   \n        |     |      ")

def reseta_tabuleiro():
    t = [["a","b","c"],["d","e","f"],["g","h","i"]]
    return t

def preenche_tabuleiro(t,vez):
    erro="erro"
    while (erro=="erro"):
        casa = input ("Agora é a vez do "+vez+"! \nDigite a letra da casa que você quer colocar a peça: ")

        if casa=="a":
            if t[0][0]=="a":
                t[0][0]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
    
        if casa=="b":
            if t[0][1]=="b":
                t[0][1]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="c":
            if t[0][2]=="c":
                t[0][2]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="d":
            if t[1][0]=="d":
                t[1][0]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="e":
            if t[1][1]=="e":
                t[1][1]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="f":
            if t[1][2]=="f":
                t[1][2]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="g":
            if t[2][0]=="g":
                t[2][0]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="h":
            if t[2][1]=="h":
                t[2][1]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
        if casa=="i":
            if t[2][2]=="i":
                t[2][2]=vez
                erro="ok"
            else: 
                print("Presta atenção e marca direito bosta ;( \n")
                erro = "erro"
    return t
        

def alterna_vez(vez):
    if (vez=="x"):
        vez="o"
    else:
        vez="x"
    return vez

def verifica_se_ganhou():
    print("")

def verifica_se_deu_velha():
    print("")

def termina_jogo():
    print("") 

def main():
    t=reseta_tabuleiro()
    resultado=" "
    vez="o"
    while (resultado==" "):
        vez=alterna_vez(vez)
        imprime_tabuleiro(t)
        preenche_tabuleiro(t,vez)
    termina_jogo()
        
        

main()