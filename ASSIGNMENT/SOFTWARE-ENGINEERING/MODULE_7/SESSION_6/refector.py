class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, follower):
        super().__init__(username, email)
        self.follower = follower


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, follower, badge):
        super().__init__(username, email, follower)
        self.badge = badge

    # Helper method
    def format_followers(self):
        if self.follower >= 1_000_000:
            return f"{self.follower / 1_000_000:.1f}M"
        elif self.follower >= 1_000:
            return f"{self.follower / 1_000:.1f}K"
        else:
            return str(self.follower)

    # Instagram profile display
    def display_profile(self):
        badge_status = "Verified " if self.badge else "Not Verified"


        print(f"Username  : @{self.username}")
        print(f"Followers : {self.format_followers()}")
        print(f"Badge     : {badge_status}")


# Object
obj = VerifiedInfluencer("parth_navapariya", "parth@gmail.com", 1500000, True)
obj.display_profile()