class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.folowing = 0

    def follow(self, user):  # when this method is called, it knows the object that called it
        user.followers += 1  # when we follow a user, their followers will increase by 1.
        self.folowing += 1  # also, our following count will increase by 1.


user_1 = User("001", "andrea")
user_2 = User("002", "gisselle")  # The Constructors are useful when we need to create a lot of attributes.

user_1.follow(user_2)  # Let's say that user_1 decide to follow user_2

print(user_1.followers)  # user_1 has 0 followers
print(user_1.folowing)  # user_1 follows 1 user_2
print(user_2.followers)  # user_2 has 1 follower (user_1)
print(user_2.folowing)  # user_2 follows 0 users
