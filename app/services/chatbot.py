class ChatBot:

    def process(self, user_message: str):

        text = user_message.strip().lower()

        if text in ["hola", "hi", "buenas", "buenos días", "buenas tardes", "buenas noches"]:

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
            return (
                "🛒 Catálogo IronFit\n\n"
                "1️⃣ Muñequeras\n"
                "2️⃣ Rodilleras\n"
                "3️⃣ Fajas\n"
                "4️⃣ Accesorios\n\n"
                "Escribe el número del producto."
            )

        return (
            "No entendí tu mensaje.\n\n"
            "Escribe *Hola* para iniciar."
        )