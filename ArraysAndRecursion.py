class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
    
    def __str__(self):
        str_val = ""
        for i in range(array_list.size):
            str_val += str(array_list.arr[i])
        return str_val
    
    def prepend(self, value):
        size = self.size
<<<<<<< HEAD
        for i in range(array_list.size):
=======
        for _ in range(array_list.size):
>>>>>>> da55e989df4404149946132b5b57d6330dc4b2d9
            array_list.arr[size] = array_list.arr[size-1]
            size -= 1
        array_list.arr[0] = value
        array_list.size += 1
        return array_list

    def insert(self, value, index):
        size = self.size
        for _ in range(array_list.size-index):
            array_list.arr[size] = array_list.arr[size-1]
            size -= 1
        array_list.arr[index] = value
        array_list.size += 1
        return array_list

    def append(self, value):
        array_list.arr[array_list.size] = value
        array_list.size += 1
        return array_list

    def set_at(self, value, index):
        pass

    def get_first(self):
        pass

    def get_at(self, index):
        pass
    
    def get_last(self):
        pass

    def resize(self):
        pass

    def remove_at(self, index):
        pass

    def clear(self):
        pass

array_list = ArrayList()
array_list.append(4)
array_list.append(3)
array_list.append(6)
<<<<<<< HEAD
array_list.prepend(7)
=======
#array_list.prepend(8)
array_list.insert(1,0)

print(array_list)

>>>>>>> da55e989df4404149946132b5b57d6330dc4b2d9

