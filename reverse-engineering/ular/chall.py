import sys

def check_flag(user_input):
    key = [0x13, 0x37, 0x42, 0x55]
    encrypted = [
        95, 124, 17, 46, 112, 3, 33, 100, 125, 80,
        29, 54, 114, 84, 43, 100, 34, 80, 29, 59,
        114, 80, 35, 10, 125, 86, 37, 97, 110
    ]

    if len(user_input) != len(encrypted):
        return False

    for i in range(len(user_input)):
        if ord(user_input[i]) ^ key[i % len(key)] != encrypted[i]:
            return False

    return True

def main():
    user_input = input("Input: ")
    if check_flag(user_input):
        print("Benar")
    else:
        print("Salah")

if __name__ == "__main__":
    main()
