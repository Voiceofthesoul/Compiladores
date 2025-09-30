# main.py - Programa de demostración y pruebas
from stack import Stack
from queue import Queue
from hashtable import HashTable
import time

def test_stack():
    print("=== STACK (LIFO) ===")
    s = Stack()
    [s.push(x) for x in [10, 20, 30]]
    print(f"Push: 10, 20, 30")
    print(f"Pop: {s.pop()} -> {s.pop()} -> {s.pop()}")
    print(f"Vacío: {s.is_empty()}\n")

def test_queue():
    print("=== QUEUE (FIFO) ===")
    q = Queue()
    [q.enqueue(x) for x in ['A', 'B', 'C']]
    print(f"Enqueue: A, B, C")
    print(f"Dequeue: {q.dequeue()} -> {q.dequeue()} -> {q.dequeue()}")
    print(f"Vacío: {q.is_empty()}\n")

def test_hashtable():
    print("=== HASH TABLE ===")
    ht = HashTable()
    datos = {"nombre": "Ana", "edad": 25, "ciudad": "MTY"}
    [ht.insert(k, v) for k, v in datos.items()]
    print(f"Insert: {datos}")
    print(f"Get 'nombre': {ht.get('nombre')}")
    ht.delete("ciudad")
    print(f"Keys después de eliminar 'ciudad': {ht.keys()}\n")


if __name__ == "__main__":
    test_stack()
    test_queue()
    test_hashtable()

    print("\n Tests completados")