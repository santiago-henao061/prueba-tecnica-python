# Desarrollar un script en Python que, partiendo de los seguidores de las cuentas de
# Instagram @elcorteingles, @mercadona y @carrefoures, extraiga para cada seguidor la siguiente información pública:
# • Nombre completo tal como figura en su perfil
# • Número(s) de teléfono (si están publicados)
# • Dirección(es) de correo electrónico (si están publicadas)
# • Fecha de creación del perfil (o fecha de primera/última publicación si no se dispone)

#para extraer esta informacion podriamos hacer un webscraping a instragram pero no es recomendado por la proteccion de html con js dinamico que tiene y adicional necesita de selenium para simular un navegador.

#usaremos la libreria de instaloader para obtener datos, no es necesario iniciar sesion si son consultas rapidas y viene optimizada para evitar los bloqueos por instagram
#documentacion de la libreria https://instaloader.github.io/as-module.html

##################TENER EN CUENTA: como es un perfil publico y extraemos informacion publica podemos hacer la extraccion de datos, si fuera extraccion de datos personales podria violar los terminos de uso y puede bloquear la cuenta o ip##################

import instaloader
import re
import os
from dotenv import load_dotenv
from itertools import islice
import pandas as pd

#carga variables desde .env
load_dotenv()
usuario = os.getenv("INSTAGRAM_USER")
contraseña = os.getenv("INSTAGRAM_PASS")

#lista de las cuentas que se van a extraer la informacion, usaremos la cuenta creada para ver el ejemplo cuando tengan numero y correo en la biografia
cuentas=["elcorteingles","mercadona","carrefoures","ejemplo_para_prueba"]

def get_perfil_instagram(perfil_cuenta:str):
    """Esta funcion realizara el ingreso a un perfil de instagram, lo descargara y podremos extraer cierta informacion requerida

    Args:
        perfil_cuenta (str): nombre del perfil al que vamos a consultar

    Returns:
        resultado (dict): este sera el resultado de la extraccion de los datos del perfil 
    """
    try:
        #creamos una instacia de instaloader
        loader = instaloader.Instaloader()
        
        #realizamos la validacion de si ya se inicio sesion para usar el login creado y evitar multiples logueos
        try:
            #cargamos la sesion que fue previamente guardada
            loader.load_session_from_file(usuario)
        except FileNotFoundError:
            #si no encuentra la sesion crea una y la guarda para usar, esto con el fin de que se haga solo una vez por uso de codigo
            loader.login(usuario, contraseña)
            loader.save_session_to_file()
            
        #descargamos el perfil del usuario ya debe tenerlo previamente
        perfil = instaloader.Profile.from_username(loader.context, perfil_cuenta)
        
        #extraemos la informacion de la biografia
        biografia= perfil.biography
        
        #con la libreria re podemos buscar correo y teléfono en la biografia
        correos = re.findall(r'[\w\.-]+@[\w\.-]+',biografia)
        telefonos = re.findall(r'\+?\d[\d\s\-]{7,}\d',biografia)
        
        #si encuentra correos en la biografia dara una lista con un elemento
        if correos:
            correo=correos[0]
        #si no encuentra correos en la biografia dara una lista vacia 
        else:
            correo="No hay correo en la biografica"
        
        #si encuentra telefonos en la biografia dara una lista con un elemento
        if telefonos:
            telefono=telefonos[0]
        #si no encuentra telefonos en la biografia dara una lista vacia 
        else:
            telefono="No hay telefono en la biografica"
        
        #manejamos este bloque de error para validar ya que al hacer varias solicitudes instagram bloqueara la solicitud
        try:
            #get_posts devuelve un iterador que se carga publicaciones conforme se consume 
            publicaciones = perfil.get_posts()
            if publicaciones:
                #haremos un for con islice para traer solo 1 publicacion esto traera la ultima 
                for post in islice(publicaciones, 1):
                    fecha_ultima_publicacion=post.date_utc.strftime("%Y-%m-%d")
            else:
                fecha_ultima_publicacion="No existen publicaciones para sacar fecha"
        except Exception as e:
            #si bloquea las solicitudes da un error 401 
            fecha_ultima_publicacion="No pudimos sacar la informacion de fecha del ultimo post"
        
        #estructura en diccionario para facilidad de manipulacion
        respuesta={
            "username": perfil.username,
            "seguidores": perfil.followers,
            "telefono": telefono,
            "correo": correo,
            "fecha_ultima_publicacion": fecha_ultima_publicacion,
        }
        
        return respuesta
    except Exception as e:
        print(f"Error procesando {perfil_cuenta}: {e}","tipo de error:",type(e))

#creamos una lista vacia para almacenar los diferentes resultados de equipos
lista_vacia_datos=[]

#iteramos sobre cada una de las cuentas solicitadas
for perfil_cuenta in cuentas:
    #llamamos la funcion creada
    respuesta=get_perfil_instagram(perfil_cuenta)
    #añadimos las respuestas a la lista
    lista_vacia_datos.append(respuesta)
    
#convertimos los datos en un dataframe
df = pd.DataFrame(lista_vacia_datos)

#guardamos en un archivo excel en la carpeta
df.to_excel("perfiles_instagram.xlsx", index=False)

