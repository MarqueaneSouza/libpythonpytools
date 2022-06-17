class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailEnvalido(f'Email de remetente inválido: {remetente}')
        return remetente

class EmailEnvalido(Exception):
    pass