from itertools import combinations

def first_invalid(data, preamble_len):
    for i in range(preamble_len, len(data)-1):
        # Grab the current value
        cur_val = data[i]
        # And check it against all combinations of the previous values.
        prev_vals = data[i-preamble_len:i]
        comb_vals = list(combinations(prev_vals, 2))
        sum_vals = set([sum(x) for x in comb_vals])
        if cur_val not in sum_vals:
            return cur_val


def find_contiguous_sum(data, target_val):
    start_idx = 0
    end_idx = 0
    total = 0
    i = 0
    keep_going = True
    while keep_going:
        if i >= len(data):
            keep_going = False

        total += data[i]
        end_idx += 1
        i += 1

        # If the current total is greater than the target val
        # then the total and range we are checking must be reset.
        # This is due to the fact that values must be contiguous.
        if total > target_val:
            total = 0
            start_idx += 1
            i = start_idx

        # If a range if found that sums to the target val
        if total == target_val:
            end_idx = i
            # Then return the sum of the min and max vals in this range
            data_range = data[start_idx:end_idx]
            result = min(data_range)
            result += max(data_range)
            return result
        


if __name__ == "__main__":
    data = [int(line.strip()) for line in open("input.txt")]
    print("Part 1:")
    part1_result = first_invalid(data, 25)
    print(part1_result)
    print("Part 2:")
    print(find_contiguous_sum(data, part1_result))
