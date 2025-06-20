def print_hello_world(name: str, age: int):
    print(f"Hello {name} what is you day at {age}?")
    print("some")


name = input("Enter your name: ")
age = input("Enter you age: ")
print()

print_hello_world(name, age)
