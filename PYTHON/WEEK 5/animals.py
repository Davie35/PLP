# animals.py

# Base class (optional, for structure)
class Animal:
    def move(self):
        pass  # generic placeholder


# Dog class
class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")


# Bird class
class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")


# --- Demonstration ---
if __name__ == "__main__":
    animals = [Dog(), Bird()]

    for animal in animals:
        animal.move()
