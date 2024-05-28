import pytest

import sys
import os 

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from atividade09_collection import Item,ItemCollection

#  -------- ROTEIRO DE TESTE --------

# Adição de um item válido.
# Tentativa de adicionar um item inválido.
# Remoção de um item existente.
# Tentativa de remover um item que não está na coleção.
# Recuperação de itens da coleção.



def test_add_item():
    collection = ItemCollection()
    item = Item("item1")
    
    collection.add_item(item)
    
    assert item in collection.get_items()

def test_add_invalid_item():
    collection = ItemCollection()
    
    with pytest.raises(ValueError, match="Item must be a valid Item instance"):
        collection.add_item(None)
        
    with pytest.raises(ValueError, match="Item must be a valid Item instance"):
        collection.add_item("Not an item")

def test_remove_item():
    collection = ItemCollection()
    item = Item("item1")
    collection.add_item(item)
    
    collection.remove_item(item)
    
    assert item not in collection.get_items()

def test_remove_item_not_in_collection():
    collection = ItemCollection()
    item = Item("item1")
    
    with pytest.raises(ValueError, match="Item not found in the collection"):
        collection.remove_item(item)

def test_get_items():
    collection = ItemCollection()
    item1 = Item("item1")
    item2 = Item("item2")
    
    collection.add_item(item1)
    collection.add_item(item2)
    
    items = collection.get_items()
    
    assert len(items) == 2
    assert item1 in items
    assert item2 in items