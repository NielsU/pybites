from collections import Counter

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    # records_for_year = filter(lambda x: x["year"] == year,data)

    automakers = [item["automaker"] for item in data if item["year"] == year]
    automaker_counter = Counter()
    automaker_counter.update(automakers)
    return automaker_counter.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    return set(
        [
            item["model"]
            for item in data
            if item["year"] == year and item["automaker"] == automaker
        ]
    )

    """ Using filter doesnt make it more clear in my opinion, result filter still needs to get the model 
        values so its basically the same as without filter. 
        
    return set(
        [
            item["model"]
            for item in filter(
                lambda x: x["year"] == year and x["automaker"] == automaker, data
            )
        ]
    )
    """


if __name__ == "__main__":
    print(most_prolific_automaker(2005))
