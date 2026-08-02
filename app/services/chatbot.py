from app.services.state import StateManager


class ChatBot:

    def __init__(self):
        self.state = StateManager()

    def process(self, phone: str, user_message: str):

        text = user_message.strip().lower()

        current_state = self.state.get_state(phone)

        # ===============================
        # MENU PRINCIPAL
        # ===============================
        if current_state == "MENU_PRINCIPAL":

            if text in ["hola", "hi", "buenas", "menu", "menú", "inicio"]:

                return (
                    "👋 ¡Hola! Bienvenido a IronFit 💪\n\n"
                    "Soy tu asistente virtual.\n\n"
                    "Selecciona una opción:\n\n"
                    "🛒 1. Comprar productos\n"
                    "🎉 2. Ver promociones\n"
                    "📦 3. Seguimiento de pedido\n"
                    "🏋️ 4. Rutinas de entrenamiento\n"
                    "🥗 5. Nutrición\n"
                    "👨‍💼 6. Hablar con un asesor\n"
                    "🤖 7. Pregúntale a la IA\n\n"
                    "Escribe el número de la opción."
                )

            if text == "1":

                self.state.set_state(phone, "MENU_PRODUCTOS")

                return (
                    "🛒 Catálogo IronFit\n\n"
                    "1️⃣ Muñequeras\n"
                    "2️⃣ Rodilleras\n"
                    "3️⃣ Fajas\n"
                    "4️⃣ Accesorios\n\n"
                    "0️⃣ Volver al menú principal"
                )

            return "Escribe *Hola* para iniciar."

        # ===============================
        # MENU PRODUCTOS
        # ===============================
        if current_state == "MENU_PRODUCTOS":

            if text == "1":
                return (
                    "🧤 Muñequeras IronFit\n\n"
                    "💰 Precio: S/ 39.90\n"
                    "📦 Stock disponible\n\n"
                    "0️⃣ Volver"
                )

            if text == "2":
                return (
                    "🦵 Rodilleras IronFit\n\n"
                    "💰 Precio: S/ 89.90\n"
                    "📏 Tallas: S, M, L\n\n"
                    "0️⃣ Volver"
                )

            if text == "3":
                return (
                    "🏋️ Fajas IronFit\n\n"
                    "💰 Precio: S/ 79.90\n\n"
                    "0️⃣ Volver"
                )

            if text == "4":
                return (
                    "🎽 Accesorios IronFit\n\n"
                    "Tenemos straps, cinturones y bandas.\n\n"
                    "0️⃣ Volver"
                )

            if text == "0":

                self.state.set_state(phone, "MENU_PRINCIPAL")

                return (
                    "👋 Menú principal\n\n"
                    "1️⃣ Comprar productos\n"
                    "2️⃣ Promociones\n"
                    "3️⃣ Seguimiento\n"
                    "4️⃣ Rutinas\n"
                    "5️⃣ Nutrición\n"
                    "6️⃣ Asesor\n"
                    "7️⃣ IA"
                )

            return "Selecciona una opción válida."