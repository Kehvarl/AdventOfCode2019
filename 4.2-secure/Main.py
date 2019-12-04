def checkPassword(password):
    password = str(password)

    if len(password) < 6:
        return False

    for i in range(0, len(password) - 1):
        if int(password[i + 1]) < int(password[i]):
            return False

    adjMatch = False
    thisMatch = False
    cur = ""
    cur_count = 1
    for i in range(0, len(password)):
        if password[i] == cur:
            cur_count += 1
            if cur_count == 2: thisMatch = True
            if cur_count > 2: thisMatch = False
        else:
            if thisMatch:
                adjMatch = True
            thisMatch = False
            cur = password[i]
            cur_count = 1
    if thisMatch:
        adjMatch = True

    return adjMatch


print(checkPassword(111111))  # False
print(checkPassword(223450))  # False
print(checkPassword(123789))  # False
print(checkPassword(112233))  # True
print(checkPassword(123444))  # False
print(checkPassword(111122))  # True

count = 0
for p in range(246515, 739106):
    if checkPassword(p):
        count += 1

print(count)
