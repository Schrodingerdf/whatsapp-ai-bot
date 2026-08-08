from datetime import datetime, timedelta

from app.config import SESSION_TIMEOUT_MINUTES


class StateManager:

    def __init__(self):
        self.user_states = {}

    def get_state(self, phone: str):

        user_data = self.user_states.get(phone)

        # Usuario nuevo
        if user_data is None:
            print("=" * 60)
            print("USUARIO NUEVO")
            print("USUARIO:", phone)
            print("=" * 60)

            return "MENU_PRINCIPAL"

        last_activity = user_data["last_activity"]

        expiration_time = last_activity + timedelta(
            minutes=SESSION_TIMEOUT_MINUTES
        )

        now = datetime.now()

        print("=" * 60)
        print("VERIFICANDO SESION")
        print("USUARIO:", phone)
        print("ESTADO:", user_data["state"])
        print("ULTIMA ACTIVIDAD:", last_activity)
        print("AHORA:", now)
        print("EXPIRA:", expiration_time)
        print("TIMEOUT:", SESSION_TIMEOUT_MINUTES, "minutos")
        print("=" * 60)

        # ==================================================
        # SESION EXPIRADA
        # ==================================================

        if now >= expiration_time:

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

        print("=" * 60)
        print("ESTADO GUARDADO")
        print("USUARIO:", phone)
        print("ESTADO:", state)
        print("HORA:", self.user_states[phone]["last_activity"])
        print("=" * 60)

    def touch(self, phone: str):

        user_data = self.user_states.get(phone)

        if user_data:

            user_data["last_activity"] = datetime.now()

            print("=" * 60)
            print("ACTIVIDAD ACTUALIZADA")
            print("USUARIO:", phone)
            print("HORA:", user_data["last_activity"])
            print("=" * 60)

    def reset_state(self, phone: str):

        self.user_states[phone] = {
            "state": "MENU_PRINCIPAL",
            "last_activity": datetime.now()
        }

        print("=" * 60)
        print("ESTADO REINICIADO")
        print("USUARIO:", phone)
        print("NUEVO ESTADO: MENU_PRINCIPAL")
        print("=" * 60)