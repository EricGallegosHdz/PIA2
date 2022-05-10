import subprocess
import argparse
import WebScraping
import Correo
import Metadata
import ValorHash
import Scan

parser = argparse.ArgumentParser(description='Informacion de las herramientas.')

parser.add_argument("-wS","--webScraping", help="Obtencion de informacion.", action="store_true")
parser.add_argument("-s", "--Sitio", help="Link para obtener informacion.", )

parser.add_argument("-pS","--portScan", help="Escaneo de puertos.", action="store_true")

parser.add_argument("-oM", "--obtMetadatos", help="Metadatos", action="store_true")
parser.add_argument("-r", "--ruta", help="Path del archivo para recolectar informacion")

parser.add_argument("-e", "--enviar_correo", help="Envio de correos", action="store_true")

parser.add_argument("-vH", "--valorHash", help="Valores hash.", action="store_true")
parser.add_argument("-f", "--file", help="Documento")

parser = parser.parse_args()


if parser.webScraping:
    print("WebScraping\n")
    hipervinc= parser.Hipervinc
    print("{hipervinc}")
    WebScraping.WebScrapping(hipervinc)

elif parser.valorHash:
    print("Valor Hash\n")
    ValorHash.Hash(parser.file)

elif parser.portScan:
    print("PortScanner\n")
    process = subprocess.Popen(["./PortScan.sh", "{parser.ip}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Listo")
    print(process.stdout.read())

elif parser.obtMetadatos:
    print("Obtencion de Metadatos\n")
    Metadata.printmeta(parser.ruta)

elif parser.enviar_correo:
    print("Envio de correo.\n")
    MandarCorreo.Envio_Correo()
