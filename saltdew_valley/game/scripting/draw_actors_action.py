from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # self._video_service.clear_buffer()
        self._video_service.draw_background()
        self._video_service.draw_actors(cast.get_actors("players"))
        self._video_service.draw_actors(cast.get_actors("snails"))
        self._video_service.draw_actors(cast.get_actors("tilled_ground"))
        self._video_service.draw_text_bars(cast,cast.get_actors("text_bars"))
        self._video_service.draw_hotbar(cast.get_first_actor("hotbar"))
        self._video_service.draw_actors(cast.get_actors("salt"))
        # self._video_service.flush_buffer()