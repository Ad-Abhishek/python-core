class my_exception(Exception):
    pass


x = 2
try:
    raise my_exception("This is my custom exception.")
    # print(x / 0)
    # if not type(x) is str:
    #     raise Exception("custom exception")
except NameError:
    print("looks like you've made a Name error")
except ZeroDivisionError:
    print("do not divide by zero")
except Exception as error:
    print(error)
else:
    print("no errors")
finally:
    print("I'm going to print with or without any error.")
