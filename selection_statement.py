# If - else
print("Type your age: ")
your_age = int(input())

if (your_age < 18):
    print("You are illegal to smoke")
else:
    print("You are legal to smoke")


# If - elif - else
print("Type your grade: ")
your_grade = float(input())
if (your_grade < 5.0):
    print("You failed the subject")
elif (your_grade > 5.0 and your_grade < 6.5):
    print("Average grade")
elif (your_grade >= 6.5 and your_grade < 8.0):
    print("Good grade")
else:
    print("Excellent grade")


# Nested if - else
print("Type your country: ")
your_country = input()
print("Type your age: ")
your_age_2 = int(input())
if (your_country == "Vietnam"):
    if(your_age_2 >= 18):
        print("You're legal to ride a motormike")
    else:
        print("You're illegal to ride a motormike")

