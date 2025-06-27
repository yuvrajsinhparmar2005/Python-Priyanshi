#Mark Input
math = int(input("Enter marks in Maths : "))
phy = int(input("Enter marks in Physics : "))
chem = int(input("Enter marks in Chemistry : "))
bio = int(input("Enter marks in Biology : "))
eng = int(input("Enter marks in English : "))

# Calculate Total and Percentage
total = math + phy + chem + bio + eng
percentage = (total / 500) * 100

# Display Result
print("Total Marks:",total)
print("Percentage", percentage)

if percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")

