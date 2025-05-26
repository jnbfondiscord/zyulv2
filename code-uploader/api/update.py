import os

def handler(request):
    if request.method == "POST":
        body = request.body.decode()
        with open("lopa.txt", "w") as f:
            f.write(body)
        return {
            "statusCode": 200,
            "body": "Code updated."
        }
    else:
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }
