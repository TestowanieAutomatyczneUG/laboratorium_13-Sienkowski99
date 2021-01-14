# def roman(num):
#     symbols = {
#         1: "I",
#         4: "IV",
#         5: "V",
#         9: "IX",
#         10: "X",
#         40: "XL",
#         50: "L",
#         90: "XC",
#         100: "C",
#         400: "CD",
#         500: "D",
#         900: "CM",
#         1000: "M",
#     }
#     helper = []
#     for key in symbols:
#         helper.append(key)
#     helper.reverse()
#     result = ""
#     for symbol in helper:
#         while num >= symbol:
#             result += symbols[symbol]
#             num -= symbol
#     return result


class Database:
    def __init__(self):
        self.users = []

    def add_user(self, login, password):
        if login is None and password is None:
            return "critical error"
        if not isinstance(login, str) or not isinstance(password, str):
            return "ERROR"
        if len(password) < 5:
            return "password is too short"
        user = {
            "login": login,
            "password": password
        }
        self.users.append(user)
        return user

    def change_password(self, login, password):
        if login is None and password is None:
            return "critical error"
        if not isinstance(login, str) or not isinstance(password, str):
            return "ERROR"
        if len(password) < 5:
            return "password is too short"
        user = list(filter(lambda x: x["login"] == login, self.users))[0]
        if user["password"] == password:
            return "password has not changed"
        user["password"] = password
        return user
