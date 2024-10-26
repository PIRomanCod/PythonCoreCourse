def simple_generator():
    yield "First"  # yield == return
    yield "Second"

for r in simple_generator():
    print(r)