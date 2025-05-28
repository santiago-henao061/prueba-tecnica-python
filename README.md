#  Prueba de ingreso - Desarrollador Junior North Marketh

Este repositorio contiene la solucion a 3 problemas planteados

## Contenido

1. **Ejercicio 1 - Numero mas frecuente**
   - Encuentra el numero que mas veces se repite en una lista.
   - Si hay empate, devuelve el menor.

2. **Ejercicio 2 - Web Scraping**
   - Realiza scraping en MercadoLibre para extraer titulos y precios de productos.
   - Permite cambiar fácilmente la variable de busqueda.

3. **Ejercicio 3 - Login y Consumo de API**
   - Interfaz de login con Dash Mantine.
   - Validacion con SQLite.
   - Muestra datos de una API publica tras login exitoso.
  
4. **Ejercicio 4 Instagram - Scraping de Perfiles de Instagram**
   - Extrae informacion publica de un perfil de Instagram.
   - Detecta correos electronicos y telefonos dentro de la biografia.
   - Obtiene la ultima fecha de publicacion (si no ha sido bloqueado por exceso de peticiones).
   - Exporta todos los datos a un archivo Excel.

## Requisitos

- Python 3.8 o superior
- Las dependencias se listan en "requirements.txt" (solo para el modulo_ejercicio2 y modulo_ejercicio3), SE AÑADEN dependencias para (ejercicio_instagram)

## Instalacion

1. Clona este repositorio:

   ```bash
   git clone https://github.com/santiago-henao061/prueba-tecnica-python.git
   cd prueba-tecnica-python
   ```

2. Crea y activa un entorno virtual en la carpeta principal PRUEBA TECNICA:

   ```bash
   python -m venv env
   source env/bin/activate   # En Linux/macOS
   env\Scripts\activate      # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### 1. Numero mas frecuente
Ejecuta:

```bash
python modulo_ejercicio1\ejercicio1.py
```

### 2. Web Scraping

```bash
python modulo_ejercicio2\ejercicio2.py
```

### 3. Login con API

```bash
python modulo_ejercicio3\ejercicio3.py
```

### 4. Scraping a Intagram

```bash
python prueba_2_usuarios_instagram\ejercicio_instagram.py
```

## Autor

- Santiago Henao Otalora
- https://www.linkedin.com/in/santiago-henao-otalora-698804259/

