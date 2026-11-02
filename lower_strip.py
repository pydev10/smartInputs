# Case-insensitive, whitespace-trimming version of "inputs_tracker.py"
class _InputMatcher:
    def __init__(self, history, match_all):
        self.history = history
        self.match_all = match_all

    def __eq__(self, value):
        if not self.history:
            return False

        value = value.strip().lower()

        if self.match_all:
            return all(answer.strip().lower() == value for answer in self.history)
        return any(answer.strip().lower() == value for answer in self.history)


class InputsTracker:
    def __init__(self):
        self.history = []

    def ask(self, prompt_text):
        try:
            answer = input(prompt_text)
            self.history.append(answer)
            return answer

        except KeyboardInterrupt:
            print("Dont interrupt the keyboard by Crtl + C!")
            return None

    def reset(self):
        self.history.clear()

    @property
    def all(self):
        return _InputMatcher(self.history, match_all=True)

    @property
    def any(self):
        return _InputMatcher(self.history, match_all=False)