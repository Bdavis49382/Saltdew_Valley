from constants import *
from game.scripting.action import Action


class DrawFlowersAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        flowers = cast.get_actors(FLOWER_GROUP)
        
        for flower in flowers:
            body = flower.get_body()

            # if brick.is_debug():
            #     rectangle = body.get_rectangle()
            #     self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = flower.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)