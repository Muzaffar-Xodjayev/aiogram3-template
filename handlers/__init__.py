from . import users
from . import admins


routers_list = [
    users.users.router,
    admins.start.router,
]

__all__ = [
    "routers_list",
]

