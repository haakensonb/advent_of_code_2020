def get_formatted_input(file_path):
    data = [line.strip() for line in open(file_path)]
    results = []
    for line in data:
        line = line.split(" ")
        privs = line[0]
        letter = line[1][0]
        password = line[2]
        low_priv = int(privs.split("-")[0])
        high_priv = int(privs.split("-")[1])
        result = {
            "low_priv": low_priv,
            "high_priv": high_priv,
            "letter": letter,
            "password": password
        }
        results.append(result)
    return results


def is_valid_password_part_1(password):
    letter_count = password['password'].count(password['letter'])
    return password['low_priv'] <= letter_count <= password['high_priv']


def is_valid_password_part_2(password):
    # Minus 1 for zero indexing.
    letter_1 = password['password'][password['low_priv'] - 1]
    val_1 = True if (letter_1 == password['letter']) else False
    letter_2 = password['password'][password['high_priv'] - 1]
    val_2 = True if (letter_2 == password['letter']) else False
    # Exclusive OR. Only 1 val can be true.
    return val_1 ^ val_2


def part_1(passwords):
    return sum([is_valid_password_part_1(password) for password in passwords])


def part_2(passwords):
    return sum([is_valid_password_part_2(password) for password in passwords])


if __name__ == "__main__":
    print("Part 1:")
    passwords = get_formatted_input("input.txt")
    print(f"Valid passwords: {part_1(passwords)}")
    print("Part 2:")
    print(f"Valid passwords: {part_2(passwords)}")
