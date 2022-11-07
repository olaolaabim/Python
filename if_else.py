is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

if is_male and is_tall:
    print("You are a male and tall or both")
else:
    print("You neither male nor tall")

if is_male and is_tall:
    print("You are a male and tall or both")
elif is_male and not (is_tall):
    print("you are short")
elif is_male and not (is_tall):
    print("you are not male but tall")
else:
    print("You neither male nor tall")