try:
    from table_crud import CRUDTable
except:
    from Src.table_crud import CRUDTable
from collections import namedtuple

class QuickSort:

    def __init__(self, db_name='secondb'):
        self.connection_obj = CRUDTable(db_name)
        self.array = self.connection_obj.get_all()
    
    def resultset(self):
        named_tuple = namedtuple(
        'data',
        ['id', 'name', 'email', 'phone', 'dob', 'gender', 'latitude', 'longitude', 'image', 'social_media']
        )
        return [dict(named_tuple(
            user_detail[0], user_detail[1], user_detail[2], user_detail[3], user_detail[4], user_detail[5], user_detail[6], user_detail[7], user_detail[8], user_detail[9]
            )._asdict()) for user_detail in self.array]
    
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


obj = QuickSort()
data = obj.resultset()
sorted_data = obj.sort(data, key='name')
for _ in sorted_data:
    print(_['name'])