import itertools


# Solution with creating slices, did not have to use isslice i think.
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""

    def rounded_avg(sequence):
        return round(sum(sequence) / len(sequence), 2)

    running_mean = []
    for i, _ in enumerate(sequence, start=1):
        slice = list(itertools.islice(sequence, i))
        running_mean.append(rounded_avg(slice))
    return running_mean


# solution using accumulate. Think this is more elegant.
def running_mean2(sequence):
    # get accummulated values in a list.
    accum = itertools.accumulate(sequence)

    # use index to calculate the avg/mean value for each item.
    return [round(value / (index), 2) for index, value in enumerate(accum, start=1)]
