"""Ex1"""

"""Create a Person class which will have three properties:
    Name
    List of foods they like
    List of foods they hate
In this class, create the method taste():
    It will take in a food name as a string.
    Return {person_name} eats the {food_name}.
    If the food is in the person's like list, add 'and loves it!' to the end.
    If it is in the person's hate list, add 'and hates it!' to the end.
    If it is in neither list, simply add an exclamation mark to the end.
    p1 = Person("Sam", ["ice cream"], ["carrots"])
    p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
    p1.taste("cheese") ➞ "Sam eats the cheese!"
    p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"""

from typing import List

# class Person:
#     def __init__(self, name: str, good_food: List[str], bad_food: List[str]) -> None:
#         self.name = name
#         self.good_food = good_food
#         self.bad_food = bad_food
    
#     def taste(self, food: str) -> str:
#         if food in self.good_food:
#             return f"{self.name} eats the {food} and loves it!"
#         elif food in self.bad_food:
#             return f"{self.name} eats the {food} and hates it!"
#         else:
#             return f"{self.name} eats the {food}!"

# p1 = Person("Sam", ["ice cream", "cake"], ["carrots", "mushrooms"])
# print(p1.taste("cake"))
# print(p1.taste("mushrooms"))
# print(p1.taste("chesse"))

"""Ex2"""

"""Create a class Smoothie and do the following:
    Create an instance attribute called ingredients.
    Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
    Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
    Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented."""

class Smoothie:
    def __init__(self, ingridients: str) -> None:
        self.ingridients = ingridients

    def get_cost(self):
        ingridients_prices = {"Apple":1.2, "Kiwi":1.5, "Banana":1.8}
        cost = 0
        for ingridient in self.ingridients:
            cost += ingridients_prices.get(ingridient, 0)
        return cost

    def get_price(self):
        cost = self.get_cost()
        return round(cost + cost * 1.5)
    
    def get_name(self):
        ingridients = sorted(self.ingridients)
        if len(ingridients) > 1:
            name = " Fusion"
        else:
            name = " Smothie"
        return " ".join(ingridients) + name
    
class AppleKiwiSmothie(Smoothie):
    def __init__(self) -> None:
        super().__init__(["Apple","Kiwi"])
        
class KiwiBanana(Smoothie):
    def __init__(self) -> None:
        super().__init__(["Kiwi", "Banana"])

ak_smoothie = AppleKiwiSmothie()
kb_smothie = KiwiBanana()

print(kb_smothie.get_name())
print(kb_smothie.get_cost())
print(kb_smothie.get_price())


"""Ex3"""

"""Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.
Attributes
An instance of the class Sudoku will have one attribute:
    board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
Methods
An instance of the class Sudoku wil have three methods:
    get_row(n): will return the row in position n.
    get_col(n): will return the column in position n.
    get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.
    game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
game.board ➞ [
  [4, 1, 7, 9, 5, 0, 0, 3, 0],
  [0, 0, 0, 0, 0, 0, 7, 0, 0],
  [0, 6, 0, 0, 0, 7, 0, 0, 0],
  [0, 5, 0, 0, 0, 9, 1, 0, 6],
  [8, 0, 0, 6, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 4, 0, 0],
  [9, 0, 0, 0, 0, 5, 0, 0, 0],
  [0, 0, 0, 4, 3, 0, 0, 0, 0],
  [2, 0, 0, 7, 0, 1, 5, 8, 0]
]
game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]"""

# class Sudoku:
#     def __init__(self, board: List(str|int)) -> None:
#         self.board = board

#     def get_row(n): #will return the row in position n.
#         return
#     def get_col(n): #will return the column in position n.
#         return
#     def get_sqr([n, m]):# will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.
#         return