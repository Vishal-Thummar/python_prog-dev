chai_type = "plain"


def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()


front_desk()
print("Final Order Tea : ", chai_type)
