def birthday_cake_candles(candles):
    # TODO: Write logic to count tallest candles
    pass

def main():
    n = int(input("Enter number of candles: "))
    candles = list(map(int, input("Enter candle heights: ").split()))
    
    result = birthday_cake_candles(candles)
    print("Tallest candle count:", result)

if __name__ == "__main__":
    main()
