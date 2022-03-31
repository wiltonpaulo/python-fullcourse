from user import myprint
from user import User
from post import Post

app_user_one = User("wiltonpaulo@gmail.com",
                    "Wilton Paulo", "pwd1", "Devops Engineer")
app_user_one.get_user_info()

app_user_two = User("joseph@gmail.com",
                    "Joseph Climber", "pwd1", "Data Engineer")
app_user_two.get_user_info()


app_user_one.change_job_tittle("Devops engineer and trainer")
app_user_one.get_user_info()


old_post = Post("Learning python classes and objects", app_user_one.name)
new_post = Post("On a secret mission today", app_user_two.name)

old_post.get_post_info()
new_post.get_post_info()
