# .lower() version of "inputs_tracker.py"
class _InputMatcher:
    def __init__(self, history, match_all):
        self.history = history
        self.match_all = match_all

    def __eq__(self, value):
        if not self.history:
            return False

        if self.match_all:
            return all(answer.lower() == value.lower() for answer in self.history)
        return any(answer.lower() == value.lower() for answer in self.history)

class InputsTracker:
    def __init__(self):
        self.history = []

    def ask(self, prompt_text):
        try:
            # ↓ DO NOT REMOVE: This is the fix to that bug where the string from the .ask() function get overriden by by other .ask() function
            print(prompt_text, end="", flush=True)

            answer = input()
            self.history.append(answer)
            return answer

        except KeyboardInterrupt:
            return None

    def reset(self):
        self.history.clear()

    @property
    def all(self):
        return _InputMatcher(self.history, match_all=True)

    @property
    def any(self):
        return _InputMatcher(self.history, match_all=False)