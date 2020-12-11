import re


HAIR_REGEX = r'#[0-9|a-f]{6}'
EYE_REGEX = r'(amb){1}|(blu){1}|(brn){1}|(gry){1}|(grn){1}|(hzl){1}|(oth){1}'


def is_valid_passport(passport, required):
    for field in required:
        # If any of the  fields can't be found, return False.
        if passport.find(field) == -1:
            return False
    return True


def is_valid_passport_multi_check(passport, required):
    if not is_valid_passport(passport, required):
        return False
    # Extract fields from passport.
    fields = passport.replace('\n', ' ').split(' ')
    fields = [x.split(':') for x in fields]
    # Must be a cleaner way to do this...
    # Should have used dict instead?
    for field in fields:
        if field[0] == 'byr':
            if not is_valid_year(field[1], 4, 1920, 2002):
                return False
        elif field[0] == 'iyr':
            if not is_valid_year(field[1], 4, 2010, 2020):
                return False
        elif field[0] == 'eyr':
            if not is_valid_year(field[1], 4, 2020, 2030):
                return False
        elif field[0] == 'hgt':
            if not is_valid_hgt(field[1]):
                return False
        elif field[0] == 'hcl':
            if not is_valid_regex_str(field[1], HAIR_REGEX):
                return False
        elif field[0] == 'ecl':
            if not is_valid_regex_str(field[1], EYE_REGEX):
                return False
        elif field[0] == 'pid':
            if not is_valid_pid(field[1]):
                return False
    return True


def is_valid_year(year, length, low_end, high_end):
    if len(year) != length:
        return False

    year = int(year)
    if year < low_end:
        return False
    elif year > high_end:
        return False
    return True


def is_valid_hgt(hgt):
    if hgt.find('cm') >= 0:
        num = int(hgt.split("cm")[0])
        return 150 <= num <= 193
    elif hgt.find('in') >= 0:
        num = int(hgt.split("in")[0])
        return 59 <= num <= 76
    return False


def is_valid_regex_str(input_str, regex_str):
    return (True if re.match(regex_str, input_str) else False)


def is_valid_pid(pid):
    return (len(pid) == 9)


if __name__ == "__main__":
    with open('input.txt') as f:
        passports = f.read().split("\n\n")
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print("Part 1:")
    valid_passports = sum([1 for x in passports if is_valid_passport(x, required)])
    print(valid_passports)
    print("Part 2:")
    part_2_valid_passports = sum([1 for x in passports if is_valid_passport_multi_check(x, required)])
    print(part_2_valid_passports)