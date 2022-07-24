import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import uteis as uteis


def enviarEmail(emails):
    # informações do servidor
    host = "smtp.gmail.com"
    port = "587"
    user = uteis.user
    password = uteis.password

    server = smtplib.SMTP(host=host, port=port)
    server.starttls()
    server.login(user=user, password=password)

    # informações do e-mail
    corpo = """
    <p>E-mail automático do <b>Seu Nome</b></p>
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = emails
    email_msg['Subject'] = "Teste envio de e-mail"
    email_msg.attach(MIMEText(corpo, 'html'))

    # colocando arquivos anexos
    # 1º arquivo
    arquivo = r'C:\Elvis\arquivo.pdf'
    arquivo_aberto = open(arquivo, 'rb')  # read and binary
    nome_do_arquivo = 'teste1'.encode('utf-8').decode('utf-8', "strict")

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(arquivo_aberto.read())
    encoders.encode_base64(att)  # transformando o arquivo em base64

    att.add_header('Content-Disposition', 'attachment', filename=f"{nome_do_arquivo}.pdf")
    arquivo_aberto.close()
    email_msg.attach(att)

    # 2º arquivo
    arquivo2 = r'C:\Elvis\arquivo2.pdf'
    arquivo_aberto2 = open(arquivo2, 'rb')  # read and binary
    nome_do_arquivo2 = 'teste2'.encode('utf-8').decode('utf-8', "strict")

    att2 = MIMEBase('application', 'octet-stream')
    att2.set_payload(arquivo_aberto2.read())
    encoders.encode_base64(att2)  # transformando o arquivo em base64

    att2.add_header('Content-Disposition', 'attachment', filename=f"{nome_do_arquivo2}.pdf")
    arquivo_aberto2.close()
    email_msg.attach(att2)

    # enviar o e-mail
    server.sendmail(from_addr=email_msg['From'], to_addrs=email_msg['To'], msg=email_msg.as_string().encode('utf-8'))
    server.quit()
    print("E-mail enviado com sucesso!")


# enviando e-mails para uma lista de e-mails
emails = ['seuemail1@gmail.com', 'seuemail2@gmail.com']
for i in emails:
    enviarEmail(i)
