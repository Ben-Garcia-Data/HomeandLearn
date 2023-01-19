class Superpowered:
    def __init__(self, name, code, rating):
        self.full_name = name
        self.superhero_code = code
        self.superhero_rating = rating

    def convert_to_proper_case(self):
        proper_case = self.full_name.title()
        return proper_case

    def abilities(self):
        superpower = 'No Superpower'
        if self.superhero_code == 'SS':
            superpower = "Super Strength"
        elif self.superhero_code == 'IB':
            superpower = "Impervious to Bullets"
        elif self.superhero_code == 'HA':
            superpower = "Hyper-awareness"
        elif self.superhero_code == 'MG':
            superpower = "Morphogenetic"
        return superpower

    def get_star_rating(self):
        star_rating = self.__convert_score()
        return star_rating

    def __convert_score(self):
        arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        return arr[self.superhero_rating]

    def print_data(self):
        print(
            self.convert_to_proper_case() + ': Superpower is - ' + self.abilities() + ", Rating: " + self.get_star_rating() + " stars")