
class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")


class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")


class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


def perform_move(character):
    character.special_move()


# Create one object of each class
warrior = Warrior()
mage = Mage()
archer = Archer()

# Store objects in a list
characters = [warrior, mage, archer]

# Perform each character's special move
for character in characters:
    perform_move(character)
