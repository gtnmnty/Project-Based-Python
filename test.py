class Animal: pass
class Dog(Animal): pass

d = Dog()
print(type(d) == Animal)
print(isinstance(d, Animal))


min_valid = min_income is None or (min_income >= 0 and income >= min_income)
max_valid = max_income is None or income <= max_incom

if min_valid and max_valid:
    return True, None

# Other Option
if not (min_valid and max_valid):
    return True, None

if (min_income is None or min_income <= income) and (max_income is None or income <= max_income):
    return True, None

min_income = income_schema.get("min")
max_income = income_schema.get("max")

if (min_income is None or income >= min_income) and (max_income is None or income <= max_income):
    return True, None
else:
    return False, Error