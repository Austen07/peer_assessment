import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from service import getMailService
from PeerReview.Logger import getLogger

log = getLogger("mail")

def SendMessage(credentials, sender, to, bcc, subject, msgHtml, msgPlain):
    """
    Sends message to the "to" and "bcc" list from sender.
    Arguments:
        credentials: access to Gmail API.
        sender: Sender of the mail
        to: Recievers of the mail
        bcc: BCCs of the mail
        subject: Subject of the mail
        msgHtml: HTML message of the mail
        msgPlain: Plain messge of the mail
    """
    service = getMailService(credentials)
    message1 = CreateMessageHtml(sender, to, bcc, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)

def SendMessageInternal(service, user_id, message):
    """
    Sends mail using Google Mail service
    Arguments:
        service: access Gmail
        user_id: UserId of sender
        message: Message of the mail
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        log.info('Mail has been sent with message Id and user Id: %s', message[u'id'], user_id)
    except errors.HttpError, error:
        log.error('An error occurred while sending message : %s', error)

def CreateMessageHtml(sender, to, bcc, subject, msgHtml, msgPlain):
    """
    Generates the html message.
    Arguments:
        sender: Sender of the mail
        to: Recievers of the mail
        bcc: BCCs of the mail
        subject: Subject of the mail
        msgHtml: HTML message of the mail
        msgPlain: Plain message of the mail
    return: 
        The HTML message compatible with Google Mail service.
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['Bcc'] = bcc
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string())}