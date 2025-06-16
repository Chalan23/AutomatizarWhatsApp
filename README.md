# 🎉🎂🎁 Automatizar WhatsApp con Python, mensajes de cumpleaños.
Este proyecto automatiza el envío de mensajes de cumpleaños personalizados a tus contactos de WhatsApp utilizando Python y la librería pywhatkit.
📅 Carga una lista de contactos con sus fechas de cumpleaños desde un archivo CSV y, si la fecha coincide con el día actual, envía un saludo automáticamente a través de WhatsApp Web.

# Funcionalidades
Envío automático de saludos de cumpleaños por WhatsApp Web.
Carga de contactos desde archivo CSV.
Personalización de mensajes para cada contacto.
Compatible con formato de fecha dd-mm (ejemplo: 16-06).
Integración con pywhatkit para interactuar con WhatsApp Web.

# Tecnologías utilizadas
Python 3.x
pandas
datetime
pywhatkit

# Instrucciones de uso (Cmd / Bash)
- Instala los requisitos
pip install pywhatkit pandas
-Asegúrate de tener WhatsApp Web activo y escaneado en tu navegador.
-Ejecuta el siguiente script
python appWsp.py
-El mensaje será programado para enviarse automáticamente uno o dos minutos después.

⏰ Automatización diaria (opcional)
Puedes usar Tareas Programadas (Windows) o cron (Linux/macOS) para ejecutar el script todos los días automáticamente.
