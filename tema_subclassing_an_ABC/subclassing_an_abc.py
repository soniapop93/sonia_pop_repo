from collections.abc import MutableSequence

class CrayonsBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def __delitem__(self, index):
        self._crayons.remove(index)

    def insert(self, index, value):
        self._crayons.insert(index, value)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
