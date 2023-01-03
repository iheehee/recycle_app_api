from users.models import Profile
from challenges.models import Challenge

def profile(user_id):
    profile = Profile.objects.get(nickname_id=user_id)
    return profile 

def challenge(challenge_id):
    challenge = Challenge.objects.filter(id__exact=challenge_id)[0]
    return challenge

