def get_bin_partition(sequence, input_str):
    if len(sequence) == 1:
        return sequence[0]
    
    left = 0
    right = len(sequence)-1
    mid = len(sequence) // 2 
    char = input_str[0]
    if char == "B" or char == "R":
        # Why is return needed here to properly clear call stack?
        return get_bin_partition(sequence[mid:right+1], input_str[1:])
    elif char == "F" or char == "L":
        return get_bin_partition(sequence[left:mid], input_str[1:])


def get_boarding_pass_id(sequence):
    row_str = sequence[0:7]
    col_str = sequence[7:]
    row = get_bin_partition(list(range(128)), row_str)
    col = get_bin_partition(list(range(8)), col_str)
    return ((row * 8) + col)

if __name__ == "__main__":
    boarding_passes = [line.strip() for line in open("input.txt")]
    print("Part 1:")
    print(max([get_boarding_pass_id(x) for x in boarding_passes]))
    print("Part 2:")
    seats = sorted([get_boarding_pass_id(x) for x in boarding_passes])
    # Look for gap in sorted seat list where next seat id is not just an increment of previous.
    # Your seat will be the seat that should have been in the gap.
    print([seats[i]+1 for i in range(len(seats)-1) if seats[i+1] != seats[i]+1][0])
