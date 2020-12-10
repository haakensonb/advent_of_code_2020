# Is there a better way to do this rather than O(n^2)?
def part_1(data):
    for i in range(len(data)):
        for j in range(len(data)):
            data_sum = data[i] + data[j]
            if (data_sum == 2020):
                return (data[i] * data[j])


def part_2(data):
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                data_sum = data[i] + data[j] + data[k]
                if (data_sum == 2020):
                    return (data[i] * data[j] * data[k])


if __name__ == "__main__":
    data = [int(line.strip()) for line in open("input.txt")]
    print("Part 1:")
    print(part_1(data))
    print("Part 2:")
    print(part_2(data))
