import time

# Definindo uma função para formatar o tempo
def formatar_tempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return f'{horas:02}:{minutos:02}:{segundos:02}'

# Classe para representar um grupo
class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.tempo = 0
        self.inicio = None

    def iniciar_atividade(self):
        self.inicio = time.time()

    def pausar_atividade(self):
        if self.inicio is not None:
            self.tempo += time.time() - self.inicio
            self.inicio = None

# Lista para armazenar grupos
grupos = []

# Função para adicionar um novo grupo
def adicionar_grupo(nome):
    grupo = Grupo(nome)
    grupos.append(grupo)
    return grupo

# Função para iniciar a atividade para um grupo
def iniciar_atividade_grupo(grupo):
    grupo.iniciar_atividade()

# Função para pausar a atividade para um grupo
def pausar_atividade_grupo(grupo):
    grupo.pausar_atividade()

# Função para mostrar a classificação
def mostrar_classificacao():
    grupos_ordenados = sorted(grupos, key=lambda x: x.tempo)
    print("=== Classificação ===")
    for i, grupo in enumerate(grupos_ordenados):
        print(f"{i+1}. {grupo.nome} - Tempo: {formatar_tempo(grupo.tempo)}")

# Adicionar grupos e iniciar atividades
grupo1 = adicionar_grupo("Grupo A")
grupo2 = adicionar_grupo("Grupo B")
grupo3 = adicionar_grupo("Grupo C")

iniciar_atividade_grupo(grupo1)
time.sleep(5)  # Simulando atividade por 5 segundos
pausar_atividade_grupo(grupo1)

iniciar_atividade_grupo(grupo2)
time.sleep(7)  # Simulando atividade por 7 segundos
pausar_atividade_grupo(grupo2)

iniciar_atividade_grupo(grupo3)
time.sleep(3)  # Simulando atividade por 3 segundos
pausar_atividade_grupo(grupo3)

# Mostrar classificação
mostrar_classificacao()
