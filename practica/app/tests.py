from django.test import TestCase
from pathlib import Path
import sys
# Add the parent directory to sys.path to import models
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import *
from app.models import *

# crear
#t = Categoria (nombre="portatiles")
#t.save()

# listar
#query = Categoria.objects.all()
#print("Categorías:", query)

# delete
#t = Categoria.objects.get(id=4)
#t.delete()
#print("Eliminado:", t.nombre)


