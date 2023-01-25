class Statistics:
    """
    Class that have all the methods to get the statistics

    ...

    Methods
    -------
    sum(number: int)
        Method to now the total sum of the numbers added to the collection.

    less(value: int)
        Method to know how many numbers are in the collection less
        than a value.

        return: int

    greater(value: int)
        Method to know how many numbers are in the collection greater
        than a value.

        return: int

    between(value: int)
        Method to know how many numbers are in the collection between a range.
        return: int
    """

    def __init__(self, data_capture):
        self.data_capture = data_capture

    def sum(self):
        """Method to now the total sum of the numbers in the collection."""
        return self.data_capture.sum

    def less(self, value: int):
        """Method to know how many numbers are in the collection less than a value.

        Args:
            value (int): Number to compare.
        """
        return len([x for x in self.data_capture.numbers if x < value])

    def greater(self, value: int):
        """Method to know how many numbers are in the collection greater than a value.

        Args:
            value (int): Number to compare."""
        return len([x for x in self.data_capture.numbers if x > value])

    def between(self, low: int, high: int):
        """Method to know how many numbers are in the collection between a range.

        Args:
            low (int): Min range number.
            high (int): Max range number.
        """
        return len([x for x in self.data_capture.numbers if low <= x <= high])
