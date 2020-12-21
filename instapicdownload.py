import instaloader
mod=instaloader.Instaloader()
a=input("Enter username--> ")
mod.download_profile(a,profile_pic_only=True)

