from typing import List, Optional

from pydantic import BaseModel, Field


class AIResult(BaseModel):

    # ==================================================
    # INTENCION
    # ==================================================

    intencion: Optional[str] = None

    # ==================================================
    # PRODUCTO
    # ==================================================

    producto: Optional[str] = None

    # ==================================================
    # TEMATICAS
    # ==================================================

    tematicas: List[str] = Field(
        default_factory=list
    )

    # ==================================================
    # PERSONALIZACION
    # ==================================================

    personalizacion: bool = False

    cambios: List[str] = Field(
        default_factory=list
    )

    # ==================================================
    # OPCION DE INVITACION
    # ==================================================

    tipo_invitacion: Optional[str] = None

    # ==================================================
    # INTENCIONES COMERCIALES
    # ==================================================

    consulta_precio: bool = False

    negociacion: bool = False

    acepta: bool = False

    comprobante_pago: bool = False

    consulta_estado_pedido: bool = False

    solicita_correccion: bool = False

    reclamo: bool = False

    devolucion: bool = False

    problema_pago: bool = False

    requiere_asesor: bool = False