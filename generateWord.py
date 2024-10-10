import json
import win32com.client as win32
import os
from pathlib import Path

# Cargar datos desde un archivo JSON
with open('json/expediente.json') as file:
    data = json.load(file)

# Abrir Word
word = win32.Dispatch('Word.Application')
word.Visible = True  # True si quieres ver la ventana de Word al ejecutar el script
doc = word.Documents.Open(os.path.abspath("plantilla_ficha_accidente.docx"))



# Diccionario de valores a reemplazar
reemplazos = {
    'nombre_trabajador': data['nombre_trabajador'],
    'puesto_trabajo': data['puesto_trabajo'],
    'edad': str(data['edad']),
    'experiencia': str(data['experiencia']),
    'lugar_accidente': data['lugar_accidente'],
    'hora_accidente': data['hora_accidente'],
    'fecha_accidente': data['fecha_accidente'],
    "descripcion_hechos": data['descripcion_hechos'],
    'lesion': data['lesion'],
}

tipo_lesion = data['tipo_lesion']

# Reemplazar los valores en los marcadores
for bookmark, value in reemplazos.items():
    if doc.Bookmarks.Exists(bookmark):
        doc.Bookmarks(bookmark).Range.Text = str(value)


path_image = r"c:\Users\varmido\Pictures\Screenshots\48fd9010-c1c1-11ee-9519-97453607d43e.jpg.webp"

for control in doc.ContentControls:
    if control.Title == "SexoHombre":
        control.Checked = (data['sexo'] == "H")  # Marcado si es hombre
    elif control.Title == "SexoMujer":
        control.Checked = (data['sexo'] == "M")  # Marcado si es mujer
    
    elif control.Title == "LesionLeve":
        control.Checked = (tipo_lesion[0] == 1)
    elif control.Title == "LesionGrave":
        control.Checked = (tipo_lesion[1] == 1)
    elif control.Title == "LesionMuyGrave":
        control.Checked = (tipo_lesion[2] == 1)
    elif control.Title == "LesionMortal":
        control.Title = (tipo_lesion[3] == 1)
    elif control.Title == "LesionSinLesion":
        control.Title = (tipo_lesion[0] == 0 and tipo_lesion[1] == 0 and tipo_lesion[2] == 0 and tipo_lesion[3] == 0)
    elif control.Title == "Foto1":
        control.Range.InlineShapes.AddPicture(path_image, LinkToFile=False, SaveWithDocument=True)

# Guardar el documento modificado
archivo = f"ficha_{data["id"]}.docx"
path_absolute_file_export = os.path.join(os.path.dirname(__file__), "media", "word", archivo)
doc.SaveAs(path_absolute_file_export)

# Cerrar Word

doc.Close()
word.Quit()
