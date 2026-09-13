import csv


def interpret(result):
    # Interpret the result for the user
    if result > 0.7:
        print("Interpretation: Strong Positive Correlation")
    elif result > 0.3:
        print("Interpretation: Moderate Positive Correlation")
    elif result > -0.3:
        print("Interpretation: Weak / No Correlation")
    elif result > -0.7:
        print("Interpretation: Moderate Negative Correlation")
    else:
        print("Interpretation: Strong Negative Correlation")

def compute_correlation(emp_list, col_a, col_b):
    if not emp_list: return "List is either empty or corrupted"

    x_vals = []
    y_vals = []

    # Append the valid columns
    for emp_info in emp_list.values():
        x = emp_info.get(col_a, "")
        y = emp_info.get(col_b, "")

        if x and y and x.replace(".", "", 1).isdigit() and y.replace(".", "", 1).isdigit():
            x_vals.append(float(x))
            y_vals.append(float(y))
        else:
            print(f"Skipping {emp_info.get('name', 'Unknown')}: invalid data in {col_a} or {col_b}")

    if len(x_vals) < 2:
        return "Not enough valid paired data points"

    # finds the mean of each list
    mean_x = find_mean(x_vals)
    mean_y = find_mean(y_vals)

    # Declare numerator, sum of each square roots
    numerator = 0.0
    sum_sq_x = 0.0
    sum_sq_y = 0.0

    for x, y in zip(x_vals, y_vals):
        diff_x = x - mean_x
        diff_y = y - mean_y
        numerator += diff_x * diff_y
        sum_sq_x += diff_x ** 2
        sum_sq_y += diff_y ** 2

    denominator = (sum_sq_x ** 0.5) * (sum_sq_y ** 0.5)
    if denominator == 0.0: return "Can't divide with 0"

    return numerator / denominator


# Finds the average after computing the sum of all
# values divided by the length of n
def find_mean(filtered_list):
    return sum(filtered_list) / len(filtered_list)

# Finds
def find_std_dev(f_list):
    if len(f_list) < 2: return 0.0

    m = find_mean(f_list)
    squared_diffs = [(x - m) ** 2 for x in f_list]
    divisor = len(f_list) - 1 if len(f_list) != 0 else 1
    res = (sum(squared_diffs) / divisor) ** 0.5

    return res

def column_stats(emp_list, column_name):
    if not emp_list: return "Employee list is empty or corrupted"

    # converts the value from string to float if the column exist in the dictionary
    # and if the number is convertable into float after
    # removing the first '.' and if isdigit() returns True
    # filtered_list = [
    #     float(emp_info[column_name])
    #     for emp_info in emp_list.values()
    #     if column_name in emp_info and emp_info[column_name]
    #         .replace(".", "", 1).isdigit()
    # ]

    filtered_list = []
    for emp_id, emp_info in emp_list.items():
        val = emp_info[column_name]
        if not (val and val.replace(".", "", 1).isdigit()):
            print(f"Error: {column_name} value on {emp_info["name"]} is not valid or empty")
        else: filtered_list.append(float(val))

    if not filtered_list: return 0.0, 0.0

    # call the mean method with filtered_list as argument
    mean_val = find_mean(filtered_list)

    # call the std_dev method and return the value
    std_dev_val = find_std_dev(filtered_list)

    return mean_val, std_dev_val


def load_csv_file():
    emp_list = {}

    try:
        with open("utils/csv/employees.csv", mode="r", encoding="utf_8") as file:
            # DirectReader automatically consider the first line as headers and skip it
            lines = csv.DictReader(file)

            for row in lines:
                # Removes the id column and make it as key main dict
                emp_id = row.pop("id")

                # Saves the line to emp_list with the emp_id as index
                emp_list[emp_id] = row

        #print(emp_list)
        return emp_list

    except FileNotFoundError:
        return "File is either missing or corrupted."


def main():
    print("Welcome to Database")
    print("What would you like to do?")
    print("1. Load CSV")
    print("2. Compute Stats")
    print("3. Determine Correlation")
    print("4. Exit")

    db_data = load_csv_file()

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print(db_data)
        elif choice == 2:
            print("\nAvailable Numeric Columns:")
            print("- Age\n- Years of EXP\n- Salary\n- Performance Score")

            while True:
                column = input("\nWhat column would you like to get: ").strip().lower()
                if column.isdigit() or column == "":
                    print("Invalid Input")
                    continue

                mean, std_dev = column_stats(db_data, column)
                print(f"\n--- Stats for {column} ---")
                print(f"Peak (Mean): {mean:.2f}")
                print(f"Spread (Std Dev): {std_dev:.2f}")

        elif choice == 3:
            print("\nAvailable Numeric Columns:")
            print("- Age\n- Years of EXP\n- Salary\n- Performance Score")

            # Get first column
            col1 = input("\nEnter first column name: ").strip().lower()
            # Get second column
            col2 = input("Enter second column name: ").strip().lower()

            # Get the values by key. Starts with Age column
            #
            sample_row = next(iter(db_data.values()), {})
            valid_columns = sample_row.keys()

            if col1 not in valid_columns:
                print(f"Error: '{col1}' is not a valid column. Available: {list(valid_columns)}")
            elif col2 not in valid_columns:
                print(f"Error: '{col2}' is not a valid column. Available: {list(valid_columns)}")
            elif col1 == col2:
                print("Cannot correlate a column with itself.")
            else:
                result = compute_correlation(db_data, col1, col2)

                if isinstance(result, str):
                    print(result)
                else:
                    print(f"\nCorrelation between '{col1}' and '{col2}': {result:.4f}")
                    interpret(result)


        elif choice == 4:
            print("RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()