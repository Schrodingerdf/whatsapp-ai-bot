from typing import Optional, List, Literal

from pydantic import BaseModel, Field


class AIResult(BaseModel):

    producto: Optional[
        Literal[
            "INVITACIONES",
            "POLOS_CUMPLEAÑOS",
            "TATUAJES",
            "POLOS_TEMATICOS"
        ]
    ] = None

    tematica: Optional[str] = None

    clasificacion_diseno: Optional[
        Literal[
            "CATALOGO",
            "NO_CATALOGO",
            "MIX"
        ]
    ] = None

    tipo_invitacion: Optional[
        Literal[
            "PREMIUM",
            "CLASICA"
        ]
    ] = None

    cambios: List[str] = Field(default_factory=list)

    intencion: Optional[str] = None

    consulta_precio: bool = False

    negociacion: bool = False

    consulta_tiempo_entrega: bool = False

    acepta: bool = False

    comprobante_pago: bool = False

    consulta_estado_pedido: bool = False

    solicita_correccion: bool = False

    pedido_confirmado: bool = False

    reclamo: bool = False

    devolucion: bool = False

    problema_pago: bool = False

    requiere_asesor: bool = False