# File encoding: UTF-8


class Array(object):
    def sum(self, size, array_string):
        numbers = [int(number) for number in array_string.split(' ')]
        if size != len(numbers):
            raise Exception('array size is not matched')
        return sum(numbers)
