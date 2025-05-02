#Priyangshu Kumar Das - 24BPE079
Q1:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"Largest: {a}, Smallest: {b}")
else:
    print(f"Largest: {b}, Smallest: {a}")
Q2:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print("Largest:", max(a, b, c), "Smallest:", min(a, b, c))
Q3:
a = int(input("Enter a number: "))
print("Even" if a % 2 == 0 else "Odd")
Q4:
a = int(input("Enter a number: "))
print("Divisible by 10" if a % 10 == 0 else "Not divisible by 10")
Q5:
a = int(input("Enter age: "))
print("Minor" if a < 18 else "Major")
Q6:
a = input("Enter a number: ")
print("Number of digits:", len(a))
Q7:
a = int(input("Enter a year: "))
print("Leap year" if a % 4 == 0 else "Not a leap year")
Q8:
a, b, c = map(int, input("Enter three angles: ").split())
print("Valid Triangle" if a + b + c == 180 else "Invalid Triangle")
Q9:
a = float(input("Enter a number: "))
print("Absolute value:", abs(a))
Q10:
l, b = map(float, input("Enter length and breadth: ").split())
print("Area is greater" if l * b > 2 * (l + b) else "Perimeter is greater")
Q11:
def straight_line(x1, y1, x2, y2, x3, y3):
   if (y2 - y1)(x3 - x2) == (y3 - y2)(x2 - x1):
       print("Points are on a straight line")
   else:
       print("Points are not on a straight line")

straight_line(0, 0, 1, 1, 2, 2)
Q12:
import math
x, y, r = map(int, input("Enter circle center and radius: ").split())
a, b = map(int, input("Enter point coordinates: ").split())
d = math.sqrt((a - x) ** 2 + (b - y) ** 2)
print("Inside Circle" if d < r else "On Circle" if d == r else "Outside Circle")
Q13:
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
n = int(input("Enter a number (0-19): "))
print(words[n] if 0 <= n <= 19 else "Out of range")
Q14:
def marks_grade(m1, m2, m3):
   def grade(m):
       if m == "Absent":
           return "NA"
       m = int(m)
       if m <= 39:
           return "F"
       elif m <= 44:
           return "P"
       elif m <= 49:
           return "C"
       elif m <= 54:
           return "B"
       elif m <= 59:
           return "B+"
       elif m <= 69:
           return "A"
       elif m <= 79:
           return "A+"
       else:
           return "O"

   if m1 == "Absent" or m2 == "Absent" or m3 == "Absent":
       print("One or more subjects absent")
       return
   m1, m2, m3 = int(m1), int(m2), int(m3)
   total = m1 + m2 + m3
   avg = total / 3
   print("Total:", total)
   print("Average:", avg)

   if m1 <= 39 or m2 <= 39 or m3 <= 39:
       print("Result: Fail")
   else:
       print("Result: Pass")

   print("Grades:", grade(m1), grade(m2), grade(m3))

marks_grade("65", "75", "80")
