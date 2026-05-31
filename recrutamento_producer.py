import pika, json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='rh.eventos')

evento = {
    'tipo': 'FuncionarioContratado',
    'funcionario_id': 1042,
    'nome': 'Bruno Souza',
    'cargo': 'Dev Salesforce',
    'salario': 8500.00
}

channel.basic_publish(exchange='',
    routing_key='rh.eventos',
    body=json.dumps(evento))

print('Evento publicado:', evento['tipo'])
connection.close()
