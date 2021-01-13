class Hamming:
    def distance(self, a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            return "error"
        if len(a) != len(b):
            return "strings are not equally long"
        result = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                result += 1
        return result
