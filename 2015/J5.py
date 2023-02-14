if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    count = 0
    if n < k:
        print('0')
        exit()

    for i in range(1, n // k + 1):
        remainder_people = k
        remainder_pieces = n
        for j in range(k):
            if remainder_people * i > remainder_pieces:
                break

