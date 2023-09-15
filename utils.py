class utils:
    @staticmethod
    def reversed(number):
        return int(str(number)[::-1])

    @staticmethod
    def formatter(number):
        binary_format = bin(number)
        octal_format = oct(number)
        return binary_format, octal_format
