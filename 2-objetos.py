class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0.0

# Primeiro jogo
game1 = Game()
# Atribuindo valores ao primeiro jogo
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 10.0

# Segundo jogo
game2 = Game()
# Atribuindo valores ao segundo jogo
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0

print("###Dados do Jogo###")
print(f"Nome do jogo: {game1.name}\nAno de lançamento: {game1.yearLaunch}\nMultiplayer: {game1.multiplayer}\nNota: {game1.note}")
print(f"\nNome do jogo: {game2.name}\nAno de lançamento: {game2.yearLaunch}\nMultiplayer: {game2.multiplayer}\nNota: {game2.note}")