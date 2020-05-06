# -*- coding: utf-8 -*-
# Python3
# Jogo da forca
# Author: Arno Junio
import random
board = ['''

>>>>>>>>>>Forca<<<<<<<<<<

    +---+
    |   |
    |
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''

     +---+
     |   |
     |   O
     |  /|
     |
     |
=========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |
     |
=========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |  /
     |
=========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |  / \\
     |
=========''']


class Game:
    def __init__(self, palavra):
        self.palavra = list(palavra)
        self.erros = 0
        self.acertos = 0
        self.palavraOculta = list(map(lambda x: x.replace(x, '_'), palavra))
        imprimeForca(self.erros)
        self.mostrarPalavra()

    def adivinhar(self, letra):
        for i in range(len(self.palavra)):
            if letra == self.palavra[i]:
                self.palavraOculta[i] = letra
                self.acertos += 1
        if letra not in self.palavra:
            self.erros += 1

    def mostrarPalavra(self):
        for i in self.palavraOculta:
            print(i, end='')
        print('')

    def jogoAcabou(self):
        if self.erros == (len(board) - 1) or self.acertos == len(self.palavra):
            return True
        else:
            return False


def imprimeForca(erros):
    print(board[erros])


def main():
    lista = [];letra = ''
    with open("palavras.txt", "r", newline="\r\n", encoding="utf8") as arquivo:
        leitor = arquivo.read()
        for i in leitor.split("\r\n"):
            lista.append(i)
    palavraEscolhida = random.choice(lista)
    jogo = Game(palavraEscolhida)
    while not jogo.jogoAcabou():
        letra = input('Informe uma letra: ')
        jogo.adivinhar(letra)
        imprimeForca(jogo.erros)
        jogo.mostrarPalavra()

    if jogo.acertos == len(jogo.palavra):
        print(palavraEscolhida)
        print("Parabéns, você venceu o jogo!")
    else:
        print("Que pena, você perdeu! Tente novamente!")
        print("Palavra revelada: ",palavraEscolhida)


if __name__ == '__main__':
    main()
