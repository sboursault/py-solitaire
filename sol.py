def find_stack(stacks: dict, card: str) -> dict | None:
    for stack in stacks:
        if card in stack['face_down'] or card in stack['face_up']:
            return stack
    return None


def return_card(stacks: dict, card_clicked: str):
    stack = find_stack(stacks, card_clicked)
    if len(stack['face_up']) == 0:
        stack['face_down'].pop()
        stack['face_up'].append(card_clicked)
