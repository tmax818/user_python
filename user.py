class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        """Have this method print all the user's details on separate lines."""
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        """Have this method change the user's member status to True and set their gold card points to 200."""
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        """have this method decrease the user's points by the amount specified."""
        self.gold_card_points -= amount
