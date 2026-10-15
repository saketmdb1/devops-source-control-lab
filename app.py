def get_message():
    return "Hello from DevOps!"


def login(username):
    if not username:
        raise ValueError("Username is required")

    return f"Welcome, {username}!"


if __name__ == "__main__":
    print(get_message())