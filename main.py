from user import User

user1 = User('Tyler', 'Maxwell', 'tdog@aol.com', 39)
user2 = User('Buddy', 'Reed', 'bdog@gmail.com', 24)
user3 = User('Ryan', 'Roesing', 'rdog@earthlink.net', 25)

user1.display_info()
user1.enroll()
user1.display_info()

user1.spend_points(50)
user2.enroll()
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()
