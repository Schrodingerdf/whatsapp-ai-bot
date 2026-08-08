from app.services.state import StateManager
from app.services.gemini import GeminiService
from app.config import ASESOR_PHONE
from app.config import ASESOR_LINK


class ChatBot:

    def __init__(self):
        self.state = StateManager()
        self.gemini = GeminiService()

    def process(self, phone: str, user_message: str):

        text = user_message.strip().lower()

        current_state = self.state.get_state(phone)

        # Actualizar actividad del usuario
        self.state.touch(phone)

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
                    "3️⃣ Alquiler de SoftPlay\n"
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
                    "👨‍💼 *Atención personalizada*\n\n"
                    "¡Gracias por comunicarte con *Kusi Celebration*! 💛\n\n"
                    "Será un gusto atenderte de manera personalizada y ayudarte con cualquier consulta, cotización o pedido.\n\n"
                    "📲 *Haz clic en el siguiente enlace para conversar directamente con uno de nuestros asesores:*\n\n"
                    f"{ASESOR_LINK}"
                )

            elif text == "5":

                self.state.set_state(phone, "IA")

                return (
                    "🤖 Bienvenido al Asistente IA de Kusi Celebration.\n\n"
                    "Puedes hacerme cualquier pregunta y haré lo posible por ayudarte.\n\n"
                    "💬 Escribe tu pregunta.\n\n"
                    "0️⃣ Volver al menú principal."
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

            mensaje = (
                "Hola, vengo desde el chatbot de Kusi Celebration y me gustaría recibir más información."
            )

            mensaje = mensaje.replace(" ", "%20")

            link = f"https://wa.me/{ASESOR_PHONE}?text={mensaje}"

            return (
                "👨‍💼 *Seguimos aquí para ayudarte.*\n\n"
                "Si deseas conversar con un asesor, utiliza el siguiente enlace:\n\n"
                f"{link}\n\n"
                "0️⃣ Volver al menú principal."
            )

        # ==================================================
        # IA
        # ==================================================
        elif current_state == "IA":

            if text == "0":
                self.state.reset_state(phone)
                return self.process(phone, "hola")

            respuesta = self.gemini.ask(user_message)

            return (
                f"🤖 {respuesta}\n\n"
                "━━━━━━━━━━━━━━\n"
                "💬 Puedes seguir preguntándome.\n"
                "0️⃣ Volver al menú principal."
            )

        return "😊 Escribe *Hola* para iniciar la conversación."