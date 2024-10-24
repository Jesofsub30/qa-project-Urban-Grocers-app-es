# Proyecto Urban Grocers 
Se desarrollo una serie de pruebas, para la crecaión de kit dentro de un usuario en específico. 
Se realizaron una serie de 9 pruebas divididas en: 5 pruebas positivas y 4 negativas con base en la siguiente lista de comprobación:
# Lista de comprobación:
![image](https://github.com/user-attachments/assets/615ffbfa-4a19-4fb9-9955-01fdb3fbc3e9)
# Crear nuevo usuario
Para la ejecución de estas pruebas primero se debe crear un usuario nuevo con base en los siguientes parametros

POST /api/v1/users
{
    "Content-Type": "application/json"
}

Conjunto minimo de datos para crear un usuario.

{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

Si la cuenta se ha creado correctamente se recibe la siguiente respuesta:


201 Creado
{
    authToken: 'jknnFApafP4awfAIFfafam2fma'
}



En caso contrario:

400 Bad request o sus equivalentes.

# Creacion de un nuevo kit.
La creacion de un nuevo kit requiere los siguientes parametros:

POST /api/v1/kits

Headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

kit_body = {
       "name": "a",
       "card":4
   }
Creacion exitosa de un kit:


201 Creado
{
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": null,
       "id": 7,
       "productsCount": 0
   }


   Creacion fallida de un kit:
   400 Bad request.

   # Requerimentos adicionales
   Se requiere tener instalados los siguientes paquetes en Pycharm:
   
   Requests
   
   Pytest
