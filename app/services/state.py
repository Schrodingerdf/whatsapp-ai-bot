class StateManager:

    def __init__(self):
        self.user_states = {}

    def get_state(self, phone: str):
        return self.user_states.get(phone, "MENU_PRINCIPAL")

    def set_state(self, phone: str, state: str):
        self.user_states[phone] = state

    def reset_state(self, phone: str):
        self.user_states[phone] = "MENU_PRINCIPAL"