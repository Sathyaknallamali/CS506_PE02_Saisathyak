class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_person(self):
        print(f"Person: {self.first_name} {self.last_name}")

class User(Person):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name)
        self.email = email

    def describe_user(self):
        self.describe_person()
        print(f"Email: {self.email}")

class Admin(User):
    def __init__(self, first_name, last_name, email, privileges):
        super().__init__(first_name, last_name, email)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin Privileges: {', '.join(self.privileges)}")

# Creating an instance of Admin
admin = Admin("Charlie", "Brown", "charlie@example.com", ["can add post", "can delete post", "can ban user"])

# Calling methods
admin.describe_user()
admin.show_privileges()