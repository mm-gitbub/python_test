# Creating a class of cake and declaring the variables
class Cake:
    recipe_type = "Basic cake"
    baking_temperature = 180
    baking_time = 30

# To create different objects, we are using constructor
# Call the method, self as argument, self argument does not contain any value and only passes parameters to object
# Constructor for initializing new cake objects
    def __init__(self,flour,sugar,milk,eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_milk = milk
        self.cake_eggs = eggs
# Defining methods
    def mixing_the_cake(self):
        print(f"Mixing {self.cake_flour} grams. of flour, {self.cake_sugar} grams of sugar, {self.cake_milk} ml of milk and {self.cake_eggs} no. of eggs")

    def baking(self):
        print(f"Bake the cake with {self.__class__.baking_temperature} degree centigrade for {self.__class__.baking_time} minutes")

    def serve(self):
        print("Serve the cake with decorations")

# # Create objects.
# # Flour, sugar, milk, eggs in order
# cake_1 = Cake(200,140,110,2)
# cake_2 = Cake(210,150,120,3)
# cake_3 = Cake(250,175,125,3)

# # Check for ingredients of the object
# print(f"Flour used for cake_1 object is {cake_1.cake_flour}")
# print(f"Baking time for cake_2 object is {cake_2.baking_time}")
# cake_3.baking()
# cake_1.serve()
# cake_2.mixing_the_cake()

# Create another clas named Bakery it has the preparation method which calls other methods from class cake

class Bakery:
    def __init__(self,name):
        self.bakery_name = name # Initializing the method that sets the name of the Bakery

# Method to preparation
    def prepare_cake(self,Cake):
        print(f"Preparation of the cake from the {self.bakery_name} bakery")
        Cake.mixing_the_cake()
        Cake.baking()
        Cake.serve()

# Creating instances/objects with specific ingredients- flour, sugar, milk, eggs
cake_1 = Cake(200,200,240,2)
cake_2 = Cake(200, 150, 220, 2)

# Create instance for Bakery class
bakery_1 = Bakery("TripleTen Bakery")

# Use the Bakery instance to prepare cake_1
bakery_1.prepare_cake(cake_1)
