def hello(a="hmm"):
    print(a)

hello.__name__ = "ff"
print(hello.__name__)