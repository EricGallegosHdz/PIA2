from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib, ssl
import getpass


def Correo():
    remit = input("Correo remitente: ")
    password = getpass.getpass("Contraseña: ")

    destino = input("Correo destino: ")
    asunto = input("Asunto: ")

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = remit
    mensaje["To"] = destino

    html = f"""
    <html>
    <body>
        Buen día,
	
	Espero que te encuentres bien no es phishing 
	solo es mi PIA de Programacion jaja

    </body>
    </html>
    """

    parte_html = MIMEText(html, "html")
    mensaje.attach(parte_html)

    arc = input("Path del archivo: ")

    with open(arc, "rb") as adj:
        contenido_adj = MIMEBase("application", "octet-stream")
        contenido_adj.set_payload(adj.read())

    encoders.encode_base64(contenido_adj)

    contenido_adj.add_header(
        "Content-Disposition",
        "attachment; filename= {arc}",
    )

    mensaje.attach(contenido_adj)
    text = mensaje.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(remit, password)
        server.sendmail(remit, destino, text)
        print("Correo enviado")