class User():
    is_registered = True

    def __init__(self, name, login):
        self.user_name = name
        self.user_login = login

    def describe(self):
        return f'Name: {self.user_name}, login {self.user_login}'


class Group():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        if user not in self.members:
            print(f'A new member has been added to the group {self.name}')
            self.members.append(user)

    def print_member_descriptions(self):
        print(f'Information about group members {self.name}:')
        for member in self.members:
            print(member.describe())

    def is_user_in_group(self,user):
        if user in self.members:
            print(f"User {user.user_name} is in the group")
        # Complete the method

user1 = User('Mark', 'supermarkus94')
group1 = Group('Dog Lovers')
group1.add_member(user1)
group1.is_user_in_group(user1)