class Count:
    def __init__(self, init_steps):
        self.init_steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args  # args => tuple (100, )
        self.init_steps += inc


count_step = Count(100)
count_step(25)
count_step(50)
print(count_step.init_steps)