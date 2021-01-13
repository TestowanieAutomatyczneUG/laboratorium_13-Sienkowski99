class FizzBuzz:
    def game(self, num):
        if not isinstance(num, int):
            return "err"
        # num = int(num)
        if (num % 5) == 0 and num % 3 == 0:
            return "FizzBuzz"
        elif (num % 5) == 0 and num % 3 != 0:
            return "Buzz"
        elif (num % 5) != 0 and num % 3 == 0:
            return "Fizz"
        elif (num % 5) != 0 and num % 3 != 0:
            return f"{num}"
        else:
            raise Exception("Error in FizzBuzz")
