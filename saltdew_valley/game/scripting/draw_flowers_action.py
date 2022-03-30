from constants import *
from game.scripting.action import Action


class DrawFlowersAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        flowers = cast.get_actors(FLOWER_GROUP)
        self._video_service.clear_buffer()
        for flower in flowers:
            
            self._video_service.draw_flower(flowers)
        
        self._video_service.flush_buffer()