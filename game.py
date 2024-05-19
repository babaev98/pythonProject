import script as sc
from script_bot import bot
from script_bot import player as play

player1 = sc.Player(input("Введите имя первого игрока, если это будет бот то введите :bot   :  "))
player1.player_or_bot()
player2 = sc.Player(input("Введите имя первого игрока, если это будет бот то введите :bot   :  "))
player2.player_or_bot()
victory = False


def play_or_bot(ob=object) -> object:
    result = object
    if ob.name == "bot":
        result = bot
    else:
        result = play
    return result


player1.striking(play_or_bot(player1).move())
player2.striking(play_or_bot(player2).move())

while not victory:
    if play.victory_check(player1.pole):
        print("Победил игрок номер 2")
        break
    if play.victory_check(player2.pole):
        print("Победил игрок номер 1")
        break
    if play_or_bot(player1) == bot:
        bot.logic_bot(player2.pole, bot.move())
    elif play_or_bot(player1) == play:
        player2.striking(play.move())
    player1.PrinPole(player2.pole)
    if play_or_bot(player2) == bot:
        bot.logic_bot(player1.pole, bot.move())
    elif play_or_bot(player2) == play:
        player1.striking(play.move())
    player2.PrinPole(player1.pole)

print("Конец")
