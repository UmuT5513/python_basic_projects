list = []
for i in range(1,151):
    list.append(i)

    if i % 15 == 0:
        list.remove(i)
        list.append("FizzBuzz")
    elif i % 5 == 0:
        list.remove(i)
        list.append("Buzz")
    elif i % 3 == 0:
        list.remove(i)
        list.append("Fizz")

print(list)
