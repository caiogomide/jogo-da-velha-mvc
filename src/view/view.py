from time import sleep
import tkinter as tk
from tkinter import font
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label
import src.constants as constants


class View (tk.Tk):

    def __init__(self, controller):
        

        # Inicializa o padrão Tkinter da tela
        super().__init__()

        # Define a Instância de controller usada
        self._controller = controller
        # Inicializa a tela de boas vindas
        self._tela_atual =  None  
        # Inicializa as posições do jogo
        self._posicoes = {}
        # Cria as telas disponíveis do jogo
        self.tela_inicial = self.cria_tela_inicial()
        self.tela_de_jogo = self.cria_tela_de_jogo(0,0,0)
        # Define o titulo do jogo
        self.title("Jogo da Velha")
        # Define o usuário da partida
        self.usuario = ''
        # Define o agente inteligente da partida
        self.agente_inteligente = ''
       

    '''
    Função Auxiliar 
    ---------------
    Cria o placar do jogo
    '''
    def _cria_placar(self, pontuacao_usuario, pontuacao_agente_inteligente, contador_empates):
        
       # Cria o placar do jogo
        self.placar = tk.Label(
            bg = "#F5F5F5",
            master=self.placeholder_tela_de_jogo,
            text=  f"| Usuário: {pontuacao_usuario} | \n |  Computador: {pontuacao_agente_inteligente} | \n | Empates: {contador_empates} |",
            padx=100
        )
        
        # Posiciona o placar do jogo ao lado direito da grade do jogo
        self.placar.grid(row=1,column=5)
    
    '''
    Função Auxiliar
    ---------------
    Cria a label de status de jogo
    Mostra se usuário ganhou, perdeu
    ou se ocorreu empate
    '''
    def _cria_status(self):
        # Cria a label responsável por demonstrar se o usuário ganhou, perdeu ou empatou
        self.status = tk.Label(
            bg = "#F5F5F5",
            master = self.placeholder_tela_de_jogo,
            text = "",
            font=font.Font(size=12, weight="bold"),
            pady=50
        )
        # Posiciona o status no jogo
        self.status.grid(row=8,column=1)
    '''
    Função Auxiliar
    ---------------
    Cria e personaliza cada célula do tabuleiro
    '''
    def _cria_celula(self):
        # Personaliza cada célula da grade onde ocorre o jogo
        celula = tk.Button(
            bg = "#F5F5F5",
            master=self.placeholder_tela_de_jogo,
            image = PhotoImage(file = f'{constants.BACKGROUND_COR}'),
            font=font.Font(size=48, weight="bold"),
            fg="black",
            width=150,
            height=150,
            highlightbackground="#121212",
            highlightthickness = 3
        )
        return celula
    
    ''' 
    Função Auxiliar
    ---------------
    Posiciona cada celula na 
    sua respectiva linha e
    coluna
    '''
    def _posiciona_celula(self, celula, linha, coluna):
         celula.grid(
                    row=linha,
                    column=coluna,
                    padx=0,
                    pady=0,
                    sticky="nsew"
                )
    '''
    Função Auxiliar
    ---------------
    Configura a grade, as linhas e as colunas
    '''
    def _configura_grade(self, linha):
        self.rowconfigure(linha, weight=2, minsize=100)
        self.columnconfigure(linha, weight=2, minsize=125)
        
    '''
    Função Auxiliar
    ---------------
    Cria o tabuleiro do jogo
    '''
    def _cria_tabuleiro(self):
        
        for linha in range(3):
            
            # Configura a grade, as linhas e as colunas
            self._configura_grade(linha)
            # Cria cada célula da grade onde ocorre o jogo
            for coluna in range(3):
                
                celula = self._cria_celula()
                
                # Adiciona ao dicionário de posições um elemento
                # Cujo a Key é o botão e o Value a posição do elemento
                self.posicoes[celula] = (linha, coluna)
         
                # Cria um listener binding ao elemento, o qual ativa
                # A função dada ao ser pressionado
                celula.bind("<ButtonPress-1>", self.clique_posicao)
                
                # Posiciona cada célula da grade no seu respectivo lugar
                self._posiciona_celula(celula, linha, coluna)
            
    '''
    Método que cria tela de jogo
    a qual inclui a grade do jogo
    '''
   
    def cria_tela_de_jogo(self, pontuacao_usuario, pontuacao_agente_inteligente, contador_empates):

        # Cria o placholder da tela de jogo
        self.placeholder_tela_de_jogo = tk.Frame(master=self, bg="#F5F5F5",pady=100,padx=200)
        # Cria a grade inicial do jogo
        self.posicoes = {}

        self._cria_placar(pontuacao_usuario, pontuacao_agente_inteligente, contador_empates)
        self._cria_status()
        self._cria_tabuleiro()
        
        return self.placeholder_tela_de_jogo
    
    '''
    Método responsável por realizar a mudança 
    da tela mostrada ao usuário, recebe esta
    tela, do tipo Frame
    '''
    def muda_tela(self, tela, msg=''):
        # Define a nova tela, como a tela recebida como parâmetro
        nova_tela = tela
        # Apaga a tela caso não seja nula
        if self._tela_atual is not None:
            self._tela_atual.destroy()
        # Cria a nova tela dada e faz o packing dela
        self._tela_atual = nova_tela
        self._tela_atual.pack(fill=tk.X,expand=10000)
        # Define os simbolos caso tenham sido selecionados
        if msg=='o':
            self._controller.seleciona_simbolo('o','x')
        elif msg=='x':
            self._controller.seleciona_simbolo('x','o')

    '''
    Função Auxiliar
    ---------------
    Cria o texto inicial
    de boas vindas
    '''
    def _cria_texto_inicial(self, placeholder_tela_inicial):
        texto_inicial = Label(
            master=placeholder_tela_inicial,
            text="BEM VINDO AO JOGO DA VELHA! \n \n ESCOLHA O SÍMBOLO \"X\" ou \"O\" PARA JOGAR",
            pady = 100,
            bg="#F5F5F5",
            fg = "#121212",
            font=font.Font(size=12, weight="bold"),
        )
        texto_inicial.pack()
        
    '''
    Função Auxiliar
    ---------------
    Cria o botão X
    '''
    def _cria_botao_x(self, placeholder_tela_inicial):
      icone_x = PhotoImage(file = r"{}".format(constants.ICONE_X)) 
      botao_x = Button(placeholder_tela_inicial, text = "X", image = icone_x, bg = "#F5F5F5", borderwidth=0, command=lambda: self.muda_tela(self.tela_de_jogo,'x'))
      botao_x.image = icone_x
      botao_x.pack()
    
    '''
    Função Auxiliar
    ---------------
    Cria o botão O
    '''
    def _cria_botao_o(self, placeholder_tela_inicial):
      icone_o = PhotoImage(file = r"{}".format(constants.ICONE_O)) 
      botao_o = Button(placeholder_tela_inicial, text = "O", image = icone_o, bg = "#F5F5F5", borderwidth=0, command=lambda: self.muda_tela(self.tela_de_jogo,'o'))
      botao_o.image = icone_o
      botao_o.pack(pady=100)

    '''
    Método que cria tela inicial
    possui boas vindas ao usuário
    '''
    
    def cria_tela_inicial(self):
      
      # Cria o placeholder da tela inicial do jogo 
      placeholder_tela_inicial = tk.Frame(master=self, bg="#F5F5F5",pady=20)
      # Cria o texto de iniciação do jogo
      self._cria_texto_inicial(placeholder_tela_inicial)
      # Cria um botão para tela inicial representando o ícone X
      self._cria_botao_x(placeholder_tela_inicial)
      # Cria um botão para tela inicial representando o ícone O
      self._cria_botao_o(placeholder_tela_inicial)

      # Aplicando todas modificações a tela inicial
      tela_inicial = placeholder_tela_inicial

      return tela_inicial
 
   
    '''
    Método responsável por atualizar a imagem de uma célula
    com o símbolo X ou O, não retorna valores
    '''
    def atualiza_imagem_posicao(self, posicao_clicada, simbolo):
        # Acessa a imagem respectiva ao símbolo dado
        if simbolo == 'x':
            imagem_simbolo = constants.SIMBOLO_X
        elif simbolo == 'o':
            imagem_simbolo = constants.SIMBOLO_O
        simbolo = PhotoImage(file = f"{imagem_simbolo}") 
        # Adiciona a imagem a posicao clicada
        posicao_clicada.config(image = simbolo)
        posicao_clicada.image = simbolo
        

 
    '''
    Evento ativado ao usuário clicar em uma posição,
    realiza a jogada, incluindo atualização da
    lógica e da view
    '''
    def clique_posicao(self, event):
        
        # Seleciona a posição clicada pelo usuário
        posicao_clicada = event.widget    
        # Encontra a linha e coluna da jogada
        linha, coluna = self.posicoes[posicao_clicada]
        # Ativa a ação do controller
        self._controller.jogada_usuario(posicao_clicada, linha, coluna)

    '''
    Método responsável pela jogada do Agente Inteligente
    '''
    def agente_jogada_posicao(self):
        pass

    '''
    Método responsável por atualizar a view
    do placar do jogo
    '''
    def atualiza_pontuacao(self, pontuacao_usuario, pontuacao_agente_inteligente, contador_empates):
        
        
        dados_placar=f"| Usuário: {pontuacao_usuario} | \n | Computador: {pontuacao_agente_inteligente} | \n | Empates: {contador_empates} |"
        self.placar.config(text=dados_placar)
    
    '''
    Método responsável por resetar a view 
    e voltar a grade inicial, sem símbolos
    '''
    def _reset_view(self):
        
        # Encontra a coordenada selecionada
        for posicao in self.posicoes.keys():   
            posicao.config(highlightbackground="#121212", image=PhotoImage(master=self._tela, file = f'{constants.BACKGROUND_COR}'), highlightthickness=3)     
            
        self.status.config(text="")
           
    '''
    Método responsável por personalizar
    a view da grade quando ocorre um empate
    '''
    def _personaliza_empate(self):    
        for posicao in self.posicoes.keys():     
            posicao.config(highlightbackground="#F24F00")
            posicao.config(highlightthickness=5)
            self.status.config(text="EMPATE")
            self.status.config(fg="#F24F00")
            


    '''
    Método responsável por personalizar a view
    da grade quando o usuário ganha
    '''
    def _personaliza_usuario_ganhou(self, sequencia_vencedora):
        for posicao, coordenada in self.posicoes.items():
            if coordenada in sequencia_vencedora:
                posicao.config(highlightbackground="#32CD32")
                posicao.config(highlightthickness=5)
                self.status.config(text="VOCÊ VENCEU!")
                self.status.config(fg="#32CD32")


    '''
    Método responsável por personalizar a view
    da grade quando o Agente Inteligente ganhar
    '''
    def _personaliza_agente_ganhou(self, sequencia_vencedora):
        for posicao, coordenada in self.posicoes.items():
            if coordenada in sequencia_vencedora:
                posicao.config(highlightbackground="#ff0800")
                posicao.config(highlightthickness=5)
                self.status.config(text="VOCÊ PERDEU!")
                self.status.config(fg="#ff0800")


    '''
    Método responsável por atualizar a view
    para três situações:
        [] Empate
        [] Usuário Ganhou
        [] Agente Ganhou
    '''
    def reset(self, flag_status, sequencia_vencedora):
        
        # View de empate
        if flag_status == 'empate':
            self._personaliza_empate()
        
        # View de usuário ganhou
        elif flag_status == 'usuario_ganhou':
            self._personaliza_usuario_ganhou(sequencia_vencedora)
        
        # View de agente ganhou
        elif flag_status == 'agente_ganhou':
            self._personaliza_agente_ganhou(sequencia_vencedora)
        
        # Gera um espaço de 5 segundos para o usuário visualizar status da partida anterior
        sleep(5)

        # Reseta view
