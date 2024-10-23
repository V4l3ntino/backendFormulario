import json
import win32com.client as win32
import os
from pathlib import Path
import re

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
imagenes = data['imagenes'].split(",")
valoracion_hechos = data["valoracionHechos"].split(",")

if data['imagenes'] == "[]":
    imagenes = []

# Reemplazar los valores en los marcadores
for bookmark, value in reemplazos.items():
    if doc.Bookmarks.Exists(bookmark):
        doc.Bookmarks(bookmark).Range.Text = str(value)




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
        control.Checked = (tipo_lesion[3] == 1)
    elif control.Title == "LesionSinLesion":
        control.Checked = (data['lesionado_check'] == False)
    elif control.Title == "BAJA":
        control.Checked = (valoracion_hechos[0] == "BAJA")
    elif control.Title == "MEDIA":
        control.Checked = (valoracion_hechos[0] == "MEDIA")
    elif control.Title == "ALTA":
        control.Checked = (valoracion_hechos[0] == "ALTA")
    elif control.Title == "LEVE":
        control.Checked = (valoracion_hechos[1] == "LEVE")
    elif control.Title == "GRAVE":
        control.Checked = (valoracion_hechos[1] == "GRAVE")
    elif control.Title == "MUY GRAVE":
        control.Checked = (valoracion_hechos[1] == "MUY GRAVE")
    elif control.Title == "1SI":
        control.Checked = (valoracion_hechos[2] == "SI")
    elif control.Title == "1NO":
        control.Checked = (valoracion_hechos[2] == "NO")
    elif control.Title == "2SI":
        control.Checked = (valoracion_hechos[3] == "SI")
    elif control.Title == "2NO":
        control.Checked = (valoracion_hechos[3] == "NO")
    elif control.Title == "3SI":
        control.Checked = (valoracion_hechos[4] == "SI")
    elif control.Title == "3NO":
        control.Checked = (valoracion_hechos[4] == "NO")
    
    for index, image in enumerate(imagenes):
        image = re.sub(r"[<>[\]]","",image)
        image = image.split("/")[1]
        path_image = os.path.join(os.path.dirname(__file__), "media", "imagenes", image)
        if control.Title == f"Foto{index+1}":
            control.Range.InlineShapes.AddPicture(path_image, LinkToFile=False, SaveWithDocument=True)

# Guardar el documento modificado
archivo = f"ficha_{data["id"]}.docx"
path_absolute_file_export = os.path.join(os.path.dirname(__file__), "media", "word", archivo)
doc.SaveAs(path_absolute_file_export)

# Cerrar Word

doc.Close()
word.Quit()
