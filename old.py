from random import shuffle

# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
# https://en.wikipedia.org/wiki/Playing_card_suit

# ♠ ♥ ♦ ♣

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

piles = [
    [
        '♠1',
        '♠2',
        '♠3',
    ],
    [
        '♣10',
    ],
    [
        '♣K',
    ],
    [
        '♦6',
        '♦7',
        '♦8',
    ],
    [
        '♥Q',
        '♥K',
    ],
    [

    ],
    [
        '♦1',
        '♦2',
        '♦3',
        '♦4',
        '♦5',
        '♦6',
        '♦7',
        '♦8',
    ],
]


def print_piles() -> None:
    for rang in range(0, 13):
        str = ''
        for col in range(0, 7):
            if len(piles[col]) > rang:
                carte = piles[col][rang]
            else:
                carte = ''
            str += carte.rjust(5)
        print(str)


def main() -> None:
    # print(cards)
    # shuffle(cards)
    # print(cards)
    print_piles()


#    for index in range(0, 10):
#        template = 'fibonacci({index}) = {result}'
#        print(template.format(index=index, result=fibonacci(index)))


if __name__ == '__main__':
    main()
