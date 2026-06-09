def local_chai():
    yield "small"
    yield "medium"
    yield "large"


def imported_chai():
    yield "oolang"
    yield "green"
    yield "curdamom"


def ful_menu():
    yield local_chai()
    yield imported_chai()


for chai in ful_menu():
    for cup in chai:
        print(cup)
