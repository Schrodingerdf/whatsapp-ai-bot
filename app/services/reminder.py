import asyncio

from app.config import REMINDER_SECONDS
from app.services.whatsapp import WhatsAppService


class ReminderService:

    def __init__(self):

        self.whatsapp = WhatsAppService()
        self.tasks = {}

    async def _send_reminder(self, phone: str):

        await asyncio.sleep(REMINDER_SECONDS)

        self.whatsapp.send_text(
            to=phone,
            message=(
                "😊 ¿Sigues ahí?\n\n"
                "Si necesitas ayuda para elegir un producto o resolver alguna duda,\n"
                "aquí estoy para ayudarte. 💛"
            )
        )

        self.tasks.pop(phone, None)

    def schedule(self, phone: str):

        self.cancel(phone)

        task = asyncio.create_task(
            self._send_reminder(phone)
        )

        self.tasks[phone] = task

    def cancel(self, phone: str):

        task = self.tasks.get(phone)

        if task:

            task.cancel()

            self.tasks.pop(phone, None)