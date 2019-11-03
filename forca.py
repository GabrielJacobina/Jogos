def jogar():

    import random
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    lista = ["banana", "maça", "abacaxi", "melancia", "pera", "goiaba"]
    fruta = random.choice(lista)
    palavra_secreta = fruta.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                index += 1
        else:
             erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou!")
        print("A palavra secreta é: "+ palavra_secreta)
    else:
        print("Você perdeu!")
        print("A palavra secreta é: "+ palavra_secreta)
    print("Fim do jogo")

if(__name__ == "__main__"):
  jogar()