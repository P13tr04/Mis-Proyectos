import time
import random
from typing import List, Dict, Tuple

def crear_paciente(id_paciente: int, nombre: str, gravedad: int, tiempo_espera: int, edad: int) -> Dict:
    """Crea y retorna un diccionario representando un paciente"""
    return {
        'id': id_paciente,
        'nombre': nombre,
        'gravedad': gravedad,
        'tiempo_espera': tiempo_espera,
        'edad': edad
    }

def generar_pacientes_aleatorios(cantidad: int) -> List[Dict]:
    """Genera una lista de pacientes aleatorios"""
    nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofia"]
    pacientes = []
    for i in range(cantidad):
        paciente = crear_paciente(
            id_paciente=i+1,
            nombre=random.choice(nombres),
            gravedad=random.randint(1, 10),
            tiempo_espera=random.randint(5, 240),
            edad=random.randint(1, 99)
        )
        pacientes.append(paciente)
    return pacientes

def quick_sort_gravedad(pacientes: List[Dict]) -> List[Dict]:
    """Ordena pacientes por gravedad (descendente) usando QuickSort"""
    if len(pacientes) <= 1:
        return pacientes
    
    pivot = pacientes[len(pacientes) // 2]
    left = [x for x in pacientes if x['gravedad'] > pivot['gravedad']]
    middle = [x for x in pacientes if x['gravedad'] == pivot['gravedad']]
    right = [x for x in pacientes if x['gravedad'] < pivot['gravedad']]
    
    return quick_sort_gravedad(left) + middle + quick_sort_gravedad(right)

def insertion_sort_edad(pacientes: List[Dict]) -> List[Dict]:
    """Ordena pacientes por edad (descendente) usando InsertionSort"""
    for i in range(1, len(pacientes)):
        key = pacientes[i]
        j = i-1
        while j >= 0 and key['edad'] > pacientes[j]['edad']:
            pacientes[j+1] = pacientes[j]
            j -= 1
        pacientes[j+1] = key
    return pacientes

def bubble_sort_tiempo_espera(pacientes: List[Dict]) -> List[Dict]:
    """Ordena pacientes por tiempo de espera (descendente) usando BubbleSort"""
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j]['tiempo_espera'] < pacientes[j+1]['tiempo_espera']:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    return pacientes

def priorizar_pacientes(pacientes: List[Dict], estrategia: str) -> Tuple[List[Dict], float]:
    """Prioriza pacientes según la estrategia especificada y mide el tiempo de ejecución"""
    start_time = time.time()
    
    if estrategia == 'gravedad':
        resultado = quick_sort_gravedad(pacientes.copy())
    elif estrategia == 'edad':
        resultado = insertion_sort_edad(pacientes.copy())
    elif estrategia == 'tiempo_espera':
        resultado = bubble_sort_tiempo_espera(pacientes.copy())
    else:
        raise ValueError("Estrategia no válida")
    
    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    
    return resultado, tiempo_ejecucion

def mostrar_pacientes(pacientes: List[Dict], titulo: str = "Lista de Pacientes"):
    """Muestra una lista de pacientes en formato tabular"""
    print(f"\n{titulo}:")
    print("-" * 70)
    print(f"{'ID':<5}{'Nombre':<15}{'Gravedad':<10}{'Edad':<10}{'Tiempo Espera (min)':<20}")
    print("-" * 70)
    for p in pacientes:
        print(f"{p['id']:<5}{p['nombre']:<15}{p['gravedad']:<10}{p['edad']:<10}{p['tiempo_espera']:<20}")
    print("-" * 70)

def analizar_rendimiento(pacientes: List[Dict], iteraciones: int = 10):
    """Analiza el rendimiento de los algoritmos de ordenamiento"""
    tiempos = {
        'gravedad': [],
        'edad': [],
        'tiempo_espera': []
    }
    
    for _ in range(iteraciones):
        _, tiempo = priorizar_pacientes(pacientes, 'gravedad')
        tiempos['gravedad'].append(tiempo)
        
        _, tiempo = priorizar_pacientes(pacientes, 'edad')
        tiempos['edad'].append(tiempo)
        
        _, tiempo = priorizar_pacientes(pacientes, 'tiempo_espera')
        tiempos['tiempo_espera'].append(tiempo)
    
    # Calcular promedios
    promedio_gravedad = sum(tiempos['gravedad'])/len(tiempos['gravedad'])
    promedio_edad = sum(tiempos['edad'])/len(tiempos['edad'])
    promedio_espera = sum(tiempos['tiempo_espera'])/len(tiempos['tiempo_espera'])
    
    # Mostrar resultados en texto
    print("\nAnálisis de Rendimiento:")
    print(f"QuickSort (Gravedad): {promedio_gravedad:.6f} segundos (promedio)")
    print(f"InsertionSort (Edad): {promedio_edad:.6f} segundos (promedio)")
    print(f"BubbleSort (Tiempo Espera): {promedio_espera:.6f} segundos (promedio)")

# Ejemplo de uso
if __name__ == "__main__":
    # Generar datos de prueba
    pacientes = generar_pacientes_aleatorios(20)
    
    # Mostrar pacientes sin ordenar
    mostrar_pacientes(pacientes, "Pacientes sin ordenar")
    
    # Priorizar por diferentes criterios
    pacientes_gravedad, _ = priorizar_pacientes(pacientes, 'gravedad')
    mostrar_pacientes(pacientes_gravedad, "Pacientes ordenados por Gravedad (QuickSort)")
    
    pacientes_edad, _ = priorizar_pacientes(pacientes, 'edad')
    mostrar_pacientes(pacientes_edad, "Pacientes ordenados por Edad (InsertionSort)")
    
    pacientes_espera, _ = priorizar_pacientes(pacientes, 'tiempo_espera')
    mostrar_pacientes(pacientes_espera, "Pacientes ordenados por Tiempo de Espera (BubbleSort)")
    
    # Analizar rendimiento de los algoritmos
    analizar_rendimiento(pacientes)
