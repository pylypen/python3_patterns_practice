def inBuilt_Iterator1():
    alphabets = [chr(i) for i in range(65, 91)]

    for alpha in alphabets:
        print(alpha, end=" ")
    print()


def inBuilt_Iterator2():
    alphabets = [chr(i) for i in range(97, 123)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


def alphabets_upto(letter):
    alphabets = [chr(i) for i in range(65, 91)]

    for alpha in alphabets[:ord(letter)-65 + 1]:
        yield alpha


if __name__ == "__main__":
    print("Note: Following code is the example of explicitly created Iterator method")
    alphabets_upto_K = alphabets_upto('K')
    alphabets_upto_M = alphabets_upto('M')

    for alpha in alphabets_upto_K:
        print(alpha, end=" ")

    print()

    for alpha in alphabets_upto_M:
        print(alpha, end=" ")

    print()
    print("Following code is the example of using in-built iterator method")

    inBuilt_Iterator1()
    inBuilt_Iterator2()
