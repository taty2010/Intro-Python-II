class Items():
    def __init__(self, name, info):
        self.name = name
        self.info = info
    def __str__(self):
        return f"Name: {self.name}, Info: {self.info}"

# command = "get item"
# command2 = input("pick up or drop an item:")
# result = command2.split(" ")
# for i, j in enumerate(result):
#     picked = ["item"]
#     if j == "get":
#         picked.append("item")
#         print("you picked up an item")
#     if j == "drop":
#         picked.remove("item")
#         print("you dropped an item")
