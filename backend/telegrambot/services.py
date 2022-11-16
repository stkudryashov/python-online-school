from accounts.models import User, UserType
from telegrambot import keyboards

from telegram import Update
from telegram.ext import CallbackContext

from telegrambot.models import BotAnswer


def get_user_keyboard(user: User):
    if user.type.id_name == 'teacher':
        return keyboards.TEACHER_MENU_KEYBOARD
    else:
        return keyboards.STUDENT_MENU_KEYBOARD


def change_user_type(update: Update, context: CallbackContext):
    if not User.objects.filter(telegram_id=update.message.chat_id).exists():
        update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)
        return

    user = User.objects.get(telegram_id=update.message.chat_id)

    if user.is_superuser:
        if context.args:
            new_type = context.args[0]

            if new_type not in list(UserType.objects.values_list('id_name', flat=True)):
                update.message.reply_text('Неверный тип пользователя 🥲')
                return

            user.type = UserType.objects.get(id_name=new_type)
            user.save()

            update.message.reply_text(
                'Успешно ❤',
                reply_markup=get_user_keyboard(user)
            )
        else:
            update.message.reply_markdown_v2(f'Тип аккаунта: `{user.type.id_name}`')
    else:
        update.message.reply_text(BotAnswer.objects.get(query='Не понимаю').text)
