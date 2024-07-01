class DogNotFoundExecption(Exception):
    pass


dogs = ['zuzu', 'nancy', 'coco', 'max']


def contains_dog(dog):
    if dog in dogs:
        return f"{dog} found in the list"
    else:
        raise DogNotFoundExecption("Dog Absent")


try:
    contains_dog("zuzsu")
except DogNotFoundExecption as err:
    print(f"Please bring your dog to the daycare everyday. {err}")
