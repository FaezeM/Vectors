import torch

A = torch.tensor([
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
])

B = torch.tensor([
    [25, 15, 10],
    [20, 10, 5],
    [30, 20, 15]
])


# Calculate total sales for each product across all branches
total_sales = A + B

# Calculate overall income (total sales for all products combined)
overall_income = torch.sum(total_sales)

# Calculate incomes for each product listed on rows of sales_data_branch_a and sales_data_branch_b matrices
income_per_product_a = torch.sum(A, dim=1)  # Sum of each row (days) for Branch A
income_per_product_b = torch.sum(B, dim=1)  # Sum of each row (days) for Branch B

print(total_sales)
print(overall_income)
print(income_per_product_a)
print(income_per_product_b)
