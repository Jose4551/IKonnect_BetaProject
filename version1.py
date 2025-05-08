import tkinter as tk
from tkinter import messagebox
import mysql.connector
from collections import Counter
import re

# Configuración de conexión a MySQL
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'tonyjok1414',
    'database': 'ikonnect'
}

# Función para ejecutar consultas SQL simples y devolver resultados
def run_query(query):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Funciones específicas para cada resumen

def total_mensajes():
    query = "SELECT COUNT(*) FROM mensajes;"
    result = run_query(query)
    return f"Cantidad total de mensajes: {result[0][0]}"


def usuarios_mensajes(mayor=True):
    order = 'DESC' if mayor else 'ASC'
    query = (
        "SELECT u.nombre, COUNT(*) AS total "
        "FROM mensajes m "
        "JOIN usuarios u ON m.usuario_id = u.id "
        "GROUP BY u.id "
        f"ORDER BY total {order} LIMIT 5;"
    )
    result = run_query(query)
    title = "Usuarios con más mensajes:" if mayor else "Usuarios con menos mensajes:"
    lines = [f"{row[0]}: {row[1]}" for row in result]
    return title + "\n" + "\n".join(lines)


def horarios_mas_activos():
    query = (
        "SELECT HOUR(enviado_at) AS hora, COUNT(*) AS total "
        "FROM mensajes "
        "GROUP BY hora "
        "ORDER BY total DESC LIMIT 5;"
    )
    result = run_query(query)
    lines = [f"{row[0]}:00 - {row[1]} mensajes" for row in result]
    return "Horas más activas:\n" + "\n".join(lines)


def palabras_frecuentes():
    query = "SELECT contenido FROM mensajes;"
    rows = run_query(query)
    all_text = ' '.join(r[0] for r in rows).lower()
    words = re.findall(r"\b\w+\b", all_text)
    counter = Counter(words)
    comunes = counter.most_common(5)
    lines = [f"{word}: {count}" for word, count in comunes]
    return "Palabras más frecuentes:\n" + "\n".join(lines)

# Configuración de la interfaz con Tkinter
root = tk.Tk()
root.title("WhatsApp Summary")
root.geometry("400x300")

# Título del proyecto
title_label = tk.Label(root, text="Resumen de Conversación WhatsApp", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Botones para cada función
btn_total = tk.Button(root, text="Total de mensajes", width=25, command=lambda: messagebox.showinfo("Total de mensajes", total_mensajes()))
btn_total.pack(pady=5)

btn_mayor = tk.Button(root, text="Usuarios más activos", width=25, command=lambda: messagebox.showinfo("Usuarios más activos", usuarios_mensajes(True)))
btn_mayor.pack(pady=5)

btn_menos = tk.Button(root, text="Usuarios menos activos", width=25, command=lambda: messagebox.showinfo("Usuarios menos activos", usuarios_mensajes(False)))
btn_menos.pack(pady=5)

btn_horas = tk.Button(root, text="Horas más activas", width=25, command=lambda: messagebox.showinfo("Horas más activas", horarios_mas_activos()))
btn_horas.pack(pady=5)

btn_palabras = tk.Button(root, text="Palabras más frecuentes", width=25, command=lambda: messagebox.showinfo("Palabras frecuentes", palabras_frecuentes()))
btn_palabras.pack(pady=5)

# Iniciar la app
root.mainloop()