import sys
import numpy as np

# Function to read input and emit key-value pairs
def read_input(file):
    for line in file:
        yield line.strip().split('\t')

# Reducer function
def reducer():
    # Initialize variables
    sum_x = sum_y = sum_xy = sum_x2 = count = 0
    for data in read_input(sys.stdin):
        _, x, y, x2, xy = map(float, data)
        # Update sums
        sum_x += x
        sum_y += y
        sum_x2 += x2
        sum_xy += xy
        count += 1
    
    # Debug statements
    print("Count:", count)
    print("Sum_x:", sum_x)
    print("Sum_y:", sum_y)
    print("Sum_x2:", sum_x2)
    print("Sum_xy:", sum_xy)
    
    # Handle division by zero
    if count * sum_x2 - sum_x**2 != 0:
        # Calculate coefficients (beta_0 and beta_1)
        beta_1 = (count * sum_xy - sum_x * sum_y) / (count * sum_x2 - sum_x**2)
        beta_0 = (sum_y - beta_1 * sum_x) / count
        # Output the coefficients
        print("Coefficients (beta_0, beta_1):", beta_0, beta_1)
    else:
        print("Cannot calculate coefficients: division by zero")

if __name__ == "__main__":
    reducer()
