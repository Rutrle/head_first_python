class CountFromBy:
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


if __name__ == '__main__':
    my_counter = CountFromBy(5, 2)
    my_counter.increase()
    my_counter.increase()
    print(my_counter)
