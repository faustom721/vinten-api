from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, ci, password, first_name, last_name, email, phone):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            ci=ci,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
