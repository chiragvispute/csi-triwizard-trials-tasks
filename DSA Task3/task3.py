def is_palindrome(arr):
    # TODO: Write logic here
    return False

def main():
    # Take input
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    # Call the function
    result = is_palindrome(arr)

    # Print the result
    if result:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

if __name__ == "__main__":
    main()
