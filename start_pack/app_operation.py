from utils import functions


def app_operation(operations):
    five_operations = functions.get_five_operation(operations)
    for i in five_operations:
        print(i)