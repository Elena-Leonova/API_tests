from api import Pets

pets = Pets()


def test_get_registered_and_deleted():
    status = pets.get_registered_and_deleted()
    assert status == 200


def test_get_login_token():
    status = pets.get_login_token()[1]
    token = pets.get_login_token()[0]
    assert token
    assert status == 200


def test_get_list_of_users():
    status = pets.get_list_users()[1]
    my_id = pets.get_list_users()[0]
    assert status == 200
    assert my_id


def test_get_create_pet():
    status = pets.get_create_pet()[1]
    pet_id = pets.get_create_pet()[0]
    assert status == 200
    assert pet_id


def test_get_list_of_pets():
    status = pets.get_list_of_pets()[1]
    list_of_pets = pets.get_list_of_pets()[0]
    assert status == 200
    assert list_of_pets


def test_get_like_to_pet():
    status = pets.get_like_to_pet()
    assert status == 200


def test_get_comment_to_pet():
    status = pets.get_comment_to_pet()[1]
    id_message = pets.get_comment_to_pet()[0]
    assert status == 200
    assert id_message


def test_get_pet():
    status = pets.get_pet()[1]
    description = pets.get_pet()[0]
    assert status == 200
    assert description


def test_delete_pet():
    status = pets.delete_pet()
    assert status == 200


def test_patch_pet():
    status = pets.patch_pet()[1]
    pet_id = pets.patch_pet()[0]
    assert status == 200
    assert pet_id


def test_upload_image():
    status = pets.upload_image()[1]
    link = pets.upload_image()[0]
    assert status == 200
    assert link
