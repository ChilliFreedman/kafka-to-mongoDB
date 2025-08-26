import json
class DataLoader:
    def __init__(self,path_interesting = "data/interesting_category_dict.json",path_not_interesting = "data/not_intersting_category_dict.json"):
        self.path_interesting = path_interesting
        self.path_not_interesting = path_not_interesting

    def get_interesting_data(self):
        with open(self.path_interesting,encoding="utf-8") as interesting_json:
            interesting_data = json.load(interesting_json)
        return interesting_data

    def get_not_interesting_data(self):
        with open(self.path_not_interesting,encoding="utf-8") as not_interesting_json:
            not_interesting_data = json.load(not_interesting_json)
        return not_interesting_data

if __name__ == "__main__":
    dataloader = DataLoader()
    #print(dataloader.get_interesting_data())
    print(dataloader.get_not_interesting_data())