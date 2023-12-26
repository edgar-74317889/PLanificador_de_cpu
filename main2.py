import random  # genera_numeros_aleatorios


class Cliente:
    def __init__(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente


class Ventanilla:
    def __init__(self, numero):
        self.numero = numero
        self.tiempo_atencion = 0
        self.tiempo_sin_atender = 0

    def atender_cliente(self, cliente):
        tiempo_atencion = random.uniform(1, 10)  # Tiempo de atención aleatorio
        self.tiempo_atencion += tiempo_atencion
        print(
            f"Ventanilla {self.numero}: Atendiendo cliente tipo {cliente.tipo_cliente} durante {round(tiempo_atencion)} minutos"
        )

    def sin_atender(self):
        veces_sin_atender = random.randint(
            1, 5
        )  # Número de veces que la ventanilla dejará de atender
        tiempo_sin_atender = random.uniform(
            5, 30
        )  # Tiempo que la ventanilla dejará de atender en cada ocasión
        self.tiempo_sin_atender += veces_sin_atender * tiempo_sin_atender
        print(
            f"Ventanilla {self.numero}: No atenderá durante un total de {veces_sin_atender} veces, por un tiempo total de {round(veces_sin_atender * tiempo_sin_atender)} minutos"
        )


def simular_atencion(num_ventanillas, num_clientes):
    ventanillas = [Ventanilla(i) for i in range(1, num_ventanillas + 1)]
    clientes = []

    for i in range(num_clientes):
        tipo_cliente = random.choices(
            ["Tarjeta", "Sin tarjeta", "Preferencial"], [0.7, 0.2, 0.1]
        )[0]
        if tipo_cliente == "Tarjeta":
            subtipo_cliente = random.choices(
                [
                    "Cuentas comunes",
                    "Personas naturales VIP",
                    "Personas jurídicas comunes",
                    "Personas jurídicas VIP",
                ],
                [0.4, 0.3, 0.15, 0.15],
            )[0]
            cliente = Cliente(f"{tipo_cliente} - {subtipo_cliente}")
        elif tipo_cliente == "Sin tarjeta":
            cliente = Cliente(tipo_cliente)
        else:
            subtipo_cliente = random.choices(
                ["Mayores de 60 años", "Deficiencia física", "Necesidades especiales"],
                [0.6, 0.2, 0.2],
            )[0]
            cliente = Cliente(f"{tipo_cliente} - {subtipo_cliente}")

        clientes.append(cliente)

    for cliente in clientes:
        ventanilla = min(
            ventanillas, key=lambda v: v.tiempo_atencion + v.tiempo_sin_atender
        )
        ventanilla.atender_cliente(cliente)
        ventanilla.sin_atender()

    total_tiempo_atencion = sum(v.tiempo_atencion for v in ventanillas)
    total_tiempo_sin_atender = sum(v.tiempo_sin_atender for v in ventanillas)
    print(
        f"\nTiempo total de atención en todas las ventanillas: {round(total_tiempo_atencion)} minutos"
    )
    print(
        f"Tiempo total de no atención en todas las ventanillas: {round(total_tiempo_sin_atender)} minutos"
    )


def main():
    num_ventanillas = int(input("Ingrese el número de ventanillas: "))
    num_clientes = int(input("Ingrese el número de clientes a simular: "))
    simular_atencion(num_ventanillas, num_clientes)


if __name__ == "__main__":
    main()