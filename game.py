def play_game(root):

    node = root

    while node.answer is None:

        resp = input(node.question + " (s/n): ")

        if resp.lower() == "s":
            node = node.yes
        else:
            node = node.no

    print("\nA resposta é:", node.answer)
