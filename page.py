class Page:
    def __init__(self, name, neighbors, page_rank):
        self.name = name
        self.neighbors = neighbors
        self.pageRank = page_rank

    def send_messages(self):
        tab = []
        for neighbor in self.neighbors:
            #neighbor_number = 1 if len(self.neighbor) == 0 else len(self.neighbors)
            tab.append((neighbor, (self.pageRank / len(self.neighbors))))
            tab.append((self.name, 0))
        return tab

