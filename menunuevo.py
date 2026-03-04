import sqlite3
from datetime import datetime

DB_NAME = "techbank.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transacciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operacion TEXT,
            monto REAL,
            saldo REAL,
            fecha TEXT
        )
    ''')
    cur.execute("SELECT saldo FROM transacciones ORDER BY id DESC LIMIT 1")
    if not cur.fetchone():
        saldo_inicial = 1000.0
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO transacciones (operacion, saldo, fecha) VALUES (?, ?, ?)",
                    ("Saldo inicial", saldo_inicial, fecha))
    conn.commit()
    conn.close()
    
def get_saldo_actual():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT saldo FROM transacciones ORDER BY id DESC LIMIT 1")
    result = cur.fetchone ()
    conn.close()
    return result[0][0] if result else 1000.0

def log_transaccion(operacion, monto, saldo):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO transacciones (operacion, monto, saldo, fecha) VALUES (?, ?, ?, ?)",
                (operacion, monto, saldo, fecha_actual))
    conn.commit()
    conn.close()

def mostrar_historial():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT operacion, monto, saldo, fecha FROM transacciones ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()
    conn.close()
    print("\n=== HISTORIAL DE OPERACIONES (últimas 10) ===")
    if not rows:
        print("No hay transacciones.")
    else:
        for row in rows:
            print(f"ID {row[0]}: {row[1]} ${row[2]:.2f} → Saldo: ${row[3]:.2f} | {row[4]}")
    print("=======================================")

#INICIALIZAR
init_db()
saldo = get_saldo_actual()
print("===Bienvenido a TechBanck Riwi Digital===")
input("Presiona Enter para continuar...") #pausa inicial

continuar = True
print("===Bienvenido a TechBanck Riwi Digital===")
input("Presiona Enter para continuar...")

while continuar:  # ← REPITE MIENTRAS continuar = True
    print(f"\nSaldo actual: ${saldo:.2f}")
    print("1 - Consultar saldo")
    print("2 - Retirar dinero")
    print("3 - Depositar dinero")
    print("4 - Ver historial")
    print("5 - Salir")
    
    try:
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            print(f"Saldo actual: ${saldo:.2f}")
            log_transaccion("Consulta", 0, saldo)
        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Saldo actual: ${saldo:.2f}")
                log_transaccion("Retiro", -monto, saldo)
            else:
                print("Fondos insuficientes.")
        elif opcion == 3:
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f"Depósito exitoso. Saldo actual: ${saldo:.2f}")
            log_transaccion("Depósito", monto, saldo)
        elif opcion == 4:
            mostrar_historial()
        elif opcion == 5:
            mostrar_historial()
            print("¡Gracias por usar TechBanck Riwi Digital!")
            continuar = False  # APAGA LA BANDERA = SALE DEL BUCLE
        else:
            print("Opción inválida.")
    except ValueError:
        print("Ingrese un número válido.")

    saldo = get_saldo_actual() 