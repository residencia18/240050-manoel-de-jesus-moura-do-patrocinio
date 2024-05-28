class Item:
    def __init__(self, name):
        self.name = name

class ItemCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not item or not isinstance(item, Item):
            raise ValueError("Item must be a valid Item instance")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not found in the collection")
        self.items.remove(item)

    def get_items(self):
        return self.items
