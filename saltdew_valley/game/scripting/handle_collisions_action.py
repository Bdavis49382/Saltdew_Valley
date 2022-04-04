from game.scripting.action import Action
from game.casting.text_bar import Text_bar
from game.shared.tile import Tile
class Handle_collisions_action(Action):

    def __init__(self,callback) -> None:
        super().__init__()
        self._callback = callback
    


    def execute(self,cast,script):
        self.check_for_game_over(cast)
        self.check_for_salt(cast)
        
    def check_for_salt(self,cast):
        snail = cast.get_first_actor("snails")
        salt = cast.get_actors("salt")

        for piece_of_salt in salt:
            if piece_of_salt.get_position().equals(snail.get_tiled_coordinates()):
                cast.remove_actor("salt",piece_of_salt)
                snail.set_position(Tile(0,0))
                
            

    def check_for_game_over(self,cast):
        player = cast.get_first_actor("players")
        snail = cast.get_first_actor("snails")

        if player.get_position().equals(snail.get_position()):

            cast.add_actor("text_bars",Text_bar("Game Over ",Tile(1,4)))

            self._callback.game_over()