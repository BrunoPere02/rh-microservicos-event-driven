import pika, json

def processar(ch, method, properties, body):
    evento = json.loads(body)
    if evento['tipo'] == 'FuncionarioContratado':
        print(f"Novo funcionario: {evento['nome']}")
        print(f"Criando folha de pagamento...")
        print(f"Salario: R$ {evento['salario']}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='rh.eventos')
channel.basic_consume(queue='rh.eventos',
    on_message_callback=processar, auto_ack=True)

print('Aguardando eventos de RH...')
channel.start_consuming()
