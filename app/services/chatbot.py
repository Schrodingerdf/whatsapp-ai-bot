from app.services.state import StateManager
from app.services.gemini import GeminiService
from app.services.tematicas import buscar_tematicas
from app.config import ASESOR_PHONE, ASESOR_LINK


class ChatBot:

    def __init__(self):

        self.state = StateManager()
        self.gemini = GeminiService()

    # ==================================================
    # PROCESAR MENSAJE PRINCIPAL
    # ==================================================

    def process(self, phone: str, user_message: str):

        text = user_message.strip().lower()

        current_state = self.state.get_state(phone)

        # Actualizar actividad del usuario
        self.state.touch(phone)

        print("=" * 60)
        print("CHATBOT")
        print("USUARIO:", phone)
        print("ESTADO:", current_state)
        print("MENSAJE:", user_message)
        print("=" * 60)

        # ==================================================
        # MENU PRINCIPAL
        # ==================================================

        if current_state == "MENU_PRINCIPAL":

            # ----------------------------------------------
            # SALUDOS
            # ----------------------------------------------

            if text in [
                "hola",
                "hi",
                "buenas",
                "menu",
                "menú",
                "inicio"
            ]:

                return self.menu_principal()

            # ----------------------------------------------
            # INVITACIONES
            # ----------------------------------------------

            elif text == "1":

                self.state.set_state(
                    phone,
                    "INVITACIONES_TEMATICA"
                )

                return (
                    "Perfecto, mamita 🥰\n\n"
                    "¿Qué temática o personaje te interesa "
                    "para tu invitación? 🎈✨"
                )

            # ----------------------------------------------
            # POLOS
            # ----------------------------------------------

            elif text == "2":

                self.state.set_state(
                    phone,
                    "POLOS"
                )

                return (
                    "👕 *Polos personalizados para cumpleaños*\n\n"
                    "Cuéntame qué diseño o temática tienes "
                    "en mente. 😊\n\n"
                    "0️⃣ Volver al menú principal"
                )

            # ----------------------------------------------
            # TATUAJES
            # ----------------------------------------------

            elif text == "3":

                self.state.set_state(
                    phone,
                    "TATUAJES"
                )

                return (
                    "🎨 *Tatuajes temporales*\n\n"
                    "Cuéntame qué temática o personaje estás "
                    "buscando. 😊\n\n"
                    "0️⃣ Volver al menú principal"
                )

            # ----------------------------------------------
            # POLOS TEMATICOS
            # ----------------------------------------------

            elif text == "4":

                self.state.set_state(
                    phone,
                    "POLOS_TEMATICOS"
                )

                return (
                    "👕 *Polos temáticos y para fechas especiales*\n\n"
                    "Cuéntame qué temática o diseño tienes "
                    "en mente. 😊\n\n"
                    "0️⃣ Volver al menú principal"
                )

            # ----------------------------------------------
            # OTRO MENSAJE → GEMINI
            # ----------------------------------------------

            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # INVITACIONES - ESPERANDO TEMATICA
        # ==================================================

        elif current_state == "INVITACIONES_TEMATICA":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_tematica_invitacion(
                phone,
                user_message
            )

        # ==================================================
        # INVITACIONES - ESPERANDO PREMIUM / CLASICA
        # ==================================================

        elif current_state == "INVITACIONES_OPCIONES":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_opcion_invitacion(
                phone,
                user_message
            )

        # ==================================================
        # INVITACIONES - PERSONALIZACION
        # ==================================================

        elif current_state == "INVITACIONES_PERSONALIZACION":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_personalizacion(
                phone,
                user_message
            )

        # ==================================================
        # POLOS
        # ==================================================

        elif current_state == "POLOS":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # TATUAJES
        # ==================================================

        elif current_state == "TATUAJES":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # POLOS TEMATICOS
        # ==================================================

        elif current_state == "POLOS_TEMATICOS":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # ASESOR
        # ==================================================

        elif current_state == "ASESOR":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            return self.link_asesor()

        # ==================================================
        # IA
        # ==================================================

        elif current_state == "IA":

            if text == "0":

                self.state.reset_state(phone)

                return self.menu_principal()

            respuesta = self.gemini.ask(
                user_message
            )

            return (
                f"🤖 {respuesta}\n\n"
                "━━━━━━━━━━━━━━\n"
                "💬 Puedes seguir preguntándome.\n"
                "0️⃣ Volver al menú principal."
            )

        # ==================================================
        # ESTADO DESCONOCIDO
        # ==================================================

        self.state.reset_state(phone)

        return self.menu_principal()

    # ==================================================
    # PROCESAMIENTO GENERAL CON IA
    # ==================================================

    def procesar_con_ia(
        self,
        phone: str,
        user_message: str
    ):

        result = self.gemini.classify(
            user_message
        )

        print("=" * 60)
        print("RESULTADO IA")
        print(result.model_dump())
        print("=" * 60)

        # ----------------------------------------------
        # ASESOR
        # ----------------------------------------------

        if result.requiere_asesor:

            return self.activar_asesor(
                phone
            )

        # ----------------------------------------------
        # NEGOCIACION
        # ----------------------------------------------

        if result.negociacion:

            return self.activar_asesor(
                phone
            )

        # ----------------------------------------------
        # INVITACIONES
        # ----------------------------------------------

        if result.producto == "INVITACIONES":

            self.state.set_state(
                phone,
                "INVITACIONES_TEMATICA"
            )

            return self.procesar_tematica_invitacion(
                phone,
                user_message,
                result
            )

        # ----------------------------------------------
        # POLOS
        # ----------------------------------------------

        if result.producto == "POLOS_CUMPLEAÑOS":

            self.state.set_state(
                phone,
                "POLOS"
            )

            return (
                "👕 *Polos personalizados para cumpleaños*\n\n"
                "¡Perfecto! Cuéntame qué temática o diseño "
                "tienes en mente. 😊\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ----------------------------------------------
        # TATUAJES
        # ----------------------------------------------

        if result.producto == "TATUAJES":

            self.state.set_state(
                phone,
                "TATUAJES"
            )

            return (
                "🎨 *Tatuajes temporales*\n\n"
                "Cuéntame qué temática o personaje "
                "estás buscando. 😊\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ----------------------------------------------
        # POLOS TEMATICOS
        # ----------------------------------------------

        if result.producto == "POLOS_TEMATICOS":

            self.state.set_state(
                phone,
                "POLOS_TEMATICOS"
            )

            return (
                "👕 *Polos temáticos*\n\n"
                "Cuéntame qué temática o diseño tienes "
                "en mente. 😊\n\n"
                "0️⃣ Volver al menú principal"
            )

        return (
            "😊 Claro, puedo ayudarte con Kusi Celebration.\n\n"
            "Puedes indicarme qué producto estás buscando:\n\n"
            "1️⃣ Invitaciones digitales\n"
            "2️⃣ Polos personalizados\n"
            "3️⃣ Tatuajes temporales\n"
            "4️⃣ Polos temáticos"
        )

    # ==================================================
    # PROCESAR TEMATICA DE INVITACION
    # ==================================================

    def procesar_tematica_invitacion(
        self,
        phone: str,
        user_message: str,
        result=None
    ):

        # ----------------------------------------------
        # CLASIFICAR CON GEMINI
        # ----------------------------------------------

        if result is None:

            result = self.gemini.classify(
                user_message
            )

        print("=" * 60)
        print("GEMINI - TEMATICA INVITACION")
        print("MENSAJE:", user_message)
        print("RESULTADO:", result.model_dump())
        print("=" * 60)

        # ==================================================
        # ASESOR EXPLICITO
        # ==================================================

        mensajes_asesor = [
            "asesor",
            "asesora",
            "quiero hablar con un asesor",
            "quiero hablar con una asesora",
            "quiero hablar con alguien",
            "quiero hablar con una persona",
            "atención personalizada",
            "atencion personalizada",
        ]

        solicita_asesor = any(
            frase in user_message.strip().lower()
            for frase in mensajes_asesor
        )

        if solicita_asesor:

            return self.activar_asesor(
                phone
            )

        # ==================================================
        # BUSCAR TEMATICA
        # ==================================================

        if result.tematicas:

            resultados = buscar_tematicas(
                result.tematicas
            )

            print("=" * 60)
            print("BUSQUEDA DE TEMATICAS")
            print("SOLICITADAS:", result.tematicas)
            print("ENCONTRADAS:", resultados)
            print("=" * 60)

            # ==================================================
            # VARIAS TEMATICAS ENCONTRADAS
            # ==================================================

            if len(resultados) > 1:

                self.state.set_state(
                    phone,
                    "INVITACIONES_OPCIONES"
                )

                mensaje = (
                    "✨ ¡Claro, mamita! 🥰\n\n"
                    "Tenemos disponibles estas temáticas:\n\n"
                )

                for i, tematica in enumerate(
                    resultados,
                    start=1
                ):

                    mensaje += (
                        f"{i}️⃣ *{tematica['nombre']}*\n"
                        f"{tematica['link']}\n\n"
                    )

                mensaje += (
                    "💬 ¿Cuál de las opciones te gustaría? ❤️"
                )

                return mensaje

            # ==================================================
            # UNA TEMATICA ENCONTRADA
            # ==================================================

            if len(resultados) == 1:

                tematica = resultados[0]

                self.state.set_state(
                    phone,
                    "INVITACIONES_OPCIONES"
                )

                # ------------------------------------------
                # PERSONALIZACION DETECTADA
                # ------------------------------------------

                if result.personalizacion:

                    return (
                        "✨ ¡Perfecto! 🥳\n\n"
                        f"Tenemos la temática de "
                        f"*{tematica['nombre']}* disponible. ❤️\n\n"
                        "Si deseas, también podemos tomarla "
                        "como referencia y realizar las "
                        "personalizaciones que necesites. ✨\n\n"
                        "1️⃣ 💎 *PREMIUM*\n"
                        "[LINK PREMIUM]\n\n"
                        "2️⃣ 🌸 *CLÁSICA*\n"
                        "[LINK CLÁSICA]\n\n"
                        "💬 Elige *1* o *2* y luego cuéntame "
                        "qué cambios te gustaría realizar. 🥰"
                    )

                # ------------------------------------------
                # TEMATICA NORMAL
                # ------------------------------------------

                return (
                    "✨ ¡Perfecto! 🥳\n\n"
                    f"Tenemos una invitación de "
                    f"*{tematica['nombre']}* para ti. ❤️\n\n"
                    "📋 Te compartimos nuestras opciones:\n\n"
                    "1️⃣ 💎 *PREMIUM*\n"
                    "[LINK PREMIUM]\n\n"
                    "2️⃣ 🌸 *CLÁSICA*\n"
                    "[LINK CLÁSICA]\n\n"
                    "💬 ¿Cuál opción te gustaría?\n"
                    "Escribe *1* o *2*. 😊"
                )

            # ==================================================
            # TEMATICA NO ENCONTRADA
            # ==================================================

            tematica_solicitada = ", ".join(
                result.tematicas
            )

            self.state.set_state(
                phone,
                "INVITACIONES_OPCIONES"
            )

            return (
                "✨ ¡Perfecto! 🥳\n\n"
                f"Aunque actualmente no tenemos una "
                f"invitación de *{tematica_solicitada}* "
                "en nuestro catálogo, podemos prepararla "
                "para ti. ❤️\n\n"
                "Contamos con dos opciones:\n\n"
                "1️⃣ 💎 *PREMIUM*\n"
                "[LINK PREMIUM]\n\n"
                "2️⃣ 🌸 *CLÁSICA*\n"
                "[LINK CLÁSICA]\n\n"
                "De cualquiera de estas opciones podemos "
                "preparar tu temática, mamita. 🥰✨\n\n"
                "💬 Escribe *1* para Premium o *2* para Clásica."
            )

        # ==================================================
        # SI NO HAY TEMATICA
        # ==================================================

        # ----------------------------------------------
        # NO SE DETECTO TEMATICA
        # ----------------------------------------------

        return (
            "🥰 Cuéntame qué temática o personaje "
            "te interesa para tu invitación.\n\n"
            "Por ejemplo:\n"
            "🐭 Mickey\n"
            "🎮 Pokémon\n"
            "🐮 Granja de Zenón\n"
            "🎀 Princesas"
        )

    # ==================================================
    # PROCESAR PREMIUM / CLASICA
    # ==================================================

    def procesar_opcion_invitacion(
        self,
        phone: str,
        user_message: str
    ):

        text = user_message.strip().lower()

        # ==================================================
        # PREMIUM
        # ==================================================

        if text == "1":

            self.state.set_state(
                phone,
                "INVITACIONES_PERSONALIZACION"
            )

            return (
                "💎 *PREMIUM seleccionada* 🥰\n\n"
                "¡Perfecto! ❤️\n\n"
                "¿Deseas realizar algún cambio "
                "en el diseño?\n\n"
                "Si no deseas cambios, escribe *NO* "
                "y continuamos con la cotización.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # CLASICA
        # ==================================================

        if text == "2":

            self.state.set_state(
                phone,
                "INVITACIONES_PERSONALIZACION"
            )

            return (
                "🌸 *CLÁSICA seleccionada* 🥰\n\n"
                "¡Perfecto! ❤️\n\n"
                "¿Deseas realizar algún cambio "
                "en el diseño?\n\n"
                "Si no deseas cambios, escribe *NO* "
                "y continuamos con la cotización.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # SI ESCRIBE OTRA TEMATICA
        # ==================================================

        result = self.gemini.classify(
            user_message
        )

        print("=" * 60)
        print("INTERPRETANDO OPCION INVITACION")
        print("MENSAJE:", user_message)
        print("RESULTADO:", result.model_dump())
        print("=" * 60)

        # ----------------------------------------------
        # NUEVA TEMATICA
        # ----------------------------------------------

        if result.tematicas:

            return self.procesar_tematica_invitacion(
                phone,
                user_message,
                result
            )

        # ----------------------------------------------
        # ASESOR EXPLICITO
        # ----------------------------------------------

        mensajes_asesor = [
            "asesor",
            "asesora",
            "quiero hablar con un asesor",
            "quiero hablar con una asesora",
            "quiero hablar con alguien",
            "quiero hablar con una persona",
            "atención personalizada",
            "atencion personalizada",
        ]

        solicita_asesor = any(
            frase in text
            for frase in mensajes_asesor
        )

        if solicita_asesor:

            return self.activar_asesor(
                phone
            )

        # ----------------------------------------------
        # OPCION INVALIDA
        # ----------------------------------------------

        return (
            "😊 Puedes indicarme cuál prefieres:\n\n"
            "1️⃣ 💎 *Premium*\n"
            "2️⃣ 🌸 *Clásica*\n\n"
            "💬 Escribe *1* o *2*."
        )

    # ==================================================
    # PERSONALIZACION
    # ==================================================

    def procesar_personalizacion(
        self,
        phone: str,
        user_message: str
    ):

        text = user_message.strip().lower()

        result = self.gemini.classify(
            user_message
        )

        print("=" * 60)
        print("PERSONALIZACION")
        print("MENSAJE:", user_message)
        print("RESULTADO:", result.model_dump())
        print("=" * 60)

        # ==================================================
        # ASESOR EXPLICITO
        # ==================================================

        mensajes_asesor = [
            "asesor",
            "asesora",
            "quiero hablar con un asesor",
            "quiero hablar con una asesora",
            "quiero hablar con alguien",
            "quiero hablar con una persona",
            "atención personalizada",
            "atencion personalizada",
        ]

        solicita_asesor = any(
            frase in text
            for frase in mensajes_asesor
        )

        if solicita_asesor:

            return self.activar_asesor(
                phone
            )

        # ==================================================
        # NEGOCIACION
        # ==================================================

        if result.negociacion:

            return self.activar_asesor(
                phone
            )

        # ==================================================
        # NO QUIERE CAMBIOS
        # ==================================================

        if text in [
            "no",
            "no quiero",
            "ninguno",
            "ninguna",
            "sin cambios",
            "no deseo cambios"
        ]:

            return (
                "Perfecto 😊\n\n"
                "Continuemos con la cotización de tu "
                "invitación. ❤️"
            )

        # ==================================================
        # CAMBIOS DETECTADOS
        # ==================================================

        if result.cambios:

            cambios = ", ".join(
                result.cambios
            )

            return (
                "✨ ¡Perfecto! 🥰\n\n"
                "He registrado los siguientes cambios:\n\n"
                f"📝 {cambios}\n\n"
                "Ahora podemos continuar con la "
                "cotización de tu invitación. ❤️\n\n"
                "¿Deseas continuar?"
            )

        # ==================================================
        # NO SE ENTENDIO
        # ==================================================

        return (
            "🥰 Cuéntame qué cambios te gustaría "
            "realizar en tu invitación.\n\n"
            "Si no deseas realizar cambios, "
            "escribe *NO*."
        )

    # ==================================================
    # MENU PRINCIPAL
    # ==================================================

    def menu_principal(self):

        return (
            "👋 ¡Hola! 😊✨ Bienvenido(a) a "
            "*Kusi Celebrations* 💚\n\n"
            "✨ Experiencias que celebran la vida. 🎈\n\n"
            "Tenemos para ti:\n\n"
            "1️⃣ Invitaciones digitales\n"
            "2️⃣ Polos personalizados para cumpleaños\n"
            "3️⃣ Tatuajes temporales para celebraciones\n"
            "4️⃣ Polos temáticos y para fechas especiales\n\n"
            "💬 ¿En qué producto estás interesado(a)? 😊"
        )

    # ==================================================
    # ACTIVAR ASESOR
    # ==================================================

    def activar_asesor(
        self,
        phone: str
    ):

        self.state.set_state(
            phone,
            "ASESOR"
        )

        return (
            "👨‍💼 *Atención personalizada*\n\n"
            "¡Gracias por comunicarte con "
            "*Kusi Celebrations*! 💚\n\n"
            "Será un gusto atenderte de manera "
            "personalizada.\n\n"
            "📲 *Haz clic en el siguiente enlace "
            "para conversar directamente con uno "
            "de nuestros asesores:*\n\n"
            f"{ASESOR_LINK}"
        )

    # ==================================================
    # LINK ASESOR
    # ==================================================

    def link_asesor(self):

        mensaje = (
            "Hola, vengo desde el chatbot de "
            "Kusi Celebrations y me gustaría "
            "recibir más información."
        )

        mensaje = mensaje.replace(
            " ",
            "%20"
        )

        link = (
            f"https://wa.me/"
            f"{ASESOR_PHONE}"
            f"?text={mensaje}"
        )

        return (
            "👨‍💼 *Seguimos aquí para ayudarte.*\n\n"
            "Si deseas conversar con un asesor, "
            "utiliza el siguiente enlace:\n\n"
            f"{link}\n\n"
            "0️⃣ Volver al menú principal."
        )