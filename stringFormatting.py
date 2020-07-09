def print_formatted(number):
    length = len(str(bin(number))) - 2
    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexadecimal = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]
        print(decimal.rjust(length), octal.rjust(length), hexadecimal.rjust(length), binary.rjust(length))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)