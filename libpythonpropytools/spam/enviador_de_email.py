class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Emailnvalido(f'Email de remetente inválido: {remetente}')
        return remetente


class Emailnvalido(Exception):
    pass
