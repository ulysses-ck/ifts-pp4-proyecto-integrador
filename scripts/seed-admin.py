from apps.Usuarios.models import User

def run():
    # create admin account
    try:
        new_admin = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
        )

        new_admin.set_password("admin123")

        print("Admin account created successfully.")
    except Exception as e:
        print(f"Error creating admin account: {e}")

if __name__ == '__main__':
    run()
