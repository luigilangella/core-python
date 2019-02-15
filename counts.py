def count_upper_case(message):
    """This function count how many upper case
    letters are contained in a given message"""
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case(" ") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Upper Case"
assert count_upper_case("a") == 0, "One Lower Case"
assert count_upper_case("£$$%&") == 0, "Special Caracters"

print("All Test Have Passed!")


"""def count_upper_case(message):
    count = 0
    if message == "":
        return count 
    for c in message:
        if c.isupper():
            count += 1
        return count
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case(" ") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Upper Case"
assert count_upper_case("a") == 0, "One Lower Case"
assert count_upper_case("£$$%&") == 0, "Special Caracters"

print("All Test Passed!")"""