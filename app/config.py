from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la aplicación
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
ENVIRONMENT = os.getenv("ENVIRONMENT")