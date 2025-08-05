from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path

path = Path("py.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "allanbs.88@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("allanbs.88@gmail.com", "hggpbbquxapnlseh")
    smtp.send_message(mensaje)
    print("Mensaje enviado")