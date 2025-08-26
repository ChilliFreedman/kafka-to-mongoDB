from sub_kafka_configurations import ConsumerConfig

class ConsumerSet:
    def __init__(self,consumer_config:ConsumerConfig,topic):
        self.topic = topic
        self.consumer_con = consumer_config
        self.events = self.consumer_con.get_consumer_events(self.topic)

    def consumer_with_auto_commit(self):
        self.print_messages(self.events)

    def print_messages(self,events):
        for message in events:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))


if __name__ == '__main__':
    consumer = ConsumerSet(ConsumerConfig(),"interesting")
    consumer.consumer_with_auto_commit()


