import os

direectory = os.path.join(
    os.getcwd(), "data")
try:
    os.rmdir(direectory)
except Exception as e:
    print("Error happened " + e.__str__())
