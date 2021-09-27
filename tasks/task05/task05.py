def create_user(name, surname, **kwargs) -> dict:
    res = {name: name, surname: surname, "age": 42, "extra": {}}
    for key, value in kwargs.items():
        if key == 'age':
            res[key] = value
        else:
            res["extra"][key] = value
    return res


assert create_user("John", "Doe") == \
       {
           'John': 'John',
           'Doe': 'Doe',
           'age': 42,
           'extra': {}
       }
assert create_user("John", "Doe", age=65) == \
       {
           'John': 'John',
           'Doe': 'Doe',
           'age': 65,
           'extra': {}
       }
assert create_user("John", "Doe", age=66, occupation="physicist", won_nobel=True) == \
       {
           'John': 'John',
           'Doe': 'Doe',
           'age': 66,
           'extra': {
               'occupation': 'physicist',
               'won_nobel': True
           }
       }
