
class Card:

    points_mapping = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, suit, value):

        if suit not in ['spade', 'club', 'diamond', 'heart']:
            raise ValueError(
                "{} must be in ['spade', 'club', 'diamond', 'heart']")

        self.suit = suit

        if value not in ['A', 'Q', 'K', 'J'] and value not in list(range(2, 11)):
            raise ValueError
        self.value = value

    def mapping_points(self):
        if isinstance(self.value, str):
            return self.points_mapping[self.value]
        else:
            return self.value

    def __add__(self, other):
        return self.mapping_points() + other.mapping_points()

    def __gt__(self, other):
        return self.mapping_points() > other.mapping_points()

    def __eq__(self, other):
        return self.mapping_points() == other.mapping_points()


class Deck:

    pass