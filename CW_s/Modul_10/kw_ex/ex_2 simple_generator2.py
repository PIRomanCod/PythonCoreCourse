def simple_generator():
    yield "First"  # yield == return
    yield "Second"

gen = simple_generator()
print(gen)

r = next(gen)
print(r)

r = next(gen)
print(r)

r = next(gen)
print(r)