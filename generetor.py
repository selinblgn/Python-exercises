def cube():
    for i in range(5):
        yield i**3

print(cube())        