from validate_docbr import CPF, CNPJ


class Document:
    @staticmethod
    def create(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValuerError("Invalid digits quantity!")


class DocCpf:
    def __init__(self, document) -> None:
        if self.validate(document):
            self.cpf = document
        else:
            raise ValuerError("Invalid CPF!")

    def __str__(self) -> str:
        return self.format()

    def validate(self, document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)


class DocCnpj:
    def __init__(self, document) -> None:
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValuerError("Invalid CNPJ!")

    def __str__(self) -> str:
        return self.format()

    def validate(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
