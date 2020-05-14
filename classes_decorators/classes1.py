class Pessoa:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser do tipo string")
        self._nome = nome

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        if not isinstance(sexo, str):
            raise TypeError("O sexo deve ser do tipo string")
        if sexo == "M":
            self._sexo = "Masculino"
        elif sexo == "F":
            self._sexo = "Feminino"
        else:
            raise ValueError("O sexo deve ser F ou M")
