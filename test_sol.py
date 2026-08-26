from sol import *


def test_return_card():
    stacks = [
        {
            'face_down': ['♦1', '♦2'],
            'face_up': ['♦3'],
        },
        {
            'face_down': ['♦4', '♦5'],
            'face_up': [],
        },
        {
            'face_down': ['♦6', '♦7'],
            'face_up': [],
        }
    ]
    sol.return_card(stacks, '♦5')

    assert stacks == [
        {
            'face_down': ['♦1', '♦2'],
            'face_up': ['♦3'],
        },
        {
            'face_down': ['♦4'],
            'face_up': ['♦5'],
        },
        {
            'face_down': ['♦6', '♦7'],
            'face_up': [],
        }
    ]


def test_move():
    stacks = [
        {
            'face_down': ['♦1', '♦2'],
            'face_up': ['♣5'],
        },
        {
            'face_down': ['♦4', '♦5'],
            'face_up': ['♦6'],
        },
        {
            'face_down': ['♦9', '♦10'],
            'face_up': ['♣K'],
        }
    ]
    move_card(stacks, '♣5', '♦6')

    assert stacks == [
        {
            'face_down': ['♦1', '♦2'],
            'face_up': [],
        },
        {
            'face_down': ['♦4', '♦5'],
            'face_up': ['♦6', '♣5'],
        },
        {
            'face_down': ['♦9', '♦10'],
            'face_up': ['♣K'],
        }
    ]
