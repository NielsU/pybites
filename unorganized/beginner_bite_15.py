names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""

    for index, name in enumerate(names):
        print(f"{index+1}. {name:<11}{countries[index]} ")


enumerate_names_countries()
