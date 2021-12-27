"""
Métodos Dunter (duplo underscore)
"""


class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:  # primeiro dunter (init) que é o construtor de objetos
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):  # representa o objeto , já que o padrão, exibe o endereço de memória
        return f"{self.__titulo} é o titulo"

    def __str__(self):  # retorno padrão em texto, mas, o str sobreescreve o repr
        return self.__titulo

    # criar um método len para evitar o aparecimento de erro , comum em classes abstratas
    def __len__(self):
        return self.__paginas

    # fazer um garbage collector(remover variável da memória)
    def __del__(self):
        print("Variável deletada")

    # somar ou concatenar, evitando o problema
    def __add__(self, other):
        return f"{self}  {other}"

    # multiplicar string e numero
    def __mul__(self, other: int) -> str:
        if isinstance(other, int):
            msg = ''
            for num in range(1, other + 1):
                msg += str(self) + ' '
            return msg
        return "Multiplicação não possível"

if __name__ == '__main__':
    livro1: object = Livro("Python", "Alguem", 554)
    print(livro1)
    print(len(livro1))
    print(livro1 + 2)
    print(livro1 * 4)
    del livro1