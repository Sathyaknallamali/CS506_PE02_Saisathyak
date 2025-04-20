class User:
    def __init__(self, first_name, last_name, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"User  Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Creating instances of User
user1 = User("Alice", "Smith", "alice@example.com", 30, "New York")
user2 = User("Bob", "Johnson", "bob@example.com", 25, "Los Angeles")

# Calling methods for user1
user1.describe_user()
user1.greet_user()

# Calling methods for user2
user2.describe_user()
user2.greet_user()