# Crea una aplicación en Python que:
# • Use algun módulo gráfico para mostrar una ventana de login.
# • Utilice una base de datos SQLite para validar si el usuario está registrado.
# • Si el usuario no existe, puede mostrar un mensaje de error (no se requiere registrar
# usuarios).
# • Al hacer login correctamente, se muestre información proveniente de una API
# pública, por ejemplo: (Api del clima, Api de Rick and Morty o a su eleccion)

# ACLARACION: se puede hacer el modulo grafico con tkinter pero para mostrar algo diferente usare libreria de componentes llamada Dash mantine components
# permite construir rápidamente interfaces web modernas con validación, sin salir del entorno Python tengo experiencia ya que la usaba en mi anterior trabajo
# pagina de uso https://www.dash-mantine-components.com/

import requests
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from dash import Dash, Output, Input, html, callback,State,no_update
from dash_iconify import DashIconify
import dash
#traemos las funciones de validar_usuario e iniciar_base para el funcionamiento del sql
from backend_conexion_sql import validar_usuario, inicializar_base

inicializar_base()
#datos de usuario creado: santiago, contraseña: 12345

dash._dash_renderer._set_react_version("18.2.0")
app = Dash()

app.title = "Ejercicio Login con bases de datos"
#parte visual de la pagina
app.layout = dmc.MantineProvider(
    children=[
        dmc.NotificationProvider(),
        html.Div(id="espacio_notificacion"),
        dmc.Flex(
            h="100vh",
            w="100%",
            justify="center",
            align="center",
            direction="column",
            gap="xl",
            id="contenido_dinamico_principal",
            children=[
                dmc.Title("Iniciar sesión", order=1),
                #input del usuario a ingresar
                dmc.TextInput(id="usuario", label="Usuario", placeholder="Ingresa tu nombre de usuario",w="50%"),
                #input de la contrasena a usar
                dmc.PasswordInput(id="contrasena", label="Contraseña", placeholder="Ingresa tu contraseña",w="50%"),
                dmc.Button("Login",id="btn_continuar",n_clicks=0,w="10%",variant="gradient",gradient={"from": "red", "to": "pink"},),
            ]
        )]
)

#callback para la ejecucion del bloque 
@callback(
    #id donde retorna la info
    Output("contenido_dinamico_principal", "children"),
    #id donde retorna la notificacion
    Output("espacio_notificacion", "children"),
    #interaccion del boton para activar el callback
    Input("btn_continuar", "n_clicks"),
    #valores del input usuario
    State("usuario", "value"),
    #valores del input contrasena
    State("contrasena", "value"),
)
def validar_login(n_clicks,input_usuario,input_contraseña):
    #si n_clicks es 0 no haga nada, nos aseguramos de que no se ejecute sin un click 
    if n_clicks == 0:
        raise PreventUpdate
    #aseguramos de que si se da click tenga los campos input_usuario e input_contraseña tengan informacion
    if not input_usuario or not input_contraseña:
        #si no tiene los campos en los input crea una notificacion y la muestra
        notificacion=dmc.Notification(
        title="Hace falta un campo",
        action="show",
        message="Es necesario que ingreses ambos campos para poder continuar",
        icon=DashIconify(icon="tabler:bulb-filled"),
        )  
        return no_update,notificacion
    #hacemos uso de la funcion para validar si existe el usuario ingresado
    if validar_usuario(input_usuario, input_contraseña):
        #llamamos al api publica de rick y morty
        response = requests.get("https://rickandmortyapi.com/api/character/?page=1")
        #si el status_code es 200 muestra la informacion por pantalla
        if response.status_code == 200:
            personajes = response.json()["results"][:5]
            #crea una lista simple de nombres de personajes y si se encuentran vivos
            lista = [html.Div(f"{p['name']} - {p['status']}") for p in personajes]
            notificacion=dmc.Notification(
                title="Bienvenido!!",
                action="show",
                message="Ingresaste de manera exitosa, :D",
                icon=DashIconify(icon="ic:round-celebration"),
                ) 
            return lista,notificacion
    #sino se encuentra el usuario arroja la notificicacion
    else:
        notificacion=dmc.Notification(
            title="Usuario no encontrado",
            action="show",
            message="No se encuentra informacion del usuario, valida los datos ingresados",
            icon=DashIconify(icon="tabler:bulb-filled"),
            ) 
        return no_update,notificacion

#para correr la app
if __name__ == "__main__":
    app.run(debug=True)
