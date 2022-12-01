# in a separate file call an "Admin" and call show_privelages() to show that all is OK

from multiple_modules_two import Admin

new_user = Admin('Anera', 'Svarc', 32, 'female', ["can add post", "can delete post"])
new_user.show_privileges()