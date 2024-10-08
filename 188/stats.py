import os
import statistics
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DATA = "testfiles_number_loc.txt"
STATS = os.path.join(TMP, DATA)
if not os.path.isfile(STATS):
    urlretrieve(os.path.join(S3, DATA), STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
    returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    with open(data) as d:
        return [int(line.split()[0]) for line in d.readlines()]


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(
        count=None,
        min_=None,
        max_=None,
        mean=None,
        pstdev=None,
        pvariance=None,
        sample_count=None,
        sample_stdev=None,
        sample_variance=None,
    )

    stats["count"] = len(data)
    stats["min_"] = min(data)
    stats["max_"] = max(data)
    stats["mean"] = statistics.fmean(data)
    stats["pstdev"] = statistics.pstdev(data)
    stats["pvariance"] = statistics.pvariance(data)

    stats["sample_count"] = len(sample)
    stats["sample_stdev"] = statistics.stdev(sample)
    stats["sample_variance"] = statistics.variance(sample)

    return STATS_OUTPUT.format(**stats)


print(create_stats_report())
