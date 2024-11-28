def display_counter(value):
    print(f"\nCurrent Counter Value: {value}\n")

def main():
    counter = 0
    while True:
        print("Options:")
        print("1. Increment Counter")
        print("2. Decrement Counter")
        print("3. Reset Counter")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            counter += 1
        elif choice == "2":
            counter -= 1
        elif choice == "3":
            counter = 0
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue

        display_counter(counter)

if __name__ == "__main__":
    main()
