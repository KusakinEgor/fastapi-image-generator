from sqladmin import ModelView
from app.models.client import Client

class UserAdmin(ModelView, model=Client):
    column_list = [Client.id, Client.email, Client.role, Client.registered_at]
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
