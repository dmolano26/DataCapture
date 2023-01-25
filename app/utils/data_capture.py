from utils.statistics import Statistics


class DataCapture:
    """
    A class used to capture the data

    ...

    Methods
    -------
    add_number(number: int)
        method to add numbers to the collection.

    build_stats()
        method to pre-calculate the statistics for the collection.
        return: Statistics object
    """

    def __init__(self) -> None:
        self.numbers = []
        self.sum = 0
        self.less_than_count = {}
        self.greater_than_count = {}
        self.within_range_count = {}
        self.built = False

    def add_number(self, number: int) -> None:
        """Each time a number is added, it is also added to the
        corresponding dictionary and the count for that number is incremented.

        Args:
            number (int): new number to add.
        """
        self.numbers.append(number)
        self.sum += number
        self.less_than_count[number] = self.less_than_count.get(
            number, 0) + 1
        self.greater_than_count[number] = self.greater_than_count.get(
            number, 0) + 1
        self.within_range_count[number] = self.within_range_count.get(
            number, 0) + 1

    def build_stats(self) -> Statistics:
        """method to pre-calculate the statistics for the collection.

        Returns:
            Statistics: Object with the calculated data.
        """
        if self.built:
            return
        self.sum = sum(self.numbers)
        for i in range(len(self.numbers)):
            number = self.numbers[i]
            self.less_than_count[number] = len(
                [x for x in self.numbers[:i] if x < number]
            )
            self.greater_than_count[number] = len(
                [x for x in self.numbers[i + 1:] if x > number]
            )
            self.within_range_count[number] = (
                len([x for x in self.numbers if x >= number])
                - self.greater_than_count[number]
            )
        self.built = True
        return Statistics(self)
