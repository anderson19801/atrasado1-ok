from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name= 'Anderson', cpf='12345678901',
                    email='b166er1980@hotmail.com', phone='21 2222-2222',)
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subsject(self):
        #email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        #email = mail.outbox[0]
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        #email = mail.outbox(0)
        expect = ['contato@eventex.com.br', 'b166er1980@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        #email = mail.outbox[0]

        self.asserIn('Anderson Martins', self.email.body)
        self.asserIn('12345678901', self.email.body)
        self.asserIn('b166er1980@hotmail.com', self.email.body)
        self.asserIn('21 2222-2222', self.email.body)