name = "Abhishek"
count = 1


def func():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "green"
        print(color)
        print(name)

    greeting("Abhishek")


func()
