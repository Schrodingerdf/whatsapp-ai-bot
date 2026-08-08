from datetime import datetime, timedelta

from app.config import SESSION_TIMEOUT_MINUTES


class StateManager:

    def __init__(self):
        self.user_states = {}

    def get_state(self, phone: str):

        user_data = self.user_states.get(phone)

        # Usuario nuevo
        if user_data is None:
            return "MENU_PRINCIPAL"

        last_activity = user_data["last_activity"]

        expiration_time = last_activity + timedelta(
            minutes=SESSION_TIMEOUT_MINUTES
        )

        # Verificar si la sesión expiró
        if datetime.now() >= expiration_time:

            print("=" * 60)
            print("SESION EXPIRADA")
            print("USUARIO:", phone)
            print("ESTADO ANTERIOR:", user_data["state"])
            print("=" * 60)

            self.reset_state(phone)

            return "MENU_PRINCIPAL"

        return user_data["state"]

    def set_state(self, phone: str, state: str):

        self.user_states[phone] = {
            "state": state,
            "last_activity": datetime.now()
        }

    def reset_state(self, phone: str):

        self.user_states[phone] = {
            "state": "MENU_PRINCIPAL",
            "last_activity": datetime.now()
        }