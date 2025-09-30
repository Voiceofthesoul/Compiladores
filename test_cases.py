# test_cases.py - Casos de prueba específicos
from stack import Stack
from queue import Queue
from hashtable import HashTable

def test_casos_edge():
    """Prueba casos límite y especiales"""
    print("=== CASOS EDGE ===")
    
    # Stack vacío
    s = Stack()
    assert s.pop() is None, "Pop en stack vacío debe retornar None"
    assert s.peek() is None, "Peek en stack vacío debe retornar None"
    print(" Stack vacío")
    
    # Queue con un elemento
    q = Queue()
    q.enqueue(42)
    assert q.front() == 42, "Front debe mostrar elemento sin removerlo"
    assert q.dequeue() == 42, "Dequeue debe retornar el elemento"
    assert q.is_empty(), "Queue debe estar vacío después de dequeue"
    print(" Queue con un elemento")
    
    # HashTable con actualización
    ht = HashTable()
    ht.insert("key", "valor1")
    ht.insert("key", "valor2")
    assert ht.get("key") == "valor2", "Debe actualizar valor existente"
    print("✓ HashTable actualización")
    
    # Tipos de datos mixtos
    s = Stack()
    tipos = [42, "texto", [1,2], {"a": 1}, None]
    [s.push(x) for x in tipos]
    resultados = [s.pop() for _ in range(len(tipos))]
    assert resultados == tipos[::-1], "Stack debe manejar tipos mixtos"
    print(" Tipos de datos mixtos")

def test_operaciones_compuestas():
    """Prueba operaciones más complejas"""
    print("\n=== OPERACIONES COMPUESTAS ===")
    
    # Simulación de paréntesis balanceados con Stack
    s = Stack()
    expresion = "((a+b)*c)"
    balanceado = True
    for char in expresion:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.pop() is None:
                balanceado = False
                break
    balanceado = balanceado and s.is_empty()
    print(f" Paréntesis {'balanceados' if balanceado else 'desbalanceados'}")
    
    # Simulación de cola de impresión con Queue
    q = Queue()
    trabajos = ["doc1.pdf", "imagen.jpg", "reporte.docx"]
    [q.enqueue(t) for t in trabajos]
    print(f" Cola de impresión: {[q.dequeue() for _ in range(len(trabajos))]}")
    
    # Tabla de símbolos simple con HashTable
    ht = HashTable()
    simbolos = [("int", "x"), ("float", "pi"), ("string", "nombre")]
    [ht.insert(var, tipo) for tipo, var in simbolos]
    # Solo verificamos que funcione get
    print(f" Tabla de símbolos: x={ht.get('x')}, pi={ht.get('pi')}, nombre={ht.get('nombre')}")

if __name__ == "__main__":
    test_casos_edge()
    test_operaciones_compuestas()
    print("\n Todos los tests pasaron")