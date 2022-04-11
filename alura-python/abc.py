from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    def __delitem__(self):
        pass

    def __setitem__(self):
        pass

    def insert(self):
        pass


objetoValidado = MinhaListinhaMutavel('myname', ['myprogram', 'myprogram2'])
for item in objetoValidado:
    print(item)
