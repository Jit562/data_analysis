# 1. Calculate the average value of salary using csv.
import csv
import pandas as pd


def Average_salary(filename):

    total_salry = 0
    num_entries = 0

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            salary = float(row[3])
            total_salry += salary
            num_entries += 1

    average_salary =  total_salry / num_entries if num_entries > 0 else 0

    return average_salary

filename = "data.csv"

avg_salary = Average_salary(filename)

print("Average Salary: ", round(avg_salary))


# 1. Calculate the average value of salary using pandas library.

def average_sal(filename):
    df  = pd.read_csv(filename)
    avg_salary = df['Salary'].mean()

    return avg_salary

filename = 'data.csv'

avgs = average_sal(filename)

print("Average Salary: ", round(avgs))



#2.	Find the minimum and maximum values of Age using csv.

import csv

def find_min_max_age(filename):
    min_age = float('inf')
    max_age = float('-inf')

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  

        for row in csv_reader:
            age = int(row[1])  
            if age < min_age:
                min_age = age
            if age > max_age:
                max_age = age

    return min_age, max_age


filename = "data.csv"
min_age, max_age = find_min_max_age(filename)

print("Minimum Age:", min_age)
print("Maximum Age:", max_age)


#2.	Find the minimum and maximum values of Age using Pandas

def find_min_max_age(filename):

    df  = pd.read_csv(filename)

    min_age = df['Age'].min()
    max_age = df['Age'].max()

    return min_age, max_age

filename = 'data.csv'
min_age, max_age = find_min_max_age(filename)

print("Minimum age is: ", min_age)

print("maximum age is: ", max_age)



#3.	Count the number of rows that satisfy the condition that “age is 28 and Gender is Female” using csv

import csv

def count_rows_with_condition(filename, age_value, gender_value):
    count = 0

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            age = int(row[1])  
            gender = row[2]    

            if age == age_value and gender == gender_value:
                count += 1

    return count


filename = "data.csv"
age_value = 28
gender_value = "Female"
row_count = count_rows_with_condition(filename, age_value, gender_value)

print("Number of rows with age", age_value, "and gender", gender_value + ":", row_count)


#3.	Count the number of rows that satisfy the condition that “age is 28 and Gender is Female” using pandas


def count_rows_with_condition(filename, age_value, gender_value):

    df = pd.read_csv(filename)

    condition = (df['Age'] == age_value) & (df['Gender'] == gender_value)

    count = df[condition].shape[0]

    return count

filename = "data.csv"
age_value = 28
gender_value = "Female"
row_count = count_rows_with_condition(filename, age_value, gender_value)

print("Number of rows with age", age_value, "and gender", gender_value + ":", row_count)