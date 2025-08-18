def find_pairs(arr, K):
    #Write logic here!!
    return []

def main():
    # Take input
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    K = int(input("Enter value of K: "))

    # Call the function
    result = find_pairs(arr, K)

    # Print the result
    print("Pairs with sum", K, "are:", result)

if __name__ == "__main__":
    main()
