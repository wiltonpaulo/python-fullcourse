class User:
    def __init__(self, user_email, name, password, current_job_tittle):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_tittle = current_job_tittle

    def change_password(self, new_password):
        self.password = new_password

    def change_job_tittle(self, new_job_tittle):
        self.current_job_tittle = new_job_tittle

    def get_user_info(self):
        print(
            f"User {self.name} currently works as {self.current_job_tittle}. You can contact them at {self.email}")
