from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):

    use_in_migrations = True    

    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname=nickname
        )
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user

class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = CustomUserManager()
    
    username = models.CharField(max_length=128, null=True)
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    is_active = models.BooleanField(default=True)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)   

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['nickname']

#class User(AbstractBaseUser):

    #email = models.EmailField(max_length=254, unique=True)
    #avatar = models.FileField(upload_to="avatar", blank=True)
    #nickname = models.CharField(max_length=50, blank=False, default="")
    #favs = models.ManyToManyField("recycles.Recycle", related_name="favs", blank=True)
    #USERNAME_FIELD = 'email' 
    #REQUIRED_FIELDS = []

    #def __str__(self):
    #    return self.nickname