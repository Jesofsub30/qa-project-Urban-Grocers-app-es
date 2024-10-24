import data
import sender_stand_request
from data import kit_body
from sender_stand_request import response


def get_kit_body(kit_name):
    current_kit = data.kit_body.copy()
    current_kit["name"] = kit_name
    return current_kit

def possitive_assert(kit_name):
    kit_body= get_kit_body(kit_name)
    kit_response=sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name

def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400


#Pruebas
# Prueba numero 1. El numero de caracteres para "name" es 1
def test_create_kit_1_character_in_name_get_success():
    possitive_assert("A")

# Prueba numero 2. El numero de caracteres para "name" es 511
def test_create_kit_511_character_in_name_get_success():
    possitive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba numero 3. El numero de caracteres para "name" es menor del permitido(0)
def test_create_kit_0_character_in_name_get_unsuccessfully_response():
    negative_assert("")

# Prueba numero 4. El numero de caracteres para "name" es mayor que el permitido (512)
def test_create_kit_512_character_in_name_get_unsuccessfully_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba numero 5. Se permiten caracteres especiales para "name"
def test_create_kit_special_character_in_name_get_success_response():
    possitive_assert( "'№%@',")

#Prueba numero 6. Se permiten espacios en "name"
def test_create_kit_has_spaces_in_name_get_success_response():
    possitive_assert(" A Aaa ")

#Prueba numero 7. Se permiten numeros en "name"
def test_create_kit_contain_numbers_in_name_get_success_response():
    possitive_assert("123")


#Prueba numero 8. El parametro no se pasa en la solicitud
def test_create_kit_512_character_in_name_get_unsuccessfully_response():
    kit_body=data.kit_body.copy()
    kit_body.pop("name")
    negative_assert("kit_body")

#Prueba numero 9. Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_use_number_type_in_first_name_get_unsuccessfully_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
