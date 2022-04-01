from game.scripting.action import Action
from game.casting.text_bar import Text_bar
from game.shared.tile import Tile
class Handle_collisions_action(Action):

    def __init__(self,callback) -> None:
        super().__init__()
        self._callback = callback
    


    def execute(self,cast,script):
        self.check_for_game_over(cast)
        
    

    def check_for_game_over(self,cast):
        player = cast.get_first_actor("players")
        snail = cast.get_first_actor("snails")

        if player.get_position().equals(snail.get_position()):

            cast.add_actor("text_bars",Text_bar("Game Over ",Tile(1,4)))

            self._callback.game_over()