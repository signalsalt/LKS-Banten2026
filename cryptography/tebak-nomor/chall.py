#!/usr/bin/env python3
import random
import os
import signal
import sys

FLAG = os.environ.get('FLAG', 'LKS{fake_flag}')

signal.alarm(30)

def main():
    print("=" * 42)
    print("  Selamat datang di Tebak Nomor! ")
    print("=" * 42)
    print()

    sys.stdout.flush()
    username = input("Masukkan username kamu: ").strip()

    if not username:
        print("Username tidak boleh kosong!")
        return

    random.seed(username)
    secret_number = random.randint(1000000000, 9999999999)

    print(f"\nHalo {username}!")
    print("Aku punya angka rahasia 10 digit.")
    print("Kamu cuma punya 1 kesempatan untuk menebak.\n")
    sys.stdout.flush()

    guess = input("Tebakan kamu: ").strip()

    try:
        if int(guess) == secret_number:
            print(f"\nBenar sekali! Kamu hebat!")
            print(f"Ini hadiahnya: {FLAG}")
        else:
            print(f"\nYahh salah! Mungkin lain kali ya.")
    except ValueError:
        print("Input tidak valid!")

    sys.stdout.flush()

if __name__ == '__main__':
    main()
