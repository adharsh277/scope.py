


def myfunc():
    global x
    x = 300


myfunc()
x = 300


def myfunc():
    global x
    x = 200


myfunc()

print(x)

print(x)


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)
