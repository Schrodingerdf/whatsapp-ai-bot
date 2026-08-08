from app.services.state import StateManager
from app.services.gemini import GeminiService
from app.config import ASESOR_PHONE, ASESOR_LINK


class ChatBot:

    def __init__(self):

        self.state = StateManager()
        self.gemini = GeminiService()

    # ==================================================
    # PROCESAR MENSAJE
    # ==================================================

    def process(self, phone: str, user_message: str):

        text = user_message.strip().lower()

        # ==================================================
        # OBTENER ESTADO
        # ==================================================

        current_state = self.state.get_state(phone)

        # Actualizar actividad
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
            # SALUDO
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
            # OPCIONES NUMERICAS
            # ----------------------------------------------

            elif text == "1":

                self.state.set_state(
                    phone,
                    "TARJETAS"
                )

                return (
                    "🎂 *Tarjetas de cumpleaños*\n\n"
                    "Tenemos tarjetas personalizadas para toda ocasión.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "2":

                self.state.set_state(
                    phone,
                    "POLOS"
                )

                return (
                    "👕 *Polos personalizados*\n\n"
                    "Personalizamos polos para cumpleaños, "
                    "empresas y eventos.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "3":

                self.state.set_state(
                    phone,
                    "SOFTPLAY"
                )

                return (
                    "🎈 *Alquiler de SoftPlay*\n\n"
                    "Contamos con diferentes tamaños y temáticas.\n\n"
                    "0️⃣ Volver al menú principal"
                )

            elif text == "4":

                return self.activar_asesor(phone)

            elif text == "5":

                self.state.set_state(
                    phone,
                    "IA"
                )

                return (
                    "🤖 *Bienvenido al Asistente IA de "
                    "Kusi Celebration.*\n\n"
                    "Puedes hacerme cualquier pregunta sobre "
                    "nuestros productos y servicios.\n\n"
                    "💬 Escribe tu pregunta.\n\n"
                    "0️⃣ Volver al menú principal."
                )

            # ----------------------------------------------
            # MENSAJE LIBRE → GEMINI
            # ----------------------------------------------

            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # TARJETAS
        # ==================================================

        elif current_state == "TARJETAS":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

            return (
                "🎂 *Tarjetas de cumpleaños*\n\n"
                "Muy pronto mostraremos nuestro catálogo completo.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # POLOS
        # ==================================================

        elif current_state == "POLOS":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

            # Permitir preguntas libres dentro del flujo
            return self.procesar_con_ia(
                phone,
                user_message
            )

        # ==================================================
        # SOFTPLAY
        # ==================================================

        elif current_state == "SOFTPLAY":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

            return (
                "🎈 *Alquiler de SoftPlay*\n\n"
                "Muy pronto podrás ver todos nuestros paquetes.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # INVITACIONES
        # ==================================================

        elif current_state == "INVITACIONES":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

            return self.procesar_invitacion(
                phone,
                user_message
            )

        # ==================================================
        # ASESOR
        # ==================================================

        elif current_state == "ASESOR":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

            return self.link_asesor()

        # ==================================================
        # IA
        # ==================================================

        elif current_state == "IA":

            if text == "0":

                self.state.reset_state(phone)

                return self.process(
                    phone,
                    "hola"
                )

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

        return self.process(
            phone,
            "hola"
        )

    # ==================================================
    # GEMINI
    # ==================================================

    def procesar_con_ia(
        self,
        phone: str,
        user_message: str
    ):

        print("=" * 60)
        print("ENVIANDO MENSAJE A GEMINI")
        print("MENSAJE:", user_message)
        print("=" * 60)

        result = self.gemini.classify(
            user_message
        )

        print("=" * 60)
        print("RESULTADO IA")
        print(result.model_dump())
        print("=" * 60)

        # ==================================================
        # ASESOR
        # ==================================================

        if result.requiere_asesor:

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
        # RECLAMO / DEVOLUCION / PAGO
        # ==================================================

        if (
            result.reclamo
            or result.devolucion
            or result.problema_pago
        ):

            return self.activar_asesor(
                phone
            )

        # ==================================================
        # INVITACIONES
        # ==================================================

        if result.producto == "INVITACIONES":

            self.state.set_state(
                phone,
                "INVITACIONES"
            )

            return self.procesar_invitacion(
                phone,
                user_message,
                result
            )

        # ==================================================
        # POLOS
        # ==================================================

        if result.producto == "POLOS_CUMPLEAÑOS":

            self.state.set_state(
                phone,
                "POLOS"
            )

            return (
                "👕 *Polos personalizados* 🎉\n\n"
                "¡Perfecto! Podemos ayudarte con polos "
                "personalizados para cumpleaños.\n\n"
                "Cuéntame qué diseño o temática tienes "
                "en mente. 😊\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # POLOS TEMATICOS
        # ==================================================

        if result.producto == "POLOS_TEMATICOS":

            self.state.set_state(
                phone,
                "POLOS"
            )

            return (
                "👕 *Polos temáticos* 🎨\n\n"
                "¡Perfecto! Cuéntame qué temática tienes "
                "en mente y te ayudaremos con tu solicitud.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # ==================================================
        # TATUAJES
        # ==================================================

        if result.producto == "TATUAJES":

            return (
                "🎨 *Tatuajes temporales*\n\n"
                "¡Claro! Podemos ayudarte con información "
                "sobre nuestros tatuajes temporales.\n\n"
                "Para darte información específica, "
                "puedes conversar con uno de nuestros asesores:\n\n"
                f"{ASESOR_LINK}"
            )

        # ==================================================
        # CONSULTA DE PRECIO SIN DATOS CONFIGURADOS
        # ==================================================

        if result.consulta_precio:

            return (
                "😊 Claro. Para darte el precio exacto y "
                "actualizado, uno de nuestros asesores "
                "puede ayudarte:\n\n"
                f"{ASESOR_LINK}"
            )

        # ==================================================
        # NO SE PUDO DETERMINAR
        # ==================================================

        return (
            "😊 Claro, puedo ayudarte con Kusi Celebration.\n\n"
            "Puedes indicarme qué producto estás buscando, "
            "por ejemplo:\n\n"
            "🎂 Invitaciones\n"
            "👕 Polos personalizados\n"
            "🎨 Tatuajes\n"
            "🎈 SoftPlay\n\n"
            "También puedes escribir *asesor* si deseas "
            "hablar con una persona."
        )

    # ==================================================
    # INVITACIONES
    # ==================================================

    def procesar_invitacion(
        self,
        phone: str,
        user_message: str,
        result=None
    ):

        if result is None:

            result = self.gemini.classify(
                user_message
            )

        # --------------------------------------------------
        # NEGOCIACION
        # --------------------------------------------------

        if result.negociacion:

            return self.activar_asesor(
                phone
            )

        # --------------------------------------------------
        # MODIFICACION / MIX
        # --------------------------------------------------

        if result.clasificacion_diseno == "MIX":

            cambios = result.cambios

            if cambios:

                cambios_texto = ", ".join(
                    cambios
                )

                return (
                    "✨ *¡Perfecto!* 🥳\n\n"
                    "Podemos tomar como referencia el "
                    "diseño que te gustó y realizar "
                    "modificaciones.\n\n"
                    f"📝 Cambios solicitados: "
                    f"{cambios_texto}\n\n"
                    "Un asesor podrá ayudarte a confirmar "
                    "los detalles y realizar la cotización. 😊\n\n"
                    f"{ASESOR_LINK}\n\n"
                    "0️⃣ Volver al menú principal"
                )

            return (
                "✨ ¡Perfecto! 🥳\n\n"
                "Podemos tomar como referencia el diseño "
                "que te gustó y adaptarlo a lo que deseas. ❤️\n\n"
                "Cuéntame qué cambios te gustaría realizar.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # --------------------------------------------------
        # CATALOGO
        # --------------------------------------------------

        if result.clasificacion_diseno == "CATALOGO":

            return (
                "🎨 *Diseño de catálogo*\n\n"
                "¡Perfecto! 😊\n\n"
                "Cuéntame qué diseño del catálogo deseas "
                "para continuar con tu solicitud.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # --------------------------------------------------
        # NO CATALOGO
        # --------------------------------------------------

        if result.clasificacion_diseno == "NO_CATALOGO":

            return (
                "✨ *Diseño personalizado*\n\n"
                "¡Claro! Podemos revisar tu idea.\n\n"
                "Cuéntame qué temática o diseño tienes "
                "en mente y te ayudaremos con los detalles. 😊\n\n"
                "0️⃣ Volver al menú principal"
            )

        # --------------------------------------------------
        # TEMATICA
        # --------------------------------------------------

        if result.tematica:

            return (
                f"🎉 ¡Perfecto! Una invitación con temática "
                f"*{result.tematica}*. 😊\n\n"
                "Cuéntame si deseas un diseño del catálogo "
                "o uno personalizado.\n\n"
                "0️⃣ Volver al menú principal"
            )

        # --------------------------------------------------
        # INVITACION SIN DETALLE
        # --------------------------------------------------

        return (
            "🎂 *Invitaciones digitales*\n\n"
            "¡Perfecto! 😊\n\n"
            "Cuéntame qué temática deseas para tu "
            "invitación.\n\n"
            "Por ejemplo:\n"
            "🎈 Frozen\n"
            "🦸 Superhéroes\n"
            "🎀 Princesas\n\n"
            "0️⃣ Volver al menú principal"
        )

    # ==================================================
    # MENU PRINCIPAL
    # ==================================================

    def menu_principal(self):

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

    # ==================================================
    # ACTIVAR ASESOR
    # ==================================================

    def activar_asesor(self, phone: str):

        self.state.set_state(
            phone,
            "ASESOR"
        )

        return (
            "👨‍💼 *Atención personalizada*\n\n"
            "¡Gracias por comunicarte con "
            "*Kusi Celebration*! 💛\n\n"
            "Será un gusto atenderte de manera personalizada "
            "y ayudarte con cualquier consulta, cotización "
            "o pedido.\n\n"
            "📲 *Haz clic en el siguiente enlace para "
            "conversar directamente con uno de nuestros "
            "asesores:*\n\n"
            f"{ASESOR_LINK}"
        )

    # ==================================================
    # LINK ASESOR
    # ==================================================

    def link_asesor(self):

        mensaje = (
            "Hola, vengo desde el chatbot de Kusi Celebration "
            "y me gustaría recibir más información."
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
            "Si deseas conversar con un asesor, utiliza "
            "el siguiente enlace:\n\n"
            f"{link}\n\n"
            "0️⃣ Volver al menú principal."
        )