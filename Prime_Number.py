def is_Prime(num):
        """check if a number is a prime number

        print(is_Prime(97))
        >>>True

        """
        if num > 1:
                for i in range(2,num):
                        if num % i == 0:
                                return False
                        else:
                                return True

