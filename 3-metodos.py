class Game:
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

game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

print("###Dados do Jogo###")
print(game1)
print(game2)