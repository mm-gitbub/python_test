# Create the class
class Button:
    width = 200
    height = 50

# Constructor for initializing the new Button objects
    def __init__(self,color,text):
        self.button_color = color
        self.button_text = text

# Create objects
button_1 = Button("yellow","Buy")
button_2 = Button("red", "Delete")

#Print the width and color of yellow button and red button
print(button_1.width)
print(button_1.button_color)
print(button_2.width)
print(button_2.button_color)

