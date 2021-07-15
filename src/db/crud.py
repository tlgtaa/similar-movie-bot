from .models import User


async def get_or_create_user(db, **kwargs):
    return await db.get_or_create(User, kwargs, chat_id=kwargs['chat_id'])


async def update_model(db, obj, data, keys_to_avoid=None):
    keys = ['id', 'created_at', 'updated_at']
    if keys_to_avoid and isinstance(keys_to_avoid, list):
        keys.extend(keys_to_avoid)

    update_keys = []
    for key in data.keys():
        if value := data.get(key):
            if key not in keys:
                setattr(obj, key, value)
                update_keys.append(key)

    if not update_keys:
        return

    async with db.transaction():
        await db.update(obj, only=update_keys)

    return obj


async def user_exists(db, chat_id: str):
    if await db.count(User.select().where(User.chat_id == chat_id)):
        return True

    return False
