class utils:
    @staticmethod
    def reversed(number):
        if isinstance(number, int):
            return int(str(number)[::-1])
        else:
            raise TypeError("Input must be an integer")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            print("hello")
            return bin(number), oct(number)
        else:
            raise TypeError("Input must be an integer")
