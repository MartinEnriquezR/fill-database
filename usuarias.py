#libreria para realizar las peticiones
from os import access
import requests
from requests import exceptions
#librerias para generar nombres de manera aleatoria
import names
#librerias para generar usernames de manera aleatoria
from random_username.generate import generate_username
#libreria para la generacion de fechas
import datetime
#manejo de numeros aleatorios
import random
from random import choice
#generacion de informacion en json
import json


#funcion que devuelve una una fecha de nacimiento aleatoria
def fechaNacimiento():
    random_number_of_days = random.randrange(days_betwee_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    birthdate = random_date.strftime('%Y-%b-%d')
    return birthdate


#url del backend
api = 'https://backend-upiita.herokuapp.com/'

#generar la fecha de nacimiento
start_date = datetime.date(1951,1,1)
end_date = datetime.date(2005,1,1)
time_between_dates = end_date - start_date
days_betwee_dates = time_between_dates.days

#catalogos para el registro
estado_civil = [
    "Separacion en proceso judicial",
    "Divorciado",
    "Soltero",
    "Casado",
    "Viudo",
    "Concubinato"
]
nacionalidad = [
    "Mexicana",
    "Estadounidense",
    "Espanola",
    "Colombiana",
    "Venezolana",
    "Argentina",
    "Hondurena",
    "Cubana",
    "Salvadorena",
    "Ecuatoriana",
    "Peruana",
    "Chilena",
    "Nicaraguense",
    "Costarricense"
]
escolaridad = [
    "Primaria",
    "Secundaria",
    "Preparatoria",
    "Universidad",
]
tipo_nariz = [
    "Aguilena",
    "Griega",
    "Ancha",
    "Chata",
    "Respingada",
    "Bulbosa",
    "Desigual",
    "Otro"
]
complexion = [
    "Endomorfo",
    "Mesomorfo",
    "Ectomorfo"
]
color_ojo = [
    "Negros",
    "Grises",
    "Azules",
    "Verdes",
    "Castanos",
    "Otro"
]
forma_rostro = [
    "Diamante",
    "Ovalado",
    "Cuadrado",
    "Redondo",
    "Triangulo",
    "Alargado",
    "Otro"
]
color_cabello = [
    "Cafe",
    "Negro",
    "Rubio",
    "Rojo",
    "Otro"
]
color_piel = [
    "Muy blanca",
    "Piel blanca",
    "Morena clara",
    "Morena bronceada",
    "Muy morena",
    "Negra",
    "Otro"
]
tipo_ceja = [
    "Recta",
    "Redonda",
    "Arqueada",
    "Sin ceja",
    "Otro"
]
textura_cabello = [
    "Lacio",
    "Ondulado",
    "Rizado",
    "Afro",
    "Calvo",
    "Otro"
]
enfermedades = [
    "Hipertension",
    "Artritis",
    "Diabetes",
    "Demencia",
    "Alzheimer",
    "Depresion",
    "Insuficiencia renal",
    "Enfermedad coronaria",
    "Otra",
    "Ninguna"
]
nombre_sena_particular = [
    "Cicatriz",
    "Tatuaje",
    "Amputacion"
]
nombre_ubicacion_particular = [
    "Cabeza",
    "Cuello",
    "Hombro",
    "Brazo",
    "Espalda",
    "Mano",
    "Muslo",
    "Trasero",
    "Pantorrilla",
    "Tobillo",
    "Frente",
    "Pecho",
    "Abdomen",
    "Rodilla",
    "Pierna",
    "Pie"
]


#(1) - registro de la usuaria
#informacion para registrar a la usuaria
#username aleatorio para la usuaria
username = generate_username()
informacion = {
    'password':'dwqj32j9032',
    'password_confirmation':'dwqj32j9032',
    'genero':'Femenino',
    'is_usuaria':'True',
    'is_contacto_confianza':'True',

    'email': username[0] + '@gmail.com',
    'username': username[0],
    'nombre': names.get_first_name(gender='female'),
    'apellido_paterno': names.get_last_name(),
    'apellido_materno': names.get_last_name(),
    'fecha_nacimiento': '1997-01-1', #fechaNacimiento(),
    'estatura': random.randint(120,190),

    'estado_civil': choice(estado_civil),
    'escolaridad': choice(escolaridad),
    'nacionalidad':choice(nacionalidad),
    'tipo_nariz':choice(tipo_nariz),
    'complexion':choice(complexion),
    'color_ojo':choice(color_ojo),
    'forma_rostro':choice(forma_rostro),
    'color_cabello':choice(color_cabello),
    'color_piel':choice(color_piel),
    'tipo_ceja':choice(tipo_ceja),
    'textura_cabello':choice(textura_cabello),
    'enfermedades':[
        {'nombre_enfermedad':'Ninguna'}
    ]
}
#registro de la usuaria
try: 
    response = requests.post(
        api + 'usuaria/signup/',
        json=informacion
    )
    #estado de la peticion
    print(response.status_code)
    #token de la usuaria
    json_data = json.loads(response.text)
    access_token = json_data['access_token']
except requests.exceptions.RequestException as error:
    print(error)

#(2) - asociar el dispositivo rastreador a la usuaria
numero_serie = 811
encabezado = {
    'Authorization': 'Token ' + access_token
}
informacion_dispositivo = {
    'numero_serie':numero_serie,
    'pin_desactivador':'1234'
}
try:
    response = requests.patch(
        api + 'dispositivo/asociar/',
        headers= encabezado,
        json = informacion_dispositivo
    )
    #estado de la peticion
    print(response.status_code)
except requests.exceptions.RequestException as error:
    print(error)

#(3) - peticion para crear el grupo de confianza de la usuaria
informacion_grupo = {
    'nombre':'Prueba'
}
try:
    response = requests.post(
        api + 'grupo/',
        headers = encabezado,
        json = informacion_grupo
    )
    #estado de la peticion
    print(response.status_code)
    #codigo del grupo de la usuaria
    json_data = json.loads(response.text)
    clave_acceso = json_data['grupo']['clave_acceso']
except requests.exceptions.RequestException as error:
    print(error)

#(4) registrar las señas particulares de cada usuaria
informacion_sena = {
    'descripcion':'breve descripcion',
    'nombre_sena_particular': choice(nombre_sena_particular),
    'nombre_ubicacion_corporal':choice(nombre_ubicacion_particular)
}
try:
    response = requests.post(
        api + 'senas/',
        headers= encabezado,
        json= informacion_sena
    )
    #respuesta de la peticion
    print(response.status_code)
except requests.exceptions.RequestException as error:
    print(error)

#(5) generar la primera alerta de la usuaria
# generar una alerta en el poligono en el estado de mexico
informacion_alerta = {
    "numero_serie": numero_serie,
    "nombre_alerta": "21/06/27/01:25:00",
    "fecha_hora_inicio": "2021-06-27T01:25:00",

    "latitud": "20.123456",
    "longitud": "20.123456",
    "fecha_hora": "2021-06-27T01:25:00"    
}
try:
    response = requests.post(
        api + 'alerta/publicar/',
        json = informacion_alerta
    )
    #estado de la peticion
    print(response.status_code)
except requests.exceptions.RequestException as error:
    print(error)

