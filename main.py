class NobalInteger:
    """sorting array in ascending order
       if we do this ... now  no of previous elements = no of elements smaller than present element
       """
    def nobal(self, array):
        array.sort()

        """ check current element is not equal to previous element and if yes increase s_count
            ...apo dhan no of previous elements = no of elements greater than present element .. 
            here dont count for duplicate element """

        count = 0
        s_count = 0
        if array[0] == 0:
            count += 1
        for i in range(1, len(array)):
            if array[i] != array[i-1]:
                s_count = i  # so i elements are smaller than present element
            if array[i] == s_count:
                count += 1

        return count


object = NobalInteger()
array = list(map(int, input().split()))
print(object.nobal(array))