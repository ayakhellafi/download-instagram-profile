import instaloader
Bot= instaloader.Instaloader()

user='makdonuts_batna'

print(Bot.download_profile(user,profile_pic_only=True))