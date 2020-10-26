from django.contrib.auth.models import BaseUserManager, Group


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, email, password, group=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError('The given Phone must be set')
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        print(group)
        user.groups.add(group)
        return user

    def create_user(self, phone, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        Group.objects.get_or_create(name="admin")
        group = Group.objects.get(name="admin")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, email, password, group, **extra_fields)
