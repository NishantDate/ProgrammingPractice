class Greeter:

    def __init__(self, boss):
        self.boss = boss
        self.enter_stack = []

    def enters(self, visitor):
        self.enter_stack.append(visitor)

    def greet(self):
        toGreet = self.enter_stack.pop()
        if toGreet:
            if toGreet != self.boss:
                return f"Welcome,{toGreet}"
            else:
                return f"Hello, {toGreet}"
        return None
    
if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    print(g.greet())