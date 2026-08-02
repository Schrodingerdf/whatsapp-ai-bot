from app.services.state import StateManager


class ChatBot:

    def __init__(self):
        self.state = StateManager()

    def process(self, phone: str, user_message: str):

        text = user_message.strip().lower()
        current_state = self.state.get_state(phone)

        # ==================================================
        # MENU PRINCIPAL
        # ==================================================
        if current_state == "MENU_PRINCIPAL":

            if text in ["hola", "hi", "buenas", "menu", "menú", "inicio"]:

                return (
                    "🎉 ¡Bienvenido a Kusi Celebration!\n\n"
                    "Gracias por escribirnos.\n\n"
                    "¿En qué podemos ayudarte hoy?\n\n"
                    "1️⃣ Tarjetas de cumpleaños\n"
                    "2️⃣ Polos personalizados\n"
                    "3️⃣ Alquiler de Softplay\n"
                    "4️⃣ Hablar con un asesor\n"
                    "5️⃣ Resolver dudas con nuestra IA\n\n"
                    "💬 Escribe el número de la opción que deseas."
                )

            elif text == "1":

                self.state.set_state(phone, "TARJETAS")

                return (
                    "🎂 Tarjetas de cumpleaños\n\n"
                    "Tenemos tarjetas personalizadas para toda ocasión.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "2":

                self.state.set_state(phone, "POLOS")

                return (
                    "👕 Polos personalizados\n\n"
                    "Personalizamos polos para cumpleaños, empresas y eventos.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "3":

                self.state.set_state(phone, "SOFTPLAY")

                return (
                    "🎈 Alquiler de SoftPlay\n\n"
                    "Contamos con diferentes tamaños y temáticas.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "4":

                self.state.set_state(phone, "ASESOR")

                return (
                    "👨‍💼 Un asesor se pondrá en contacto contigo en unos minutos.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "5":

                self.state.set_state(phone, "IA")

                return (
                    "🤖 Has ingresado al modo IA.\n\n"
                    "Hazme cualquier pregunta sobre nuestros productos o servicios.\n\n"
                    "Escribe 0️⃣ para volver al menú principal."
                )

            return "😊 Escribe *Hola* para iniciar la conversación."

        # ==================================================
        # TARJETAS
        # ==================================================
        elif current_state == "TARJETAS":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            return (
                "🎂 Tarjetas de cumpleaños\n\n"
                "Muy pronto mostraremos nuestro catálogo completo.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # POLOS
        # ==================================================
        elif current_state == "POLOS":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            return (
                "👕 Polos personalizados\n\n"
                "Muy pronto mostraremos nuestro catálogo completo.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # SOFTPLAY
        # ==================================================
        elif current_state == "SOFTPLAY":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            return (
                "🎈 Alquiler de SoftPlay\n\n"
                "Muy pronto podrás ver todos nuestros paquetes.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # ASESOR
        # ==================================================
        elif current_state == "ASESOR":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            return (
                "👨‍💼 Hemos registrado tu solicitud.\n"
                "Un asesor te responderá lo antes posible.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # IA
        # ==================================================
        elif current_state == "IA":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            return (
                "🤖 La IA estará disponible en el siguiente paso del proyecto.\n\n"
                "0️⃣ Volver al menú principal"
            )

        return "😊 Escribe *Hola* para iniciar la conversación."