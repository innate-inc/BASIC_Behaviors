from innate.behavior import Behavior
from typing import List

class ChessBehavior(Behavior):
    def name(self) -> str:
        return "chess_directive"
    def get_skills(self) -> List[str]:
        return ["play_move", "compute_chess_move", "calibrate_chess"]
    def get_prompt(self) -> str:
        return """You are a chess-playing robot companion.
          Always think strategically and make the best possible moves. 
          When playing chess, analyze the board position carefully 
          and consider multiple move options before making your decision."""