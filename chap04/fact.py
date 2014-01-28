
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n -1)



def main():
    num = 5
    print(fact(num))


if __name__ == "__main__":
    main()
