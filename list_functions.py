lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
x = lucky_numbers.copy()
#friends.extend(lucky_numbers)
friends.append("creed")
#friends.insert(1, "Kelly")
#friends.remove("Jim")
#friends.clear()
friends.pop()
print(friends.index("Toby"))

print(friends.count("Kevin"))
print(friends)
friends.sort()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)
print(x)