# Class Game
# Esta classe representa um jogo com atributos como nome, ano de lançamento, se é multiplayer e nota.
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

class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} não possui jogos avaliados.")
        else:
            average_note = total_notes / num_games
            print(f"A média de notas dos jogos do estúdio {self.name} é: {average_note:.2f}")

game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, True, 9.5)
game2 = Game("Super Mario Odyssey", 2017, True, 9.0)
game3 = Game("Animal Crossing: New Horizons", 2020, True, 8.5)

studio = GameStudio("Awesome Games Studio")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)
studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()