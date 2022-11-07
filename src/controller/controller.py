from src.model.model import Model
from src.view.view import View


class Controller:

    def __init__(self):
        self._model = Model()
        self._view = View(self)
    

    '''
    Método responsável por inicializar o jogo
    na tela de boas vindas
    '''
    def iniciar_jogo(self):
        # Inicializa a tela do jogo 
        self._view.muda_tela(self._view.tela_inicial)
        self._view.mainloop()
   
    '''
    Método responsável por selecionar os simbolos de usuário
    e agente inteligente
    '''
    def seleciona_simbolo(self, usuario, agente_inteligente):
        # Instancia a classe de cada jogador
        self._model.usuario = usuario
        self._model.agente_inteligente = agente_inteligente
        # Informa a classe de cada jogador para a view
        self._view.usuario = self._model.usuario
        self._view.agente_inteligente = self._model.agente_inteligente

    '''
    Método ativado ao usuário realizar uma jogada
    '''
    def jogada_usuario(self, posicao_clicada, linha, coluna):
        # Encontra se a posição não esta ocupada por outro simbolo
        posicao_nao_ocupada = self._model.posicao_ocupada(linha, coluna) == False

        # Só realiza jogada caso a posição não esteja ocupada
        if posicao_nao_ocupada:
            # Posiciona o simbolo escolhido na view
            self._view.atualiza_imagem_posicao(posicao_clicada, self._model.usuario.simbolo)  
            # Atualiza a rodada
            self._model.flag_rodada = 'agente_inteligente'
            # Atualiza a grade do jogo
            self._model.grade.atualiza_grade(linha, coluna, self._model.usuario.simbolo)
            # A jogada do usuário ativa, em um pipeline, a jogada do Agente Inteligente
            self.jogada_agente_inteligente()
            # Analisa caso de o jogo ter terminado
            print(f'self._model.jogo_terminou:{self._model.jogo_terminou}')
            if self._model.jogo_terminou:
                self.reset()


    '''
    Método ativado ao agente inteligente realizar uma jogada
    '''
    def jogada_agente_inteligente(self):
        # Atualização do model
        linha, coluna = self._model.agente_inteligente.posicionar_simbolo(self._model.grade)
        # Selecionando posição clicada pelo agente_inteligente
        posicao_clicada = [posicao for posicao, coordenada in self._view.posicoes.items() if coordenada==(linha,coluna)][0]
        # Posiciona o simbolo escolhido na view
        self._view.atualiza_imagem_posicao(posicao_clicada, self._model.agente_inteligente.simbolo)
        # Atualiza a rodada
        self._model.flag_rodada = 'usuario'
        # Atualiza a grade do jogo
        self._model.grade.atualiza_grade(linha, coluna, self._model.agente_inteligente.simbolo)
        # Analisa caso de o jogo ter terminado
        if self._model.jogo_terminou:
            self.reset()

    '''
    Método responsável por definir uma flag de status
    para o jogo terminado
    '''
    def _flag_status(self):
        if self._model.jogo_terminou:
            # Analisa caso em que o agente inteligente ganhou
            if self._model._vencedor() == self._model.agente_inteligente.simbolo:
                return 'agente_ganhou'
            # Analisa caso em que o usuário ganhou
            elif self._model._vencedor() == self._model.usuario.simbolo:
                return 'usuario_ganhou'
            # Analisa caso de empate
            elif self._model.ha_empate():
                return 'empate'
        return ''

    '''
    Método responsável por atualizar a pontuação
    após o término do jogo
    '''
    def _atualiza_pontuacao(self):

        # Coleta a flag de status
        flag_status = self._flag_status

        # Pontuação de empate
        if flag_status == 'empate':
            self._model.incrementa_pontuacao_empate()
        
        # Pontuação de usuário
        elif flag_status == 'usuario_ganhou':
            self._model.incrementa_pontuacao_jogador()

        
        # Pontuação de agente inteligente
        elif flag_status == 'agente_ganhou':
            self._model.incrementa_pontuacao_agente_inteligente()



    '''
    Método responsável por resetar o controller do jogo
    para o estado inicial, não retorna valores
    '''
    def reset(self):

        # Coleta a flag de status
        flag_status = self._flag_status()
        # Coleta a sequencia vencedora
        sequencia_vencedora = self._model.sequencia_vencedora
        # Atualiza a pontuação do jogo
        self._atualiza_pontuacao()
        # Reseta a view e o model
        self._model.reset()
        self._view.reset(flag_status, sequencia_vencedora)
