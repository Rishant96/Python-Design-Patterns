import copy


class A:
    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 34

    def __str__(self):
        return f'{self.x}, {self.msg}, {self.y},'


if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(itm) for itm in (b, c)])
    print([i for i in (b, c)])
