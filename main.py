def get_user_name(user):
    return user["name"]


def make_greeting(user):
    name = get_user_name(user)
    return f"Привет, {name}!"