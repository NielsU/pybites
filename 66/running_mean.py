import itertools


# helper function for calculating average of a list
def rounded_avg(values: list[int]) -> float:
    return round(sum(values) / len(values), 2)


# Solution with creating slices, did not have to use isslice i think.
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""

    running_mean = []
    for i in range(1, len(sequence) + 1):
        slice = list(itertools.islice(sequence, i))
        running_mean.append(rounded_avg(slice))
    return running_mean


# rewritten to a list comprehension.
def running_mean2(sequence):
    return [rounded_avg(sequence[:i]) for i in range(1, len(sequence) + 1)]


# solution using accumulate. I think this is more opague/ diffcult to understand.
def running_mean3(sequence):
    # get accummulated values in a list.
    accum = itertools.accumulate(sequence)

    # use index to calculate the avg/mean value for each item.
    return [round(value / (index), 2) for index, value in enumerate(accum, start=1)]
