# following the single responsibility
# only doing user management
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def display_users(self):
        for user in self.users:
            print(user)

u1 = UserManager()
u1.add_user('sahil')
u1.add_user('himanshu')
u1.display_users()

# Violating the SRP as it is doing user management and i/o operations also
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        self.save_to_file()

    def remove_user(self, user):
        self.users.remove(user)
        self.save_to_file()

    def display_users(self):
        for user in self.users:
            print(user)

    def save_to_file(self):
        with open("users.txt", "w") as file:
            for user in self.users:
                file.write(user + "\n")

# applying SRP in above scenario
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def display_users(self):
        for user in self.users:
            print(user)


class UserFileStorage:
    @staticmethod
    def save_to_file(users):
        with open("users.txt", "w") as file:
            for user in users:
                file.write(user + "\n")

