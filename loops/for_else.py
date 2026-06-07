staff = [("amit", 10000), ("prakash", 20000), ("rohit", 30000)]
for name, salary in staff:
    if salary >= 10000:
        print(f"Hello {name} your salary is {salary}")

        break

else:
    print("No staff found")
