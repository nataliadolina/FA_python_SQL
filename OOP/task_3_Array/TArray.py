from string import Template


class TArray:
    def __init__(self, array_to_copy=None, num=0, data=None):
        if not array_to_copy:
            self.num = num
            self.data = [0] * self.num if not data else data

        else:
            self.num = array_to_copy.num
            self.data = array_to_copy.data

    def fill_index(self, data, index):
        self.data[index] = data
        return self

    def sorted(self):
        def switch(ind):
            if self.data[ind] > self.data[ind + 1]:
                buffer = self.data[ind + 1]
                self.data[ind + 1] = self.data[ind]
                self.data[ind] = buffer
                return True
            return False

        switched = True
        while switched:
            switched = False
            switched1, switched2 = False, False
            for i in range(0, len(self.data) - 1, 2):
                switched1 = switch(i)

            for j in range(1, len(self.data) - 1, 2):
                switched2 = switch(j)
            switched = switched1 or switched2

        return self

    def min(self):
        min_el = self.data[0]
        for i in self.data[1:]:
            if i < min_el:
                min_el = i
        return min_el

    def max(self):
        max_el = self.data[0]
        for i in self.data[1:]:
            if i > max_el:
                max_el = i
        return max_el

    def sum(self):
        s = 0
        for i in self.data:
            s += i
        return s

    def __add__(self, *data):
        for i in data:
            self.data.append(i)
        self.num = len(self.data)
        return self

    def __mul__(self, other):
        self.data = [i * other for i in self.data]
        return self

    def __str__(self):
        template_string = 'TArray[$length]{$data}'

        return Template(template_string).substitute(length=self.num, data=", ".join(map(str, self.data)))
