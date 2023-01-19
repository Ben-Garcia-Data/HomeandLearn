from Multiverse import Superpowered


class Superheroes(Superpowered):
    def __init__(self, name, code, rating, score):
        super().__init__(name, code, rating)
        self.likeability_score = score

    def likeability(self):
        niceness = str(self.likeability_score) + " YAYS out of 5"
        return niceness

    def print_data(self):
        print(
            self.convert_to_proper_case() + ': Superpower is - ' + self.abilities() + ", Rating: " + self.get_star_rating() + " stars" + ", Likeability rating: " + self.likeability())

class Supervillains(Superpowered):

    def __init__(self, name, code, rating, score):
        super().__init__(name, code, rating)
        self.evil_score = score

    def evilness(self):
        evil_ranking = str(self.evil_score) + " BOOS out of 5"
        return evil_ranking

    def print_data(self):
        print(
            self.convert_to_proper_case() + ': Superpower is - ' + self.abilities() + ", Rating: " + self.get_star_rating() + " stars" + ", " + self.evilness())
