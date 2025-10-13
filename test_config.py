
from project_YouGile import YouGileClient

URL = "https://ru.yougile.com/api-v2/"
LOGIN = ""
PASSWORD = ""
NAME = ""

api = YouGileClient()


def test_create_project_positive():
    api.get_companies()
    api.get_api_key()
    api.set_api_key()
    api.create_project()
    # создание проекта
    title = 'Project'

    result = api.create_project(title)

    # количество проектов после
    projects_after = api.get_project_list()

    assert result.status_code == 201
    assert projects_after[-1]['title'] == title


def test_create_project_negative():
    api.get_companies()
    api.get_api_key()
    api.create_project()
    # создание проекта
    title = 'Project'

    result = api.create_project(title)

    # количество проектов после
    projects_after = api.get_project_list()
    #проверка, без API ключа не работает
    assert result.status_code == 401


def test_get_project_with_id_positive():
    api.get_companies()
    api.get_api_key()
    api.set_api_key()
    api.get_project()
    # создание проекта
    title = 'ГосУслуги'

    result = api.create_project(title)
    project_id = result.json()['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.json()['title'] == title


def test_get_project_with_id_negative():
    api.get_companies()
    api.get_api_key()
    api.get_project()
    # создание проекта
    title = 'ГосУслуги'

    result = api.create_project(title)
    assert result.status_code == 401


def test_edit_project_positive():
    api.get_companies()
    api.get_api_key()
    api.set_api_key()
    api.create_project()
    api.update_project()
    title = 'Edit_ГосУслуги'
   
    result = api.create_project(title)

    project_id = result.json()['id']
    new_deleted = True
    new_title = 'Edited_ГосУслуги'

    edited = api.edit_project(project_id, new_deleted, new_title)
    new_project = api.get_project_with_id(project_id)

    assert edited.status_code == 200
    assert new_project.json()['title'] == new_title

def test_edit_project_negative():
    api.get_companies()
    api.get_api_key()
    api.create_project()
    api.update_project()
    title = 'Nem_Project'

    result = api.create_project(title)
    assert result.status_code == 401