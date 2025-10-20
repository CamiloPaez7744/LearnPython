languages = ["Python", "JavaScript", "C++"]

print(languages[-1])

languages.append("Java")
print(languages)

for lang in languages:
    print("I want to learn " + lang)

coordinates = (10.0, 20.0)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# sets
unique_languages = {"Python", "JavaScript", "C++", "Python"}
print(unique_languages)
unique_languages.add("Java")
print(unique_languages)
unique_languages.remove("C++")
print(unique_languages)
unique_languages.discard("Ruby")  # No error if not found
print(unique_languages)
unique_languages.clear()
print(unique_languages)
unique_languages.clear()  # No error if already empty

#union, intersection and difference
set_a = {"Python", "JavaScript", "C++"}
set_b = {"Java", "C#", "JavaScript"}
set_union = set_a.union(set_b)
set_intersection = set_a.intersection(set_b)
set_difference = set_a.difference(set_b)
print("Union:", set_union)
print("Intersection:", set_intersection)
print("Difference:", set_difference)

# symmetric difference
set_sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", set_sym_diff)

# dictionaries
student = {
    "name": "Dan",
    "age": 38,
    "courses": ["Math", "Science"]
}