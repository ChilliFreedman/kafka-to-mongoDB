
from pub_kafka_configurations import ProducerConfig
from pub_kafka_producer import ProducerSet
from data_loader import DataLoader

class Manager:
    def __init__(self,topic1 = "interesting",topic2 = "not_interesting"):
        self.topic1 = topic1
        self.topic2 = topic2
        self.producer_con = ProducerConfig()
        self.producer_set = ProducerSet(self.producer_con)
        self.data_loader = DataLoader()
        self.all_interesting_data = self.data_loader.get_interesting_data()
        self.all_not_interesting_data = self.data_loader.get_not_interesting_data()
        self.interesting_message = None
        self.not_interesting_message = None

    def get_10_interesting_articles(self):
        interesting_dict = {}
        for category,articl in self.all_interesting_data.items():
            interesting_dict[category] = articl[0]
            articl.pop(0)
        return interesting_dict

    def get_10_not_interesting_articles(self):
        not_interesting_dict = {}
        for category,articl in self.all_interesting_data.items():
            not_interesting_dict[category] = articl[0]
            articl.pop(0)
        return not_interesting_dict



    def publish_messages(self):
        self.producer_set.publish_message(self.topic1,self.get_10_interesting_articles())
        self.producer_set.publish_message(self.topic2, self.get_10_not_interesting_articles())
        self.producer_set.producer.flush()

if __name__ == "__main__":
    manager = Manager()
    manager.publish_messages()