def infinate():
    count = 1
    while True:
        yield f"Refil # {count}"
        count += 1
        return count


stall = infinate()
user = infinate()
meet = infinate()

for _ in range(5):
    print(f"If Runs Stal That Time {next(stall)}\n")
for _ in range(1):
    print(f"If Runs user That Time {next(user)}\n")
for _ in range(16):
    print(f"If Runs meet That Time {next(meet)}\n")


# print(next(stall))
# print(next(stall))
