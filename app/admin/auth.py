from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from app.database import get_db
from app.models.client import Client, RoleClient
from sqlalchemy import select
from starlette.middleware.sessions import SessionMiddleware

class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.middlewares = [
            (SessionMiddleware, (), {"secret_key": self.secret_key})
        ]
    
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email = form.get("username")
        password = form.get("password")

        async for db in get_db():
            result = await db.execute(select(Client).where(Client.email == email))
            user = result.scalars().first()

            if user and user.role == RoleClient.ADMIN:
                from app.routes.auth import verify_password
                if verify_password(password, user.hashed_password):
                    request.session.update({"token": user.email})
                    return True
        return False
    
    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True
    
    async def authenticate(self, request: Request):
        token = request.session.get("token")

        if not token:
            return None
        
        async for db in get_db():
            result = await db.execute(select(Client).where(Client.email == token))
            user = result.scalars().first()

            if user and user.role == RoleClient.ADMIN:
                return user
        return None
