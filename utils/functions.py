import json


def get_five_operation(operations):
    with open(operations, encoding='utf-8') as f:
        list_operations = json.load(f)
        five_last_operations = list_operations[-5:]
        five_last_operations.reverse()
        return five_last_operations
