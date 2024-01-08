import json

users = [
    {'id': 1, 'userName': 'João', 'userEmail': 'joao@email.com'},
    {'id': 2, 'userName': 'Maria', 'userEmail': 'maria@email.com'},
    {'id': 3, 'userName': 'Example', 'userEmail': 'example@email.com'}
]

def get_user_method(user_id):
    # Validate if the user exists
    user = next((user for user in users if user['id'] == user_id), None)

    return user


def test_return_user_sucess(): 
    #Arrange 
    user_id = 3
    #Act
    response = get_user_method(user_id)
    # Assert 
    assert response["id"] == user_id
    assert response["userName"] == "Example"
    assert response["userEmail"] == "example@email.com"

