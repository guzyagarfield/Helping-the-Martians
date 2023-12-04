import random

def find_cargo():
    total_weight = 713
    kilometer_marks = [0, 0, 0]

    while True:
        print("Enter the kilometer mark for each box (separated by space):")
        try:
            kilometer_marks = list(map(int, input().split()))
        except ValueError:
            print("Please enter valid integers.")

       
        for i in range(len(kilometer_marks)):
            kilometer_marks[i] += random.randint(-2, 2)

        current_weight = sum(kilometer_marks)

        if current_weight == total_weight:
            print("Congratulations! You found the cargo.")
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    print("Welcome to the Martian Cargo Finder!")
    find_cargo()