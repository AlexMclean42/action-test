import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "version": 1
        })
    }






# def add(a, b):
#     return a+b

# def subtract(a, b):
#     return a-b

# def divide(a, b):
#     return a//b

# def multiply(a, b):
#     return a*b
