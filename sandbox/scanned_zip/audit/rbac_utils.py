import os

def is_admin():
    admins = os.getenv("ADMIN_EMAILS", "").split(",")
    user_email = st.text_input("🔐 Enter your email to unlock admin functions:")
    return user_email in admins