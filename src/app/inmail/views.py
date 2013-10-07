import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail


class Handler(InboundMailHandler):

    def receive(self, mail_message):
        kwargs = {}
        for itm in 'html', 'attachments', 'headers':
            kwargs[itm] = getattr(mail_message, itm, None)
        # kwargs['from'] = mail_message.sender
        kwargs = {k:v for k, v in kwargs.items() if v is not None}
        logging.debug(kwargs)
        mail.send_mail('noreply@example.com', 'recipient@example.com', mail_message.subject, mail_message.body, **kwargs)


handle = webapp2.WSGIApplication([Handler.mapping()], debug=True)
