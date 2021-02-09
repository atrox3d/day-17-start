class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "robb")
# user1.id = "001"
# user1.username = "robb"

# print(user1.username)
# print(user1.followers)

user2 = User("002", "fab")
# user1.id = "002"
# user1.username = "fab"

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
