from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from .module_path import CONFIG_PATH
import yaml
import datetime
import traceback


def loads_mail_config():
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.load(f.read())
        return config


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(contents, name):
    mail_config = loads_mail_config()
    from_addr = mail_config['account']
    password = mail_config['password']
    smtp_server = mail_config['SMTP']
    smtp_port = mail_config['port']

    to_addr = mail_config['receiver']

    to_name = '{name} <%s>'.format(name = name)

    msg = MIMEText(contents.strip(), 'html', 'utf-8')
    msg['From'] = _format_addr('CFA <%s>' % from_addr)
    msg['To'] = _format_addr(to_name % to_addr)
    msg['Subject'] = Header('期货从业资格成绩', 'utf-8').encode()
    server = None

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())

    except BaseException:
        print(datetime.datetime.now().isoformat())
        traceback.print_exc()

    finally:
        if server is not None:
            server.quit()
