from prompts.tutor.v1 import tutor_prompt as tutor_prompt_v1

from prompts.tutor.v2 import tutor_prompt as tutor_prompt_v2


class PromptManager:

    _prompts = {
        'tutor_v1': tutor_prompt_v1,
        'tutor_v2': tutor_prompt_v2,
    }

    @classmethod
    def get_prompt(cls,name:str):
        if name not in cls._prompts:
            raise ValueError(f"Prompt {name} not found")
        return cls._prompts[name]
        