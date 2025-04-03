#Rob Gouhin
#CIT 163
#Mini Project 2
#April 2, 2024

import os 

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the filenames
personnel_file = os.path.join(current_directory, "personnel.txt")
timeclock_file = os.path.join(current_directory, "timeclock.txt")

# Ensure both files exist before proceeding
if not os.path.exists(personnel_file):
    print(f"Error: Missing file '{personnel_file}'.")
    exit(1)

if not os.path.exists(timeclock_file):
    print(f"Error: The required timeclock file '{timeclock_file}' for payroll processing is missing.")
    exit(1)
output_file = "payroll.txt"  # Output file as specified in the pseudocode

# Create a dictionary to store personnel data
personnel = {}

# Read personnel.txt into the dictionary
with open(personnel_file, 'r') as f:
    for line in f:
        # Split each line into employee_number, name, and pay_rate
        parts = line.strip().split(',')
        if len(parts) != 3:
            print(f"Warning: Malformed line in personnel file: {line.strip()}")
            continue
        employee_number = parts[0]  # Kept as string for consistency
        name = parts[1]
        try:
            pay_rate = float(parts[2])  # Convert pay_rate to float
        except ValueError:
            print(f"Warning: Invalid pay rate in line: {line.strip()}")
        parts = line.strip().split(',')
        if len(parts) != 3:
            print(f"Error: Invalid line format in timeclock file: '{line.strip()}'. Skipping this line.")
            continue
        employee_number = parts[0]
        hours_worked = int(parts[1])  # Convert to integer
        try:
            shift = int(parts[2])  # Convert to integer
        except ValueError:
            print(f"Warning: Invalid shift value in line: '{line.strip()}'. Skipping this line.")
            continue
with open(timeclock_file, 'r') as timeclock, open(output_file, 'w') as payroll:
    for line in timeclock:
        try:
            hours_worked = int(parts[1])  # Convert to integer
            shift = int(parts[2])         # Convert to integer
        except ValueError:
            print(f"Warning: Invalid hours worked or shift in line: {line.strip()}")
            continue
        employee_number = parts[0]
        hours_worked = int(parts[1])  # Convert to integer
        shift = int(parts[2])         # Convert to integer

        # Check if the employee exists in personnel data
        if employee_number not in personnel:
            print(f"Warning: Employee number '{employee_number}' not found in personnel data. Skipping this record.")
            continue
        if employee_number in personnel:
            # Adjust pay rate for shift 3 using a separate variable
            adjusted_pay_rate = pay_rate
            if shift == 3:
                adjusted_pay_rate += 1.0
            # Adjust pay rate for shift 3
            if shift == 3:
                pay_rate += 1.0

            # Precompute overtime rate
            overtime_rate = pay_rate * 1.5

            # Calculate gross pay based on hours worked
            if hours_worked <= 40:
                gross_pay = hours_worked * pay_rate
            else:
                gross_pay = 40 * pay_rate + (hours_worked - 40) * overtime_rate
                gross_pay = 40 * pay_rate + (hours_worked - 40) * pay_rate * 1.5

            # Format gross pay to two decimal places
            gross_pay_formatted = f"{gross_pay:.2f}"

            # Write the record to payroll.txt
            payroll.write(f"{employee_number},{name},{gross_pay_formatted}\n")

print(f"Payroll processing complete. Results written to {output_file}.")