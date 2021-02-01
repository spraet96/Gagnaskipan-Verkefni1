class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
    
    def __str__(self):
        str_val = ""
        for i in range(array_list.size):
            if i == (array_list.size-1):
                str_val += str(array_list.arr[i])
            else:
                str_val += str(array_list.arr[i]) + ', '
        return str_val
    
    def prepend(self, value):
        size = self.size
        if self.size == self.capacity:
            array_list.resize()
        for _ in range(array_list.size):
            array_list.arr[size] = array_list.arr[size-1]
            size -= 1
        array_list.arr[0] = value
        array_list.size += 1
        return array_list

    def insert(self, value, index):
        size = self.size
        if index >= size:
            raise IndexOutOfBounds()
        elif self.size == self.capacity:
            array_list.resize()
        for _ in range(array_list.size-index):
            array_list.arr[size] = array_list.arr[size-1]
            size -= 1
        array_list.arr[index] = value
        array_list.size += 1
        return array_list       

    def append(self, value):
        if self.size == self.capacity:
            array_list.resize()
        array_list.arr[array_list.size] = value
        array_list.size += 1
        return array_list

    def set_at(self, value, index):
        if index > self.size:
            raise IndexOutOfBounds()
        else:
            array_list.arr[index] = value


    def get_first(self):
        if array_list.size == 0:
            raise Empty()
        return array_list.arr[0]

    def get_at(self, index):
        if index > self.size:
            raise IndexOutOfBounds()
        else:
            return array_list.arr[index]
    
    def get_last(self):
        if index > self.size:
            raise Empty()
        else:
            size = self.size
            return array_list.arr[size-1]

    def resize(self):
        old_arr = self.arr
        for _ in range(array_list.capacity):
            array_list.capacity += 1
        self.arr = [0] * self.capacity
        counter = 0
        for i in old_arr:
            self.arr[counter] = i
            counter += 1
        
    def remove_at(self, index):
        if index > self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(array_list.size):
                if self.arr[i] == index:
                    for j in range(i, self.size -1):
                        self.arr[j] = self.arr[j+1]
                    self.arr[self.size -1] = None
                    self.size -= 1
                    return

    def clear(self):
        list_1 = []
        array_list.arr = list_1
        return array_list

array_list = ArrayList()
array_list.remove_at(2)

print(array_list)


