
def summa(x,y):
    try:
        return x + y
    except TypeError as e:
        raise e("Only numbers are allowed as parameters")