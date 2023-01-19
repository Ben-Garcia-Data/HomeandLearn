# https://www.homeandlearn.uk/python-classes-inheritance.html

from Heroes import Superheroes, Supervillains

hero_one = Superheroes("luke cage", "IB", 4, score=8)
hero_one.convert_to_proper_case()
hero_one.abilities()
hero_one.get_star_rating()

hero_two = Superheroes("jessica jones", "SS", 2, score=6)
hero_two.convert_to_proper_case()
hero_two.abilities()
hero_two.get_star_rating()

villain_one = Supervillains("mystique", "MG", 4,score=3)
villain_one.convert_to_proper_case()
villain_one.evilness()


hero_one.print_data()
hero_two.print_data()
villain_one.print_data()