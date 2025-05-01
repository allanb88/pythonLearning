from pathlib import Path
from time import ctime

# archivo.exists()
#archivo = Path("archivos/archivo-prueba.txt")
archivo = Path("./archivo-prueba.txt")

# archivo.rename()
# archivo.unlink()
# print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))
