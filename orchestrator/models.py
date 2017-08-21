from django.db import models

class LoginUser(models.Model):
    """
    Clase con parametros para hacer login
    """
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        # evitar persistencia
        managed = False

    # override: modelo sin persistencia
    def save(self, *args, **kwargs):
        pass

class AppUser(models.Model):
    """
    Token: usuario logeado correctamente y presente en nuestro sistema
    """
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()
    user_token = models.CharField(max_length=100, primary_key=True)
    user_rights = None

    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)