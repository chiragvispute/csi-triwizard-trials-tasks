def move_zeros(arr):
    # Write logic here!!
    return arr

def main():
    # Take input
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    # Call the function
    result = move_zeros(arr)

    # Print the result
    print("Array after moving zeros:", result)

if __name__ == "__main__":
    main()
