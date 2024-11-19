import json
import win32com.client as win32
import os
from pathlib import Path
import re
import json

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
    'tipo_suceso': data['tipo_suceso'],
    'creador': data['creador'],
    'fecha_investigacion': data['fecha_investigacion'],
    'empresa': data['empresa']
}

tipo_lesion = data['tipo_lesion']
imagenes = data['imagenes'].split(",")
valoracion_hechos = data["valoracionHechos"].split(",")
analisis_causas = json.loads(data["analisis_causas"])
causas_accidente = json.loads(data["causas_accidente"])
acciones_aplicar = json.loads(data["aplicar_accion"])


if data['imagenes'] == "[]":
    imagenes = []

# Reemplazar los valores en los marcadores
for bookmark, value in reemplazos.items():
    if doc.Bookmarks.Exists(bookmark):
        doc.Bookmarks(bookmark).Range.Text = str(value)


if doc.Bookmarks.Exists("lista_causas"):
    bookmark = doc.Bookmarks("lista_causas").Range
    bookmark.Text = ""
    bookmark.ListFormat.ApplyBulletDefault()
    for causa in causas_accidente:
        bookmark.InsertAfter(causa)
        bookmark.InsertParagraphAfter()
            
controlBox = False

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
    elif control.Title == data['formas_accidente']:
        control.Checked = (True)
        controlBox = True
    
    for index, image in enumerate(imagenes):
        image = re.sub(r"[<>[\]]","",image)
        image = image.split("/")[1]
        path_image = os.path.join(os.path.dirname(__file__), "media", "imagenes", image)
        if control.Title == f"Foto{index+1}":
            control.Range.InlineShapes.AddPicture(path_image, LinkToFile=False, SaveWithDocument=True)
    
    for lista in analisis_causas:
        for tipo in lista:
            if control.Title == tipo:
                control.Checked = (True)

# Guardar el documento modificado
archivo = f"ficha_{data["id"]}.docx"
path_absolute_file_export = os.path.join(os.path.dirname(__file__), "media", "word", archivo)
doc.SaveAs(path_absolute_file_export)

bookmark_name="tabla_acciones"
if doc.Bookmarks.Exists(bookmark_name) and len(acciones_aplicar) > 0:
    # Selecciona el rango del marcador
    bookmark_range = doc.Bookmarks(bookmark_name).Range
    
    # Asegúrate de que el marcador contiene una tabla y accede a ella
    if bookmark_range.Tables.Count > 0:
        table = bookmark_range.Tables(1)
        new_row = table.Rows(2)
        
        new_row.Cells(1).Range.Text = acciones_aplicar[0][0]
        new_row.Cells(2).Range.Text = acciones_aplicar[0][1]
        new_row.Cells(3).Range.Text = acciones_aplicar[0][2]
        
        if(len(acciones_aplicar) > 1):
            acciones_aplicar = acciones_aplicar[1:]        
            for accion in acciones_aplicar:
                # Añadir una nueva fila al final de la tabla
                new_row = table.Rows.Add()
                
                # Rellenar las celdas de la nueva fila (ejemplo para una tabla de 3 columnas)
                
                new_row.Cells(1).Range.Text = accion[0]
                new_row.Cells(2).Range.Text = accion[1]
                new_row.Cells(3).Range.Text = accion[2]

    else:
        print("No se encontró una tabla en el marcador especificado.")


if not controlBox:    
    bookmark_name = "tabla_formas_producirse"
    if doc.Bookmarks.Exists(bookmark_name):
        bookmark_range = doc.Bookmarks(bookmark_name).Range
        celda1 = False
        celda2 = False
        if bookmark_range.Tables.Count > 0:
            table = bookmark_range.Tables(1)
            for row in table.Rows:
                for index, cell in enumerate(row.Cells):
                    cell_text = cell.Range.Text.strip()
                    if(index % 2 != 0 and celda2 == False):
                        # Usar una expresión regular para verificar si el texto contiene solo caracteres de control o está vacío
                        if re.match(r'^[\x07\x0D]*$', cell_text):  # \x07 es el carácter de fin de celda, \x0D es retorno de carro
                            cell.Range.Text = data['formas_accidente']
                            celda2 = True
                    elif (celda1 == False):
                        if re.match(r'^[\x07\x0D]*$', cell_text):  # \x07 es el carácter de fin de celda, \x0D es retorno de carro
                            checkbox = cell.Range.ContentControls.Add(8)
                            checkbox.Title = "Checkbox"
                            checkbox.Checked = True
                            celda1 = True
            

# Cerrar Word

doc.Close()
word.Quit()
