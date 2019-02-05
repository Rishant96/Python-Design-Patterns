from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparing baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme-fraiche')
PizzaToppings = Enum('PizzaToppings', 'mozzarella bacon ham mushrooms \
    red_onion oregano')
STEP_DELAY = 3  # in seconds, for the sake of the example

class Pizza:
    def __init__( self, name ):
        self.name = name
        self.dough = None
        self.sauce = None
        self.toppings = []

    def __str__( self ):
        return self.name

    def prepare_dough( self, dough ):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough for \
            your {self} pizza...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')

class MargheritaBuilder:
    def __init__( self ):
        self.pizza = Pizza('Margherita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5  # in seconds, for sake of the example

    def prepare_dough( self ):
        self.progress = PizzaProgress.preparing
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce( self ):
        print('adding the tomato sauce to your margherita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_toppings( self ):
        print('adding the toppings (mozzarella, oregano) to your margherita')
        self.pizza.toppings.append([topping for topping in (
            PizzaToppings.mozzarella, PizzaToppings.oregano)])
        time.sleep(STEP_DELAY)
        print('added the toppings: mozzarella, and oregano')

    def bake( self ):
        self.progress = PizzaProgress.baking
        print(f'baking your margherita for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margherita is ready!')


class CreamyBaconBuilder:
    def __init__( self ):
        self.pizza = Pizza('Creamy Bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7  # in seconds, for the sake of the example

    def prepare_dough( self):
        self.progress = PizzaProgress.preparing
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce( self ):
        print('adding the creme fraiche to your creamy bacon pizza...')
        self.pizza.sauce = PizzaSauce.creme-fraiche
        time.sleep(STEP_DELAY)
        print('done adding the creme fraiche.')

    def add_toppings( self ):
        print('adding the toppings (mozzarella, bacon, ham, \
            red onion, mushrooms, oregano) to your creamy bacon pizza')
        self.pizza.toppings.append([topping for topping in (
            PizzaTopping.mozzarella, PizzaTopping.bacon,
            PizzaTopping.ham,PizzaTopping.mushrooms,
            PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, \
            mushrooms, red onion, oregano)')

    def bake( self ):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon pizza for \
            {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon pizza is ready!')


class Waiter:
    def __init__( self ):
        self.builder = None

    def construct_pizza( self, builder ):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce,
            builder.add_toppings, builder.bake)]

    @property
    def pizza( self ):
        return self.builder.pizza


def validate_style( builders ):
    try:
        pizza_style = input('What pizza would you like, \
            [m]argherita or [c]reamy bacon? ')
        builder = builders[pizza_style]()
    except KeyError as err:
        print('Sorry, only margherita (key m) and creamy bacon \
            (key c) are available') 
        return False, None
    return True, builder
