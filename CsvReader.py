import csv
# from csv package
def read_and_print_table():
    print(f"\n{'Name':<20} | {'Age':<5} | {'City':<15} | {'Notes':<20}")
    print("======================================================================")

    with open("utils/csv/leads.csv", mode="r", encoding="utf-8") as file:
        # csv.reader automatically parses commas inside quotes perfectly
        csv_reader = csv.reader(file)

        # Skip the header row using next()
        next(csv_reader)

        for row in csv_reader:
            # A row is a clean list of strings: [name, age, city, notes]
            name = row[0]
            age = row[1] if row[1] else "N/A"
            city = row[2]
            notes = row[3] if len(row) > 3 else ""

            print(f"{name:<20} | {age:<5} | {city:<15} | {notes:<20}")

def write_to_csv2():
    print("\n--- Add New Lead ---")
    name = input("Enter the name: ").strip()
    age = input("Enter the age: ").strip()
    city = input("Enter the city registered: ").strip()
    notes = input("Enter the notes: ").strip()

    with open("utils/csv/leads.csv", mode="a", encoding="utf-8", newline="") as file:
        # csv.writer handles all formatting rules automatically
        csv_writer = csv.writer(file)

        # Pass data as a single list. No manual formatting or \n needed!
        csv_writer.writerow([name, age, city, notes])

    print("\n✅ New Data successfully added using csv module!")
# ====================

def read_csv_naive():
    #f = open("utils/csv/leads.csv", "rt")
    # for i, line in enumerate(f, start=1):
    #     print(i, line)

    all_list=[]

    # 1. Open and read the file lines
    with open("utils/csv/leads.csv", "r") as file:
        lines = file.read().splitlines()

    # 2. Extract the header keys
    keys = lines[0].split(",")

    # 3. Used the zip() to save the values
    # based on their category / key
    for line in lines[1:]:
        val = line.split(",")
        row_dict = dict(zip(keys, val))

        all_list.append(row_dict)

    return all_list

def print_csv(saved_list):
    print(f"{'Name':<20} {'|':<3} {'Age':<5} {'|':<5} {'City':<16} {'|':<5} {'Notes':<17}")
    print("===================================================================================")
    for saved in saved_list:
        name = saved.get("name", "")
        age = saved.get("age", "") or "N/A"
        city = saved.get("city", "")
        notes = saved.get("notes", "")
        print(f"{name:<20} {'|':<3} {age:<5} {'|':<5} {city:<16} {'|':<5} {notes:<17}")

def write_to_csv():
    print("\n————— New Data —————")

    # Added to ensure age can only be used inside try block
    age = 0

    # 1. Validate Name (Cannot be empty or contain commas)
    while True:
        name = input("Enter the name: ").strip()
        if not name:
            print("Error: Name cannot be blank.")
        elif "," in name:
            print("Error: Commas are not allowed.")
        else:
            break

    # 2. Validate Age (Must be a valid integer number)
    while True:
        try:
            age_input = input("Enter the age: ").strip()
            if not age_input:
                print("Error: Age cannot be blank.")
                continue

            age = int(age_input)
            if age <= 0 or age > 120:
                print("Error: Please enter a realistic age (1-120).")
            else:
                break
        except ValueError:
            print("Error: Age must be a whole number (e.g., 25).")

    # 3. Validate City (Cannot be empty or contain commas)
    while True:
        city = input("Enter the city registered: ").strip()
        if not city:
            print("Error: City cannot be blank.")
        elif "," in city:
            print("Error: Commas are not allowed.")
        else:
            break

    # 4. Validate Notes (Optional, but still cannot contain commas)
    while True:
        notes = input("Enter the notes (Optional): ").strip()
        if "," in notes:
            print("Error: Commas are not allowed in notes.")
        else:
            break

    with open("utils/csv/leads.csv", "a", encoding="utf-8") as file:
        file.write(f"\n{name},{age},{city},{notes}")

    print("New Data successfully added!")


def main():
    print("Welcome to Database")
    print("What would you like to do?")
    print("1. Read the Database")
    print("2. Write into the Database")
    print("3. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            saved_list = read_csv_naive()
            print_csv(saved_list)
            #read_and_print_table()
        elif choice == 2:
            write_to_csv()
            #write_to_csv2()
        elif choice == 3:
            print("RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()