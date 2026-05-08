import logging

# Configuración básica del Logger
logging.basicConfig(
    filename='sistema_errores.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema."""
    pass

class DatosInvalidadosError(SoftwareFJError):
    """Se lanza cuando los datos de entrada (nombres, correos) son incorrectos."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando la lógica de la reserva falla (ej. duración negativa)."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio solicitado no existe o no es válido."""
    pass
