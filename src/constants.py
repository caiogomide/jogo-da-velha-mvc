from pathlib import Path

# função que encontra o local do arquivo
def encontra_arquivo(pasta_arquivo, nome_arquivo):
    local_jogo = Path(__file__).absolute().parent
    local_arquivo = local_jogo.parent / f'assets/{pasta_arquivo}/{nome_arquivo}'
    return local_arquivo

# Constantes relacionadas aos ícones utilizados no jogo
ICONE_X = encontra_arquivo('icones','icone-x.png')
ICONE_O = encontra_arquivo('icones','icone-o.png')
ICONE_PESSOA = encontra_arquivo('icones','icone-pessoa.png')
ICONE_ROBO = encontra_arquivo('icones','icone-robo.png')
# Constantes relacionadas aos símbolos utilizados no jogo
SIMBOLO_X = encontra_arquivo('simbolos','simbolo-x.png')
SIMBOLO_O = encontra_arquivo('simbolos','simbolo-o.png')
# Constante do background do jogo
BACKGROUND_COR  = encontra_arquivo('background','background-cor.png')

