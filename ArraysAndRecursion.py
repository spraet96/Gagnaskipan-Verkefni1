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
        for i in range(array_list.size):
            array_list[i] = array_list[i+1]
        array_list[0] = value
        return array_list

    def insert(self, value, index):
        pass

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
array_list.prepend(7)

print(array_list)