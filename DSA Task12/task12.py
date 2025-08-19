def count_occurrences(arr, k):
    # TODO: Write logic to count how many times k appears in arr
    pass

def main():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    k = int(input("Enter the number to count: "))
    result = count_occurrences(arr, k)
    print("Count:", result)

if __name__ == "__main__":
    main()
