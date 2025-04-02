import os
from datetime import datetime

def colab_or_local():
    try:
        import google.colab
        return True
    except ImportError:
        return False

# Definir rutas según si es local o en la nube
if colab_or_local():
    from google.colab import drive
    drive.mount('/content/drive')
    base_directory = '/content/drive/MyDrive'
    print("Ejecutando en Google Colab (Entorno en la nube)")
else:
    base_directory = os.getcwd()
    print("Ejecutando en entorno local")

# Función para obtener fecha de creación
def get_creation_date(file_path):
    timestamp = os.path.getctime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

# Función para listar archivos
def list_directory_files(directory):
    try:
        items = os.listdir(directory)
        print(f"\nContenido del directorio: {directory}\n")
        print("{:<40} {:<20} {:<15} {:<10}".format(
            "Nombre", "Tipo", "Tamaño (bytes)", "Creado el"))
        print("-" * 90)

        for item in items:
            item_path = os.path.join(directory, item)

            if os.path.isfile(item_path):
                item_type = "Archivo"
                size = os.path.getsize(item_path)
            elif os.path.isdir(item_path):
                item_type = "Directorio"
                size = "-"
            else:
                item_type = "Otro"
                size = "-"

            creation_date = get_creation_date(item_path)

            print("{:<40} {:<20} {:<15} {:<10}".format(
                item, item_type,str(size), creation_date))

    except FileNotFoundError:
        print(f"Error: El directorio {directory} no existe.")
    except PermissionError:
        print(f"Error: No tienes permiso para acceder a {directory}")

# Ejecutar la función principal
list_directory_files(base_directory)
