import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keyords
    def __init__(self,**kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns - hlavní column je jeden a v něm jsou další s více columns
        self.cols = 1

            # create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Name: "))

        # add Input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="Favourite Pizza: "))
        
        # add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # add widgets
        self.top_grid.add_widget(Label(text="Favourite Drink: "))
        

        # add top_grid to the app
        self.add_widget(self.top_grid)


        # add Input Box
        self.drink = TextInput(multiline=False)
        self.top_grid.add_widget(self.drink)



        # create submit button
        self.submit = Button(text="Submit", 
        font_size=32,
        size_hint_y = None,
        height=50, 
        size_hint_x = None,
        width=200
        
        )

        # bind the button
        self.submit.bind(on_press=self.press)   
        self.add_widget(self.submit)

    #definice press funkce
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        drink = self.drink.text

        #print hello "Hello {name}, you like {pizza} pizza and your favourite drink is {drink}!"
        # Print it on the screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favourite drink is {drink}!'))

        # clear the imput boxes when pressing button
        self.name.text = ""
        self.pizza.text = ""
        self.drink.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
