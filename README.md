**-- STACK (lifo), QUEUE (fifo), TABLE/HASH/DICTIONARY (order)--**

**Librerías de Python Standard Library:**

**collections.deque**
Para Stack y Queue
Proporciona operaciones O(1) en ambos extremos
Métodos: append(), pop(), popleft()

**collections.OrderedDict**
Para HashTable
Mantiene el orden de inserción

**time**
Para medir rendimiento
Función: time.perf_counter() para mediciones precisas

** CASOS DE PRUEBA (TEST CASES)**
1. OPERACIONES BÁSICAS (main.py)
**Stack Tests:**

 Push múltiples elementos (10, 20, 30)
Pop en orden LIFO (30 → 20 → 10)
Verificación de stack vacío

**Queue Tests:**

Enqueue múltiples elementos ('A', 'B', 'C')
Dequeue en orden FIFO ('A' → 'B' → 'C')
Verificación de queue vacío

**HashTable Tests:**

Inserción de pares clave-valor
Recuperación de valores con get()
Eliminación de elementos
✅ Listado de claves restantes

