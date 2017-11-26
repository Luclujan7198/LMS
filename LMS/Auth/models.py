from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager, PermissionsMixin, Group

class LMSUserManager(BaseUserManager):
    def create_user(self, ra, password=None, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ra, password, **extra_fields):
        user = self.create_user(ra, password, **extra_fields)
        user.save(using=self._db)

        # saving in group
        group = Group.objects.get(name='Coordenadores')
        user.groups.add(group)
        user.save()

        return user

class Usuario(AbstractBaseUser, PermissionsMixin):

    ra = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    ativo = models.BooleanField(default=True)

    objects = LMSUserManager()
    
    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome

    def has_module_perms(self, module):
        return True

    def has_perm(self, perm, obj=None):
        return True    

    @property
    def is_staff(self):
        return self.groups.filter(name='Coordenadores').exists()

class Aluno(Usuario):
    usuario_id = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column='usuario_id',
        parent_link=True
    )

    curso = models.CharField(max_length=200, blank=True, null=True)

class Professor(Usuario):
    class Meta:
        verbose_name_plural = 'professores'
        
    usuario_id = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column='usuario_id',
        parent_link=True
    )

    telefone = models.CharField(max_length=11, blank=True, null=True)