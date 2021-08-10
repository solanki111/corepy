""" script to send email alerts in case of failures """
import os
import sys
import json
import yaml
import smtplib
import logging
import datetime
import mimetypes
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CTYPE = 'CTYPE'
LOGS = 'logs'
RESOURCES = 'resources'
TIME_FORMAT = '%Y%m%d-%H%M%S'
TXT = '.txt'
CONFIG = 'configs'
CONFIGS_FILE = 'configs.yml'
CONFIG_PROP_FILE = 'property.yml'
FETCH_YAML_FAILED = 'Failed to fetch yaml file '
FILE_DOES_NOT_EXIST = 'The file or folder does not exist.  '


class Logging:
    def __init__(self):
        pass

    logs_path = os.path.join(os.path.abspath(''), RESOURCES, LOGS)
    file_name = LOGS + "_" + datetime.datetime.now().strftime(TIME_FORMAT) + TXT
    file_name_path = os.path.join(logs_path, file_name)
    logging.basicConfig(filename=file_name_path, filemode='w', format='%(asctime)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)
    logger = logging


logs_path = os.path.join(os.path.abspath(''), RESOURCES, LOGS)
file_name = LOGS + "_" + datetime.datetime.now().strftime(TIME_FORMAT) + TXT
file_name_path = os.path.join(logs_path, file_name)
logging.basicConfig(filename=file_name_path, filemode='w', format='%(asctime)s - %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)


def get_property_file(file_type):
    """
        Function to read property yaml file.
        :param file_type:
    """
    base_path = Path(__file__).parent
    file_nam = CONFIGS_FILE if file_type == CONFIG else CONFIG_PROP_FILE
    config_file = str(Path(base_path).joinpath(file_nam))
    yml_data = ''
    try:
        with open(str(config_file), 'r') as f:
            yml_data = yaml.safe_load(f)

    except FileNotFoundError as error:
        Logging.logger.error(FETCH_YAML_FAILED + config_file +
                             ' ' + error.__str__())
    except IOError as ex:
        Logging.logger.error(FETCH_YAML_FAILED + config_file +
                             ' ' + ex.__str__())
    return yml_data


def set_email_contents(prop_file, text):
    """
        Function to configure required email contents.
        :param prop_file:
        :param text:
    """
    msg = MIMEMultipart()
    recipients = prop_file.get('EMAIL_RECIPIENTS')
    msg['From'] = prop_file.get('EMAIL_SENDER')
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = prop_file.get('EMAIL_SUBJECT')
    body = prop_file.get('EMAIL_BODY') + '\n' + text
    msg.attach(MIMEText(body, "plain"))
    return msg


def email_notification(text):
    """
        Function to send out email alert with text msg and logs as an attachment
        :param text:
    """
    prop_file = get_property_file('')
    Logging.logger.info('Read the property file!')
    user = prop_file.get('EMAIL_USER')
    password = prop_file.get('EMAIL_PASSWORD')
    sender = prop_file.get('EMAIL_SENDER')
    to_list = prop_file.get('EMAIL_RECIPIENTS')
    file_path = Logging.file_name_path
    file_to_send = Logging.file_name
    Logging.logger.info('Preparing message for sending email notifications..')
    msg = set_email_contents(prop_file, text)
    Logging.logger.info('Message prepared!')

    ctype, encoding = mimetypes.guess_type(file_to_send)
    if ctype is None or encoding is not None:
        ctype = prop_file.get(CTYPE)

    maintype, subtype = ctype.split("/", 1)
    try:
        with open(file_path, "rb") as fp:
            Logging.logger.info('attaching logs into the email')
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=file_to_send)
            msg.attach(attachment)
            server = smtplib.SMTP(prop_file.get('SMTP_HOST'))
            server.starttls()
            server.sendmail(sender, to_list, msg.as_string())
            server.quit()
            Logging.logger.info('Email sent!')

    except smtplib.SMTPException as e:
        Logging.logger.error(prop_file.get('SMTP_ERROR') + str(e))


def get_property_file(file_type):
    """
        Function to read property yaml file.
        :param file_type:
    """
    pro_file_name = CONFIGS_FILE if file_type == CONFIG else CONFIG_PROP_FILE
    config_file = os.path.join(os.path.abspath('../'), file_name)
    Logging.logger.info('{0} file found at: {1}'.format(file_name.split('/')[1].split('.')[0], config_file))
    # data_loaded = None
    try:
        with open(str(config_file), 'r') as f:
            data_loaded = json.load(f)

    except StandardError as error:
        Logging.logger.error(FETCH_FILE_FAILED + config_file + ' ' + error.__str__())
        email_alert(FETCH_FILE_FAILED + config_file + ' ' + error.__str__())
        sys.exit('Exiting the process...')
    except IOError as ex:
        Logging.logger.error(FETCH_FILE_FAILED + config_file + ' ' + ex.__str__())
        email_alert(FETCH_FILE_FAILED + config_file + ' ' + ex.__str__())
        sys.exit('Exiting the process...')
    return data_loaded

def upload_data():




email_notification('Sending test email.. 3')
