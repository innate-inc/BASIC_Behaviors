from innate.behavior import Behavior
from typing import List

class CleanSocks(Behavior):
    def name(self) -> str:
        return "clean_socks_behavior"


    def get_skills(self) -> List[str]:
        return ["navigate", "pick_up_sock", "drop_socks"]

    def get_prompt(self) -> str:
        return """You are a sock-cleaning robot. Search the room for socks.
        When you see one, go to it, pick it up, and put it in the wooden box.
         Keep doing this until there are no more socks."""