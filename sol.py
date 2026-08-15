from random import shuffle


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


def is_face_down(stacks: dict, card: str) -> bool:
    for stack in stacks:
        for each_card in stack['face_down']:
            if each_card == card:
                return True
    return False


def is_face_up(stacks: dict, card: str) -> bool:
    for stack in stacks:
        for each_card in stack['face_up']:
            if each_card == card:
                return True
    return False


def deal_cards() -> [dict]:
    cards = [
        '♠1',
        '♠2',
        '♠3',
        '♠4',
        '♠5',
        '♠6',
        '♠7',
        '♠8',
        '♠9',
        '♠10',
        '♠J',
        '♠Q',
        '♠K',

        '♥1',
        '♥2',
        '♥4',
        '♥5',
        '♥6',
        '♥7',
        '♥8',
        '♥9',
        '♥10',
        '♥J',
        '♥Q',
        '♥K',

        '♦1',
        '♦2',
        '♦3',
        '♦4',
        '♦5',
        '♦6',
        '♦7',
        '♦8',
        '♦9',
        '♦10',
        '♦J',
        '♦Q',
        '♦K',

        '♣1',
        '♣2',
        '♣3',
        '♣4',
        '♣5',
        '♣6',
        '♣7',
        '♣8',
        '♣9',
        '♣10',
        '♣J',
        '♣Q',
        '♣K',
    ]
    shuffle(cards)
    return [
        {
            'face_down': [
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
                cards.pop(),
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
        {
            'face_down': [
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
                cards.pop(),
            ],
            'face_up': [
                cards.pop(),
            ],
        },
    ]
