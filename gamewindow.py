import gameWindowClassAI
import gameWindowClassAIvsAI
import gameWindowClassHuman


def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4, delay_value=0, sound_included=0):
    """ Start a new game based on the player type. Opens a class, and activate it
    :param player_type: 'AI' or 'AIvsAI' or 'PLAYER'. Others are treated as 'PLAYER'
    :type player_type: str
    :param game_count: How many games to be played. Default: 1. In case of a Player type this is ignored
    :type game_count: int
    :param zero_included: 0 if exclude the digit zero from the game, any other value otherwise
    :type zero_included: int
    :param num_of_digits: Number of digits to guess. This value commonly determines the size of a row
    :type num_of_digits: int
    :param delay_value: Time to wait between each guess in Milliseconds. In case of a Player type this is ignored
    :type delay_value: int
    :param sound_included: 0 if exclude the sound from the game, any other value otherwise
    :type sound_included: int
    """

    if player_type == "AI":
        my_game = gameWindowClassAI.GameAI(game_count, zero_included, num_of_digits, sound_included)
        my_game.sleeping_Time = delay_value
        my_game.startGame()

    elif player_type == "AIvsAI":
        my_game = gameWindowClassAIvsAI.GameAIvsAI(game_count, zero_included, num_of_digits, sound_included)
        my_game.sleeping_Time = delay_value
        my_game.startGame()

    else:
        my_game = gameWindowClassHuman.GameHuman(zero_included, num_of_digits, sound_included)
        my_game.startGame()
