class Node:
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None


def create_tree():

    root = Node(question="É um veículo?")

    root.yes = Node(question="Usa combustível?")
    root.no = Node(question="É eletrônico?")

    root.yes.yes = Node(answer="Carro")
    root.yes.no = Node(answer="Bicicleta")

    root.no.yes = Node(answer="Celular")
    root.no.no = Node(answer="Notebook")

    return root


