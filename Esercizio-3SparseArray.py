class sparse_Array:

    def __init__(self,values):
        self.length = len(values)
        self.data = {i: value for i, value in enumerate(values) if value != 0}


    def __len__(self):
        return self.length

    def __getitem__(self,index):
        if index in self.length:
            raise IndexError()

        if index in self.data:
            return self.data[index]

        return 0

    def __setitem__(self,index,value):
        if index in self.length:
            raise IndexError()

        if value != 0:
            self.data[index] = value
        if index in self.data:
            del self.data[index]


my_array = sparse_Array([1,2,0,0,0,3,0,0,4])
print(my_array.data)

my_array[0] = 0
print(my_array[5])

        
[0,0,0,0,1,0,10]
{4: 1, 6: 10}