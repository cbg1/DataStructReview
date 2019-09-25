def fibona(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibona(n - 1) + fibona(n - 2)


if __name__ == '__main__':
    print(fibona(700))
