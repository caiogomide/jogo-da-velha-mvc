from src.controller.controller import Controller

'''
    Jogo da Velha

    @version 1.0
    @author Caio Viegas de Souza Gomide 
    Este projeto utiliza conceitos de Inteligência Artificial, na aplicação
    do algorítmo Minimax, utilizando a linguagem Python, no jogo conhecido
    como Jogo da Velha. O algorítimo Minimax almeja um objetivo: realizar
    ações visando aumentar a medida de desempenho de cada posição no jogo,
    visando ganha-lo no final.

'''

if __name__ == "__main__":
    controller = Controller()
    controller.iniciar_jogo()