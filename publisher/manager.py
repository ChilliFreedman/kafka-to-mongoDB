from pub_kafka_configurations import ProducerConfig
from pub_kafka_producer import ProducerSet
class Manager:
    def __init__(self,topic1 = "interesting",topic2 = "not_interesting"):
        self.topic1 = topic1
        self.topic2 = topic2
        self.producer_con = ProducerConfig()
        self.producer_set = ProducerSet(self.producer_con)
        self.interesting_message = None
        self.not_interesting_message = None

    def publish_messages(self):
        self.producer_set.publish_message(self.topic1,self.interesting_message)
        self.producer_set.publish_message(self.topic2, self.not_interesting_message)

