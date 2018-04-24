try:
    from table_crud import CRUDTable
except:
    from Src.table_crud import CRUDTable
from collections import namedtuple

class QuickSort:

    """ make dictionary from tuples so that fields can be sorted with the help of dictionary keys"""
    def resultset(self, array):

        named_tuple = namedtuple(
        'data',
        ['id', 'name', 'email', 'phone', 'dob', 'gender', 'latitude', 'longitude', 'image', 'social_media']
        )
        return [dict(named_tuple(
            user_detail[0], user_detail[1], user_detail[2], user_detail[3], user_detail[4], user_detail[5], user_detail[6], user_detail[7], user_detail[8], user_detail[9]
            )._asdict()) for user_detail in array]
    
    def sort(self, array, key=None):
        less = list()
        equal = list()
        greater = list()
        if key:
            if len(array) > 1:
                pivot = array[0][key]
                for item in array:
                    if item[key] < pivot:
                        less.append(item)
                    elif item[key] > pivot:
                        greater.append(item)
                    else:
                        equal.append(item)
                return self.sort(less, key=key) + equal + self.sort(greater, key=key)
            else:
                return array
        else:
            if len(array) > 1:
                pivot = array[0]
                for item in array:
                    if item < pivot:
                        less.append(item)
                    elif item > pivot:
                        greater.append(item)
                    else:
                        equal.append(item)
                return self.sort(less) + equal + self.sort(greater)
            else:
                return array


# obj = QuickSort('postgres')
# data = obj.resultset()
# sorted_data = obj.sort(data, key='email')
# for _ in sorted_data:
#     print(_['email'])

# class MkUnique:
#     """
#     Check uniquness of value and make it unique
#     """
    
#     def unique(self, array, key):
#         i = 0
#         total_loop = len(array) - 1
#         while i<total_loop:
#             if a[i][key] == a[i+1][key]:
#                 a[i][key] += f'{i+1}'
#                 i += 1
#             else:
#                 i += 1




# a = [{'name': 'a'}, {'name': 'a'}, {'name': 'a'}]

# obj = MkUnique()
# obj.unique(a, 'name')
# print(a)