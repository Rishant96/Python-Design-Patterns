"""
This is a variation on the standard builder pattern where the
calls to the builder are chained, and the builder is defined
as an inner class.
"""


class Pizza:
    """
    This class is a mock representation of a pizza.
    It class only supports 'init' and 'str' dunder methods,
    and does not contain any preparation logic.
    However, it supports addons such as, 'garlic' and 'extra cheese'.
    """
    def __init__(self, builder):
        """
        Initializer for the 'Pizza' class.
        The 'builder' provides the 'build()' method
        and boolean fields 'garlic' and 'extra cheese'.
        """
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        extra_cheese = 'yes' if self.extra_cheese else 'no'
        info = ('Pizza with,', f'\tGarlic: {garlic}',
                f'\tExtra cheese: {extra_cheese}')
        return '\n'.join(info)

    class PizzaBuilder:
        """
        Contains preparation logic, and exposes public methods
        for customizing add-ons such as, 'garlic' and 'extra cheese'.
        """
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            """
            Adds garlic to your pizza.

            Note: returns the builder object to support the chaining
                  of calls by the builder, as part of the fluent design.
            """
            self.garlic = True
            return self

        def add_extra_cheese(self):
            """
            Adds extra cheese to your pizza.

            Note: returns the builder object to support the chaining
                  of calls by the builder, as part of the fluent design.
            """
            self.extra_cheese = True
            return self

        def build(self):
            """
            This method is to be called when the pizza is ready for the
            oven. It returns a 'Pizza' object, without any add-ons.

            Note: prior chained calls need to be made in order to customize
            the order.
            """
            return Pizza(self)


if __name__ == '__main__':
    my_favorite_pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese()\
        .build()
    no_garlic_pizza = Pizza.PizzaBuilder().add_extra_cheese().build()
    print(my_favorite_pizza)
    print('and also,')
    print(no_garlic_pizza)
