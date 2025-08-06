from sqladmin import Admin
from fastapi import FastAPI
from app.database import engine
from app.admin.views import UserAdmin
from app.admin.auth import AdminAuth
from starlette.middleware.sessions import SessionMiddleware
from app.config import KEY

def setup_admin(app: FastAPI):
    app.add_middleware(SessionMiddleware, secret_key=KEY)

    authentication_backend = AdminAuth(secret_key=KEY)
    admin = Admin(app, engine, authentication_backend=authentication_backend)

    admin.add_view(UserAdmin)
