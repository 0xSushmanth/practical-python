# pcost.py
#
# Exercise 1.27
# import os

# def portfolio_cost(file_path: str) -> float:
#     '''
#     Calculate the total cost of a portfolio based on data from a CSV file.

#     Args:
#         file_path (str): The path to the CSV file.

#     Returns:
#         float: Total cost of the portfolio.
#     '''
#     # Initialize the cost list
#     cost = []

#     # Open the CSV file
#     with open(file_path, "r") as f:
#         # Skip the header row
#         next(f)

#         # Iterate over each row in the CSV
#         for line in f:
#             # Split the line by comma to get the values
#             row = line.strip().split(",")

#             # Extract shares and price from the row
#             shares = int(row[1])
#             price = float(row[2])

#             # Calculate the cost and append it to the cost list
#             cost.append(shares * price)

#     # Calculate the total cost
#     total = sum(cost)
#     return total

# # Call the function with the file path
# file_path = "/home/sushmanth/practical-python/Work/Data/portfolio.csv"
# total_cost = portfolio_cost(file_path)
# print("Total portfolio cost:", total_cost)

# pcost.py
#
# Exercise 1.27
import os
import csv

def portfolio_cost(file_path: str) -> float:
    '''
    Calculate the total cost of a portfolio based on data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        float: Total cost of the portfolio.
    '''
    # Initialize the cost
    total_cost = 0

    # Open the CSV file
    with open(file_path, "r") as f:
        # Create a CSV reader
        reader = csv.reader(f)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV
        for row in reader:
            # Extract shares and price from the row
            shares = int(row[1])
            price = float(row[2])

            # Calculate the cost and add it to the total cost
            total_cost += shares * price

    return total_cost

# Call the function with the file path
file_path = "/home/sushmanth/practical-python/Work/Data/portfolio.csv"
total_cost = portfolio_cost(file_path)
print("Total portfolio cost:", total_cost)
