from src.model.jogadores.agente.minimax import Minimax
from src.model.jogadores.usuario.usuario import Usuario
from src.model.grade import Grade


class Model:
    def __init__(self):
        self._usuario = ''
        self._agente_inteligente = ''
        self._flags = ['usuario', 'agente_inteligente']
        self._flag_rodada = 'usuario'
        self._combinacoes_vencedoras = ''
        self._pontuacao_jogador = ''
        self._pontuacao_agente_inteligente = ''
        self._pontuacao_empate = ''
        self._quantidade_espacos_posicionados = ''
        self._sequencia_vencedora = ''
        self._jogo_terminou = ''
        self.grade = Grade()
        

    '''
    Atribui quais combinações são vencedoras para 
    cada orientação, retorna um  dicionário contendo 
    as combinações de vitórias para cada orientação
    '''

    @property
    def combinacoes_vencedoras(self):
        # Para haver um vencedor, deve haver 3 símbolos consecutivos na horizontal, diagonal ou vertical   
        
        # 3 Combinações possíveis para vencer na vertical
        combinacao_vencedora_vertical = [[(x,y) for x in range (3)] for y in range(3)]
        # 3 Combinações possíveis para vencer na horizontal
        combinacao_vencedora_horizontal = [[(x,y) for y in range (3)] for x in range(3)]
        # 2 Combinações possíveis para vencer na diagonal
        combinacao_vencedora_diagonal = [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]
        # As 8 combinações possíveis para vencer
        combinacoes_vencedoras = {
            'Vertical':combinacao_vencedora_vertical,
            'Horizontal':combinacao_vencedora_horizontal,
            'Diagonal':combinacao_vencedora_diagonal
        }
        
        return combinacoes_vencedoras

    '''
    Atributo que apresenta a sequência vencedora do jogo
    '''
    @property
    def sequencia_vencedora(self):
        return self._sequencia_vencedora


    '''
    Atribui a sequencia vencedora do jogo
    '''
    @sequencia_vencedora.setter
    def sequencia_vencedora(self,sequencia):
        self._sequencia_vencedora = sequencia
    

    '''
    Atributo que representa o término do jogo
    '''
    @property
    def jogo_terminou(self):
        print(f'self._vencedor(): {self._vencedor()}')
        print(f'self.ha_empate(): {self.ha_empate()}')
        if self._vencedor() != '' or self.ha_empate():
            return True
        return False
        
    '''
    Atributo que representa a classe do jogador usuário
    '''
    @property
    def usuario(self):
        return self._usuario

    '''
    Atribui o símbolo escolhido para o usuário
    '''
    @usuario.setter
    def usuario(self, simbolo_usuario):
        self._usuario = Usuario(simbolo_usuario)

    '''
    Atributo que representa a classe do jogador agente inteligente
    '''
    @property
    def agente_inteligente(self):
        return self._agente_inteligente

    '''
    Atribui o símbolo escolhido para o agente inteligente
    '''
    @agente_inteligente.setter
    def agente_inteligente(self, simbolo_agente_inteligente):
        self._agente_inteligente = Minimax(simbolo_agente_inteligente, self)

    
    '''
    Atributo que representa a flag de quem é a jogada atual
    do usuário ou agente inteligente
    '''
    @property
    def flag_rodada(self):
        return self._flag_rodada

    '''
    Atribui a flag de rodada
    '''
    @flag_rodada.setter
    def flag_rodada(self, flag_rodada):
        if flag_rodada in self._flags:
            self._flag_rodada = flag_rodada
        # Criar tratamento de erros
    
    '''
    Incrementa a pontuação do jogador
    '''
    def incrementa_pontuacao_jogador(self):
        self._pontuacao_jogador += 1

    '''
    Incrementa a pontuação do agente inteligente
    '''
    def incrementa_pontuacao_agente_inteligente(self):
        self._pontuacao_agente_inteligente += 1

    '''
    Incrementa a pontuação de empate
    '''
    def incrementa_pontuacao_empate(self):
        self._pontuacao_empate +=1

        
    '''
    Retorna a quantidade de espaços já ocupados
    na grade do jogo.
    '''
    def quantidade_espacos_posicionados(self):
        quantidade_espacos_posicionados = 0
        posicoes_grade = self.grade.posicoes
        for linha in posicoes_grade:
            for coluna in linha:
                if coluna == 'x' or coluna == 'o':
                    quantidade_espacos_posicionados+=1
        return quantidade_espacos_posicionados
    
    '''
    Método responsável por cálcular e retornar
    se há espaços não ocupados em uma grade 
    determinada
    '''
    def ha_espacos_vazios(self):
        posicoes_grade = self.grade.posicoes
        for linha in posicoes_grade:
            for coluna in linha:
                if coluna == []:
                    return True
        return False
    
    '''
    Méto responsável por responder se 
    uma posição já foi ocupada por um
    simbolo
    '''
    def posicao_ocupada(self, linha, coluna):
        return self.grade.posicoes[linha][coluna] == 'x' or self.grade.posicoes[linha][coluna] == 'o'

    '''
    Método responsável por checar se houve um empate
    no Jogo, dado uma grade, retorna um valor booleano
    '''
    def ha_empate(self):
        if self.ha_espacos_vazios() == False and self._vencedor() == '':
            return True
        return False
    
    '''
    Método responsável por checar se há vencedores, dado uma grade, retorna o simbolo do vencedor ou vazio
    '''
    def _vencedor(self):
        orientacoes = ['Horizontal', 'Vertical', 'Diagonal']
        # Checa se para cada orientação houve um vencedor
        for orientacao in orientacoes:
            # Checa se há vencedores na orientacao dada
            combinacoes_vencedoras_por_orientacao = self.combinacoes_vencedoras[orientacao]
            posicoes_simbolos = self.grade.posicoes
            print(f'posicoes_simbolos: {self.grade.posicoes}')
            for combinacao_vencedora_orientada in combinacoes_vencedoras_por_orientacao:
                combinacao_x = 0
                combinacao_o = 0
                # Checa se cada combinação ocorre
                for i in range(3):
                    linha, coluna = combinacao_vencedora_orientada[i]
                    # Caso um elemento de uma combinação não tenha sido preenchido, pula para próxima combinação
                    if posicoes_simbolos[linha][coluna] == '[]':
                        break
                    # Checa se o elemento na posicao dada é X ou O
                    if posicoes_simbolos[linha][coluna] == 'x':
                        combinacao_x+=1
                    if posicoes_simbolos[linha][coluna] == 'o':
                        combinacao_o+=1
                # Caso haja uma combinacao de 3 elementos na horizontal de X ou O, este é o vencedor
                if combinacao_x == 3:
                    self.sequencia_vencedora = combinacao_vencedora_orientada
                    return 'x'
                if combinacao_o == 3:
                    self.sequencia_vencedora = combinacao_vencedora_orientada
                    return 'o'
        return ''
    
    ''' 
    Método responsável por atualizar a pontuação 
    do jogo ao terminar uma partida
    '''
    def atualiza_pontuacao(self):
        if self._vencedor == self._usuario:
            self._pontuacao_jogador += 1
        elif self._vencedor == self._agente_inteligente:
            self._pontuacao_agente_inteligente += 1
        elif self.ha_empate():
            self._pontuacao_empate += 1
            
    '''
    Método Responsável por resetar o model
    '''
    def reset(self):
        self = Model()

     
        
        
       
