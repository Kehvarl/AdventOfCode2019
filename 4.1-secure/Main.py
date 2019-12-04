def checkPassword(password):
    password = str(password)
    adjMatch = False
    if len(password) < 6:
        return False
    for i in range(0, len(password) - 1):
        if int(password[i + 1]) < int(password[i]):
            return False
        if int(password[i + 1]) == int(password[i]):
            adjMatch = True

    return adjMatch


print(checkPassword(111111))
print(checkPassword(223450))
print(checkPassword(123789))

count = 0
for p in range(246515, 739106):
    if checkPassword(p):
        count += 1

print(count)
