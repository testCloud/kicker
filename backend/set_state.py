import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='kicker',
                         type='fanout')

message = json.dumps({
  'type': 'newState',
  'payload': {
    'kickerStatus': 'playerSelection',
    'gameMode': 'Competition',
    'teamBlack': {
      'attackPlayer': '7',
      'defensePlayer': '1'
    },
    'teamYellow': {
      'attackPlayer': 'CAT',
      'defensePlayer': 'idontcare'
    }
  }
})
channel.basic_publish(exchange='kicker',
                      routing_key='',
                      body=message)
connection.close()

