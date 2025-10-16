def main():
    print("Hello from a!")

def additional_function(a,b):
    print("This is an additional function in a.")
    print("It can be used for more complex logic.")
    a=a + b
    return a
if __name__ == "__main__":
    main()
    result = additional_function(5, 10)
    print(f"Result from additional_function: {result}")