def get_groups_sum(groups):
    # Use set to get unique count for each group.
    return sum([len(set("".join(group))) for group in groups])

def get_intersect_sum(groups):
    total = 0
    # Need to get the count for intersection of answers across a group.
    for group in groups:
        # No need to intersect if just one group.
        # Start by turning into a list to seperate characters in an input str.
        if len(group) == 1:
            total += len(set(list(group[0])))
        else:
            intersect = set(list(group[0]))
            # Get intersection for first member of group with all other members.
            for i in range(1, len(group)):
                intersect = intersect.intersection(set(list(group[i])))
            total += len(intersect)
    return total

if __name__ == "__main__":
    # Get each group's data and then split on new lines within a group.
    groups = [group.strip().split("\n") for group in open("input.txt").read().split("\n\n")]
    print("Part 1:")
    print(get_groups_sum(groups))
    print("Part 2:")
    print(get_intersect_sum(groups))
