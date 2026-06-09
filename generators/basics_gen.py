# def serve_chai():
#     yield "cup: small"
#     yield "cup: medium"
#     yield "cup: large"


# stall = serve_chai()

# for cup in stall :
#     print(cup)


def serve_chai():
    yield "cup: small"
    yield "cup: medium"
    yield "cup: large"


stall = serve_chai()

print(next(stall))
# print(next(stall))
# print(next(stall))
