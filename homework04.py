#!/usr/bin/env python3
"""
Homework Assignment 025: Python Fundamentals & Data Types
Student Name: [Your Full Name]
Student ID: [Your Student ID]
Date: [Submission Date]
Course: CSC 121 - Introduction to Python and Data Science

INSTRUCTIONS: 
- Replace [Your Full Name], [Your Student ID], and [Submission Date] above
- Complete each section below
- Keep all section headers and question numbers exactly as shown
- Add your answers/code after each question
- Do not delete any section markers or question numbers
"""

# ============================================================================
# SECTION 1: UNDERSTANDING DATA TYPES & OPERATIONS (50 points)
# ============================================================================

print("=== SECTION 1: UNDERSTANDING DATA TYPES & OPERATIONS ===")

# Question 1 (5 points)
# What will this expression evaluate to?
# result = 17 // 3
# a) 5.67
# b) 5
# c) 6
# d) 5.0
#
# Your answer:
question_1_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 1 answer:", question_1_answer)

# Question 2 (5 points)
# What data type will this variable be?
# value = 3.0 + 2
# a) int
# b) float
# c) str
# d) bool
#
# Your answer:
question_2_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 2 answer:", question_2_answer)

# Question 3 (5 points)
# What will this f-string produce?
# price = 15.678
# print(f"Cost: ${price:.2f}")
#
# a) Cost: $15.678
# b) Cost: $15.68
# c) Cost: $15.67
# d) Cost: $price:.2f
#
# Your answer:
question_3_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 3 answer:", question_3_answer)

# Question 4 (5 points)
# What will this code output?
# name = "Python"
# print(f"{name:>10}")
#
# a) "Python    "
# b) "    Python"
# c) "Python"
# d) This will cause an error
#
# Your answer:
question_4_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 4 answer:", question_4_answer)

# Question 5 (5 points)
# What is the result of: bool("")
# a) True
# b) False
# c) ""
# d) This will cause an error
#
# Your answer:
question_5_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 5 answer:", question_5_answer)

# Question 6 (5 points)
# True or False: The expression (5 > 3) and (2 < 1) evaluates to True.
#
# Your answer:
question_6_answer = "false"  # Replace with True or False
print("Question 6 answer:", question_6_answer)

# Question 7 (5 points)
# What will str(42) + str(8) produce?
# a) 50
# b) "50"
# c) "428"
# d) 428
#
# Your answer:
question_7_answer = "c"  # Replace with your answer (a, b, c, or d)
print("Question 7 answer:", question_7_answer)

# Question 8 (5 points)
# What is the result of: 2 ** 3
# a) 6
# b) 8
# c) 9
# d) 23
#
# Your answer:
question_8_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 8 answer:", question_8_answer)

# Question 9 (5 points)
# True or False: int(3.9) equals 4.
#
# Your answer:
question_9_answer = "False"  # Replace with True or False
print("Question 9 answer:", question_9_answer)

# Question 10 (5 points)
# What will this expression evaluate to?
# result = 15 % 4
# a) 3.75
# b) 3
# c) 4
# d) 1
#
# Your answer:
question_10_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 10 answer:", question_10_answer)

# ============================================================================
# SECTION 2: PRACTICAL PROGRAMMING (50 points)
# ============================================================================

print("\n=== SECTION 2: PRACTICAL PROGRAMMING ===")

# ----------------------------------------------------------------------------
# Part A: Personal Budget Calculator (20 points)
# ----------------------------------------------------------------------------

print("\n--- Part A: Personal Budget Calculator ---")

# Task 1: Budget Analysis (20 points)
print("\nTask 1: Budget Analysis")

# REQUIREMENTS:
# Create a personal budget calculator using variables and calculations:
#
# 1. Income Variables:
#    - monthly_salary (your estimated dream monthly income as a number)
#    - side_income (additional income like part-time job, set to 0 if none)
#    - total_monthly_income (calculate: monthly_salary + side_income)
#
# 2. Expense Variables:
#    - rent_cost (estimated monthly rent/housing cost)
#    - food_cost (estimated monthly food expenses)
#    - transportation_cost (gas, bus pass, etc.)
#    - entertainment_cost (movies, games, etc.)
#    - other_expenses (miscellaneous expenses)
#    - total_monthly_expenses (calculate sum of all expense categories)
#
# 3. Analysis Variables:
#    - monthly_savings (calculate: total_monthly_income - total_monthly_expenses)
#    - savings_percentage (calculate: monthly_savings / total_monthly_income * 100)
#    - yearly_savings (calculate: monthly_savings * 12)
#
# 4. Budget Display:
#    - Use f-strings with proper formatting (2 decimal places for money, 1 for percentages)
#    - Create a professional-looking budget report
#    - Include recommendations based on savings percentage
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

monthly_salary = 6000
side_income = 500
total_monthly_income = monthly_salary + side_income

rent_cost = 1000
food_cost = 600
transportation_cost = 400
entertainment_cost = 300
other_expenses = 250
total_monthly_expenses = rent_cost + food_cost + transportation_cost + entertainment_cost + other_expenses

monthly_savings = total_monthly_income - total_monthly_expenses
savings_percentage = (monthly_savings / total_monthly_income) * 100
yealy_savings = monthly_savings * 12

print("\n==== Personal Budget Report ====")
print(f"Total Monthly Income: ${total_monthly_income:,.2f}")
print(f"Total Monthly Expenses: ${total_monthly_expenses:,.2f}")
print(f"Monthly Savings: ${monthly_savings:,.2f}")
print(f"Sacings Percentage: ${savings_percentage:,.2f}")
print(f"Projected Yearlt Savings: ${yealy_savings:,.2f}")
if savings_percentage >=20:
    print("You have a great of your income saved")
elif 10 <= savings_percentage >= 20:
    print("Tou could save more")
else:
    print("Your expenses are taking up most of your income.")        
# ----------------------------------------------------------------------------
# Part B: Unit Conversion Calculator (15 points)
# ----------------------------------------------------------------------------

print("\n--- Part B: Unit Conversion Calculator ---")

# Task 2: Measurement Conversions (15 points)
print("\nTask 2: Measurement Conversions")

# REQUIREMENTS:
# Create a unit conversion system for various measurements:
#
# 1. Distance Conversions:
#    - distance_miles (a distance in miles, use any reasonable number)
#    - distance_kilometers (convert miles to kilometers: miles * 1.60934)
#    - distance_feet (convert miles to feet: miles * 5280)
#    - distance_meters (convert kilometers to meters: kilometers * 1000)
#
# 2. Temperature Conversions:
#    - temp_fahrenheit (a temperature in Fahrenheit)
#    - temp_celsius (convert F to C: (fahrenheit - 32) * 5/9)
#    - temp_kelvin (convert C to Kelvin: celsius + 273.15)
#
# 3. Weight Conversions:
#    - weight_pounds (a weight in pounds)
#    - weight_kilograms (convert pounds to kg: pounds * 0.453592)
#    - weight_ounces (convert pounds to ounces: pounds * 16)
#
# 4. Formatted Display:
#    - Use f-strings with appropriate decimal places
#    - Create organized conversion tables
#    - Include unit labels in your output
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

distance_miles = 10
distance_kilometers = distance_miles * 1.60934
distance_feet = distance_miles * 5200
distance_meters = distance_kilometers * 1000

print("\nDistance Conversions:")
print(f"{distance_miles} miles = {distance_kilometers:.2f} km ")
print(f"{distance_miles} miles = {distance_feet:.2f} ft ")
print(f"{distance_kilometers} km = {distance_meters:.2f} meters ")

temp_fahrenheit = 98.6
temp_celsius = (temp_fahrenheit - 32) * 5/9
temp_kelvin = temp_celsius + 273.15

print("\nTemperature Conversions:")
print(f"{temp_fahrenheit}F = {temp_celsius:.2f}C")
print(f"{temp_celsius:.2f}C = {temp_kelvin:.2f}K")

weight_pounds = 150
weight_kilograms = weight_pounds * 0.453592
weight_ounces = weight_pounds * 16

print("\nWeight Conversions:")
print(f"{weight_pounds} lbs = {weight_kilograms:.2f} kg")
print(f"{weight_pounds} lbs ={weight_ounces:.2f} oz")
# ----------------------------------------------------------------------------
# Part C: Student Grade Analyzer (15 points)
# ----------------------------------------------------------------------------

print("\n--- Part C: Student Grade Analyzer ---")

# Task 3: Grade Calculations (15 points)
print("\nTask 3: Grade Calculations")

# REQUIREMENTS:
# Create a grade analysis system for a student's performance:
#
# 1. Individual Grades (use realistic grade values 0-100):
#    - exam1_score, exam2_score, exam3_score (three exam scores)
#    - quiz1_score, quiz2_score, quiz3_score, quiz4_score (four quiz scores)
#    - homework_score (average homework grade)
#    - participation_score (participation grade)
#
# 2. Category Averages:
#    - exam_average (average of the three exams)
#    - quiz_average (average of the four quizzes)
#
# 3. Weighted Final Grade:
#    - final_grade (calculate using these weights:)
#      * Exams: 50% (exam_average * 0.5)
#      * Quizzes: 25% (quiz_average * 0.25)
#      * Homework: 15% (homework_score * 0.15)
#      * Participation: 10% (participation_score * 0.1)
#
# 4. Grade Analysis:
#    - letter_grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
#    - points_to_next_grade (how many points needed to reach next letter grade)
#    - gpa_points (A=4.0, B=3.0, C=2.0, D=1.0, F=0.0)
#
# 5. Professional Display:
#    - Use f-strings with proper formatting
#    - Create a detailed grade report
#    - Include improvement suggestions
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

exam1_score = 94
exam2_score = 76
exam3_score = 85

quiz1_score = 85
quiz2_score = 93
quiz3_score = 73
quiz4_score = 65

homework_score = 87
participation_score = 100

exam_average = (exam1_score + exam2_score + exam3_score) / 3
quiz_average = (quiz1_score + quiz2_score + quiz3_score + quiz4_score) / 4

final_grade = (exam_average * 0.5 + quiz_average * 0.25 + homework_score * 0.15 + participation_score * 0.1)

if final_grade >=90:
    letter_grade = "A"
    points_to_next_grade = 0
    gpa_points = 4.0
elif final_grade >= 80:
    letter_grade = "B"
    points_to_next_grade = 90 - final_grade
    gpa_points = 3.0
elif final_grade >= 70:
    letter_grade = "C"
    points_to_next_grade =  80 - final_grade
    gpa_points = 2.0
elif final_grade >= 60:
    letter_grade = "D"
    points_to_next_grade = 70 - final_grade
    gpa_points = 1.0
else: 
    letter_grade = "F"
    points_to_next_grade = 60 - final_grade
    gpa_points = 0.0


print(f"Exam Average: {exam_average:.2f}") 
print(f"Quiz Average: {quiz_average:.2f}")
print(f"Homework Score: {homework_score:.2f}")  
print(f"Participation Score: {participation_score:.2f}")  
print(f"Final Grade: {final_grade:.2f}")  
print(f"Letter Grade: {letter_grade}")  
print(f"Points to Next Grade: {points_to_next_grade:.2f}")  
print(f"GPA Points: {gpa_points}")  

if points_to_next_grade > 0:
    print("You need some improvement")
else:
    print("Great Job!")    
                    
# ============================================================================
# BONUS SECTION: ADVANCED CALCULATIONS (5 points)
# ============================================================================

print("\n=== BONUS SECTION: ADVANCED CALCULATIONS ===")

# Task 4: Compound Interest Calculator (5 points)
print("\nTask 4: Compound Interest Calculator")

# REQUIREMENTS:
# Create a compound interest calculator for savings/investment:
#
# 1. Investment Variables:
#    - principal_amount (initial investment amount)
#    - annual_interest_rate (as a decimal, e.g., 0.05 for 5%)
#    - years_invested (number of years)
#    - compounds_per_year (how many times interest compounds per year, e.g., 12 for monthly)
#
# 2. Calculations:
#    - final_amount (use compound interest formula: P(1 + r/n)^(nt))
#      where P=principal, r=annual rate, n=compounds per year, t=years
#    - total_interest_earned (final_amount - principal_amount)
#    - effective_annual_rate (final_amount / principal_amount) ** (1/years_invested) - 1
#
# 3. Investment Analysis:
#    - monthly_contribution_needed (if you wanted to reach a specific goal)
#    - doubling_time (approximately 72 / (annual_interest_rate * 100))
#
# 4. Professional Report:
#    - Use advanced f-string formatting
#    - Include currency formatting and percentages
#    - Create investment projections
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

principal_amount = 5000
annual_interest_rate = 0.05
years_invested = 10
compounds_per_year = 12

final_amount = principal_amount * (1 + annual_interest_rate/compounds_per_year) ** (compounds_per_year*years_invested)
total_interest_earned = final_amount - principal_amount
effective_annual_rate = (final_amount / principal_amount) ** (1/years_invested) - 1

goal_amount = 10000
monthly_contribution_needed = (goal_amount - principal_amount) / (years_invested * 12)
doubling_time = 72 / (annual_interest_rate * 100)


print(f"Initial Investment: ${principal_amount:,.2f}")
print(f"Annual Interest Rate: {annual_interest_rate*100:.2f}%")
print(f"Years Invested: {years_invested}")
print(f"Compounds per Year: {compounds_per_year}")
print(f"Final Amount: ${final_amount:,.2f}")
print(f"Total Interest Earned: ${total_interest_earned:,.2f}")
# ============================================================================
# REFLECTION SECTION (Bonus - 3 points)
# ============================================================================

print("\n=== REFLECTION SECTION ===")

# Answer these reflection questions by replacing the placeholder text:
reflection_1 = "What I found most challenging was getting thef strings to work properly."
reflection_2 = "I could see myself using this to help budget my future income."
reflection_3 = "The one I found the most interesting was the compound interest calculations since if I were to use this in the future, the interest calcuations seem like the most useful."

print("Most challenging aspect:", reflection_1)
print("Real-world applications:", reflection_2)
print("Most interesting calculation:", reflection_3)

# ============================================================================
# END OF HOMEWORK ASSIGNMENT
# ============================================================================

print("\n=== HOMEWORK ASSIGNMENT COMPLETED ===")
print("All sections completed successfully!")
