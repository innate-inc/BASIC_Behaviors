This a library of Behaviors for BASIC. BASIC is the embodied AI agent that controls Mars. BASIC gives Mars the ability to reason, memorize, plan, make decisions, and use physical and digital skills.

Behaviors steer BASIC to perform complex long horizon tasks.

Defining a Behavior requires two components:
1. List of skills that BASIC has access to
2. A natural language prompt that instructs BASIC how to perform the task

```python
from innate.behavior import Behavior
from typing import List


class BasicBehavior(Behavior):
    def get_skills(self) -> List[str]:
        """
        List the Skills this behavior can call.
        Return: list of skill names (snake_case)
        """
        return [
        "skill_one",
        "skill_two",
        ]


    def get_prompt(self) -> str:
        """
        Define how BASIC should use the Skills.
        Return: instructions shown to the agent.
        """
        return """You are Mars, a capable robot. You have these skills available:


        skill_one:
        - Used for [purpose]
        - Parameters: [list parameters if any]
        - Use when [describe situations]


        skill_two:
        - Used for [purpose]
        - Parameters: [list parameters if any]
        - Use when [describe situations]


        For each request:
        1. Choose the appropriate skill
        2. Extract any needed parameters
        3. Execute the skill
        4. Provide clear, concise feedback"""
```
```


For more details visit [our documentation](https://docs.innate.bot/docs.innate.bot/basic/behaviors)

