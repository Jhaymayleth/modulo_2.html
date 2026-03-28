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
        cur.execute("INSERT INTO transacciones (operacion, monto, saldo, fecha) VALUES (?, ?, ?, ?)",
                   ("Saldo inicial", 0.0, saldo_inicial, fecha))  # ✅ Monto = 0.0
    conn.commit()
    conn.close()
    
def get_saldo_actual():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT saldo FROM transacciones ORDER BY id DESC LIMIT 1")
    result = cur.fetchone()
    conn.close()
    return result[0] if result else 1000.0

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
    cur.execute("SELECT id, operacion, monto, saldo, fecha FROM transacciones ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()
    conn.close()
    print("\n=== HISTORIAL DE OPERACIONES (últimas 10) ===")
    if not rows:
        print("No hay transacciones.")
    else:
        for row in rows:
            monto_fmt = row[2] if row[2] is not None else 0.0  # ✅ Manejo None
            print(f"#{row[0]:2d}: {row[1]:12} ${monto_fmt:8.2f} → ${row[3]:6.2f} | {row[4]}")
    print("=======================================")

# INICIALIZAR
init_db()
saldo = get_saldo_actual()
print("===Bienvenido a TechBanck Riwi Digital===")
input("Presiona Enter para continuar...")

continuar = True
while continuar:
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
            continuar = False
        else:
            print("Opción inválida.")
    except ValueError:
        print("Ingrese un número válido.")

    saldo = get_saldo_actual()
    