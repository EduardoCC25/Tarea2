# Figuras Geometricas

* **Diseño basado en Contratos:** La clase `FiguraGeometrica` actúa como un "contrato" estricto. Al heredar de `ABC` (Abstract Base Class), obliga a que cualquier figura nueva (como `Cuadrado` o `Circunferencia`) implemente obligatoriamente los métodos `area` y `perimetro`, garantizando que el sistema nunca intente calcular una figura incompleta.
    
* **Inicialización Cooperativa:** Cuando creas un objeto (ej. `c1 = Cuadrado(...)`), Python coordina múltiples constructores. El código llama explícitamente a `FiguraGeometrica.__init__` para las matemáticas y a `Color.__init__` para el estilo, fusionando dos conceptos independientes en un solo objeto funcional.
* **Protección de Invariantes:** El programa protege la lógica interna mediante *setters*. Antes de guardar cualquier dato en `_ancho` o `_alto`, el código intercepta el valor y verifica que sea positivo; si no lo es, bloquea la operación inmediatamente con un error, evitando cálculos corruptos más adelante.
* **Procesamiento en Lote:** El archivo `main.py` centraliza la ejecución agrupando objetos dispares en una lista `figuras`. Esto permite calcular métricas globales (sumas totales) sin necesidad de escribir algoritmos separados para rectángulos o círculos.

<img width="1920" height="1080" alt="Captura de pantalla 2025-11-20 185829" src="https://github.com/user-attachments/assets/a6fb49ce-a971-401d-8f95-3fbf026d7902" />
