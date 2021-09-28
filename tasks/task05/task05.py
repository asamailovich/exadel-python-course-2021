def create_user(name, surname, age=42, **kwargs) -> dict:
    res = {"name": name, "surname": surname, "age": age, "extra": kwargs}
    return res


assert create_user("John", "Doe") == \
       {
           'name': 'John',
           'surname': 'Doe',
           'age': 42,
           'extra': {}
       }
assert create_user("John", "Doe", age=65) == \
       {
           'name': 'John',
           'surname': 'Doe',
           'age': 65,
           'extra': {}
       }
assert create_user("John", "Doe", age=66, occupation="physicist", won_nobel=True) == \
       {
           'name': 'John',
           'surname': 'Doe',
           'age': 66,
           'extra': {
               'occupation': 'physicist',
               'won_nobel': True
           }
       }
