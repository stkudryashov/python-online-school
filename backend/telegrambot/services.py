from accounts.models import User
from telegrambot import keyboards


def get_user_keyboard(user: User):
    if user.type.id_name == 'teacher':
        return keyboards.TEACHER_MENU_KEYBOARD
    else:
        return keyboards.STUDENT_MENU_KEYBOARD
