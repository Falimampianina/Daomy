import random

from data_structures.playables.domino_snake import DominoSnake
from data_structures.players.player import Player


def ai_make_random_legal_move(snake: DominoSnake, player: Player):
    if player.useless_hand(snake):
        return
    else:
        playable_pieces = []
        for domino in player.dominoes:
            if snake.check_if_domino_can_be_placed(domino):
                playable_pieces.append(domino)
        chosen_piece = random.choice(playable_pieces)
        snake.place_domino(chosen_piece)
        player.dominoes.remove(chosen_piece)
