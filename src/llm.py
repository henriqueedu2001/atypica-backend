import ollama

class LLM:
    def __init__(self, model: str):
        self.model = model
        return

    def ask(self, query: str) -> str:
        answer = ollama.generate(model=self.model, prompt=query)
        answer = answer.get('response')
        return answer