from sqlalchemy import null


class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        # if self.items.
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity   
        return 'I now have ' + str(self.items[item]) + ' ' + str(item)

        print('I now have ' + str(self.items[item]) + ' ' + str(item))

    def use_item(self, item, quantity):
        if self.items[item] <= quantity:
            return 'Uh oh, buy more Mayo!'
            print('Uh oh, buy more Mayo!')
        else:
            self.items[item] -= quantity
            return 'I have ' + str(self.items[item]) + ' ' + str(item) + ' left' 
            print('I have ' + str(self.items[item]) + ' ' + str(item) + ' left')

# fridgey = SmartFridge()
# fridgey.add_item('Mayo', 1)
# fridgey.add_item('Mayo', 2)
# fridgey.use_item('Mayo', 2.5)
# fridgey.use_item('Mayo', 0.5)

import doctest
doctest.testmod(verbose=True)