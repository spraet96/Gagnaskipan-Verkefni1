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
        for _ in range(array_list.size):
            array_list.arr[size] = array_list.arr[size-1]
            size -= 1
        array_list.arr[0] = value
        array_list.size += 1
        return array_list

    def insert(self, value, index):
        
        if index > size:
            raise IndexOutOBounds()
        else:
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
        array_list.arr[index] = value

    def get_first(self):
        if array_list.size == 0:
            raise Empty()
        return array_list.arr[0]

    def get_at(self, index):
        return array_list.arr[index]
    
    def get_last(self):
        size = self.size
        return array_list.arr[size-1]

    def resize(self):
    
        for _ in range(array_list.capacity):
            array_list.capacity += 1
        for i in range(array_list.size):
            array_list.arr + [0]
        
    def remove_at(self, index):
        pass

    def clear(self):
        list_1 = []
        array_list.arr = list_1
        return array_list

array_list = ArrayList()
array_list.append(4)
array_list.append(3)
array_list.append(6)
#array_list.prepend(8)
#array_list.insert(6,6)

print(array_list)


