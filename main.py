from entities import Cliente, Reserva
from services import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from exceptions import SoftwareFJError, ServicioNoDisponibleError
import logging

def ejecutar_simulacion():
    clientes = []
    servicios = {
        "S1": ReservaSalas("S1", "Sala Creativa", 50.0),
        "S2": AlquilerEquipos("S2", "Laptop Gamer", 40.0),
        "S3": AsesoriaEspecializada("S3", "Consultoría Software", 100.0)
    }

    print("=== SOFTWARE FJ: INICIO DE OPERACIONES ===\n")

    # Lista de 10 intentos de operaciones (casos de éxito y falla)
    operaciones = [
        ("REG_CLIENTE", "C1", "Ana Garcia", "ana@mail.com"),      # 1. OK
        ("REG_CLIENTE", "C2", "", "error_sin_nombre"),           # 2. FAIL
        ("RESERVA", "R1", "C1", "S1", 3),                        # 3. OK
        ("RESERVA", "R2", "C1", "S2", -5),                       # 4. FAIL (Duración)
        ("REG_CLIENTE", "C3", "Pedro Picapiedra", "p@mail.com"), # 5. OK
        ("RESERVA", "R3", "C3", "S99", 2),                       # 6. FAIL (Servicio inexistente)
        ("RESERVA", "R4", "C3", "S3", 1),                        # 7. OK
        ("REG_CLIENTE", "C4", "Luis Perez", "luis@mail.com"),    # 8. OK
        ("RESERVA", "R5", "C4", "S2", 2),                        # 9. OK
        ("RESERVA", "R6", "INVALIDO", "S1", 1)                   # 10. FAIL (Objeto inválido)
    ]

    for i, op in enumerate(operaciones, 1):
        print(f"Operación #{i}: {op[0]}")
        try:
            if op[0] == "REG_CLIENTE":
                nuevo_cli = Cliente(op[1], op[2], op[3])
                clientes.append(nuevo_cli)
                print(f"   Cliente registrado con éxito.")
            
            elif op[0] == "RESERVA":
                # Buscar cliente por ID en nuestra lista
                cli_obj = next((c for c in clientes if c._id_entidad == op[2]), None)
                if not cli_obj: raise Exception("Cliente no encontrado.")
                
                # Buscar servicio
                ser_obj = servicios.get(op[3])
                if not ser_obj: raise ServicioNoDisponibleError(f"El servicio {op[3]} no existe.")
                
                res = Reserva(op[1], cli_obj, ser_obj, op[4])
                res.confirmar()

        except (SoftwareFJError, Exception) as e:
            print(f"   ❌ ERROR DETECTADO: {e}")
            logging.error(f"Falla en operación {i}: {e}")
        print("-" * 40)

if __name__ == "__main__":
    ejecutar_simulacion()
