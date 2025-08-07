class Game:
    total_games = 0  # Variável de classe para contar o total de jogos criados
    
    # Método __str__ é chamado quando usamos print() no objeto.
    # Ele deve retornar uma string que representa o objeto de forma legível.
    # O self faz referência ao objeto atual, permitindo acessar seus atributos e métodos.
    def __str__(self):
        return f"Nome do jogo: {self.name}\nAno de lançamento: {self.yearLaunch}\nMultiplayer: {self.multiplayer}\nNota: {self.note}"
    
    # Método construtor para inicializar os atributos do objeto
    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0.0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluations = 0.0
        self.evaluators = 0

    # Método para exibir uma ficha técnica do jogo
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome: {self.name}\nAno Lançamento: {self.yearLaunch}\nMultiplayer: {"Sim" if self.multiplayer else "Não"}\nNota: {self.note}.")

    # Método para avaliar o jogo, atualizando a nota total e o número de avaliadores
    def evaluate(self, note):
        self.totalEvaluations += note
        self.evaluators += 1

    # Método para calcular a média das avaliações
    def average(self):
        if self.evaluators == 0:
            return 0
        return self.totalEvaluations / self.evaluators

game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

game1.technical_sheet()
game2.technical_sheet()

game1.evaluate(9.0)
game1.evaluate(7.5)

game2.evaluate(6.5)
game2.evaluate(7.5)

print(f"Média de avaliações do game {game1.name}: {game1.average()}")
print(f"Média de avaliações do game {game2.name}: {game2.average()}")

# Exibindo o total de jogos criados
print(f"Total de jogos criados: {Game.total_games}")