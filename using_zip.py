person_ages = {"bob": 20, "jim": 40}
person_city = {"jim": "Maarssen", "bob": "Houten"}


new_dict = {
    person_ages: cities for person_ages, cities in zip(person_ages, person_city)
}
print(new_dict)
