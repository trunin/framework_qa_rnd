from json import loads

from kafka import KafkaConsumer


from kafka_clent import KafkaTopics
from kafka_clent.utils import wait


class KafkaClient:

    def __init__(self, config):
        self._host = config['experiments_svc']['kafka']['host']
        self._port = config['experiments_svc']['kafka']['port']
        self._consumer = KafkaConsumer(group_id='qa-group',
                                       bootstrap_servers=f'{self._host}:{self._port}',
                                       value_deserializer=lambda x: loads(x.decode('utf-8')))

    def consume(self, topic):
        self._consumer.subscribe([topic])
        return self._consumer

    def dispose(self):
        self._consumer.close()


class CreateExpConsumer(KafkaClient):

    def wait_message_by_name(self, name, timeout=10):
        def func():
            for msg in self.consume(KafkaTopics.create_experiments):
                value = msg.value['payload']
                if name == value['name']:
                    return value
                else:
                    return None

        return wait(func, timeout)