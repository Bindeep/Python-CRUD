from collections import namedtuple

class LinerSearch:
    
    def linear_search(self, values, search_for, key='id'):
        search_at = 0
        search_res = None
    # Match the value with each data element
        while search_at < len(values) and search_res is None:
            if values[search_at][key] == search_for:
                search_res = values[search_at]
            else:
                search_at = search_at + 1

        return search_res

class BinarySearch:

    def search(self, a_list, item, key='id'):
        """Performs iterative binary search to find the position of an integer in a given, sorted, list.
        a_list -- sorted list of integers
        item -- integer you are searching for the position of
        """

        first = 0
        last = len(a_list) - 1

        while first <= last:
            mid = (first + last) // 2
            if a_list[mid][key] == item:
                return a_list[mid]
            elif a_list[mid][key] > item:
                last = mid - 1
            elif a_list[mid][key] < item:
                first = mid + 1
            else:
                return f'{item} not found in the list'
