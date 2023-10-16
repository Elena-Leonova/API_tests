import json
import uuid

import requests

import settings


class Pets:
    """ API library to the website http://34.141.58.52:8080/#/ """

    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"

    def get_registered_and_deleted(self) -> json:
        """ Request to Swagger to registrate and delete a user """
        e = uuid.uuid4().hex
        data = {
            "email": f'{e}@gmail.com',
            "password": '1234',
            "confirm_password": '1234'
        }
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json()['id']
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': {my_id}}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status

    def get_login_token(self) -> json:
        """ Request to Swagger to get login token """
        data = {
            "email": settings.VALID_EMAIL,
            "password": settings.VALID_PASSWORD,
        }

        res = requests.post(self.base_url + "login", data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """ Request to Swagger to get a list of users """
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + "users", headers=headers)
        my_id = res.json()
        status = res.status_code
        return my_id, status

    def get_create_pet(self) -> json:
        """ Request to Swagger to create a pet """
        data = {
            "name": "Homa",
            "type": settings.TYPE_OF_PET[3],
            "age": 1,
            "gender": ""
        }
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.post(self.base_url + "pet", data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()["id"]
        return pet_id, status

    def get_list_of_pets(self) -> json:
        """ Request to Swagger to get list of pets """
        data = {
            "name": "Koko",
            "type": settings.TYPE_OF_PET[1]
        }
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.post(self.base_url + "pets", data=json.dumps(data), headers=headers)
        status = res.status_code
        list_of_pets = res.json()
        return list_of_pets, status

    def get_like_to_pet(self) -> json:
        """ Request to Swagger to get like to the pet"""
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        res = requests.put(self.base_url + f"pet/{pet_id}/like", headers=headers)
        status = res.status_code
        return status

    def get_comment_to_pet(self) -> json:
        """ Request to Swagger to get comment to the pet"""
        data = {
            "message": "Cool!"
        }
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        res = requests.put(self.base_url + f"pet/{pet_id}/comment", data=json.dumps(data), headers=headers)
        status = res.status_code
        id_message = res.json()["id"]
        return id_message, status

    def get_pet(self):
        """ Request to Swagger to get description of the pet"""
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        res = requests.get(self.base_url + f"pet/{pet_id}", headers=headers)
        status = res.status_code
        description = res.text
        return description, status

    def delete_pet(self):
        """ Request to Swagger to delete the pet"""
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        res = requests.delete(self.base_url + f"pet/{pet_id}", headers=headers)
        status = res.status_code
        return status

    def patch_pet(self):
        """ Request to Swagger to update the pet"""
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        data = {
            "id": pet_id,
            "name": "Gosha",
            "type": settings.TYPE_OF_PET[4],
            "age": 5,
            "gender": "male",
            "owner_id": 0,
            "pic": "string",
            "owner_name": "string",
            "likes_count": 0,
            "liked_by_user": True
        }
        res = requests.patch(self.base_url + "pet", data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        return pet_id, status

    def upload_image(self):
        """ Request to Swagger to upload an image of pet"""
        my_token = Pets.get_login_token(self)[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets.get_create_pet(self)[0]
        files = {'pic': ('hamster.jpg', open(r"D:\QA_learning\MyProjects_Python\API_tests\tests\Photo\hamster.jpg",
                                             'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f"pet/{pet_id}/image", headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return link, status
