def print_hello_world(name: str, age: int) -> list:
    print(f"Hello {name} what is you day at {age}?")
    return [
        {"": 1},
        [1, 2],
        {"som": 2},
        [123, 44, 1111],
    ]


print(print_hello_world("Vitaly", 22))
print(NameError())
print(print_hello_world("ruff or jedi or pylsp"))
