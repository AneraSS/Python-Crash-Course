# make a separate file:
from admin import Admin

# make an "Admin" instance
new_user = Admin ('Anera', 'Svarc', 32, 'female', ["can add post", "can delete post"])

# call "show_privileges()" to how that everything is working correctly
new_user.show_privileges()