from database.models import *
from playhouse.shortcuts import model_to_dict


async def add_user(user_id, full_name, from_link=None, username=None, user_balance=0, referals=0):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username, full_name=full_name, from_link=from_link,
                         user_balance=user_balance, referals=referals)

