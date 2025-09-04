from innate.behavior import Behavior
from typing import List

class SecurityGuard(Behavior):
    def name(self) -> str:
        return "security_guard_behavior"


    def get_skills(self) -> List[str]:
        return ["navigate", "open_door", "send_email"]

    def get_prompt(self) -> str:
        return """You are a security guard robot. Patrol the house,
         stay alert and professional, watch for intruders, 
         open doors when needed, and send an email immediately 
         if you find one."""