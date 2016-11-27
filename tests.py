from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def tes_get(self):
        """get /inscricao/ must return status code 200"""
        #response = self.client.get('/inscricao/')
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """must user subscriptions/subscription_form.html"""
        #response = self.client.get('/inscricao/')
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contains input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must  contains csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 field"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name= 'Anderson', cpf='12345678901',
                    email='b166er1980@hotmail.com', phone='21 2222-2222',)
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid post should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subsject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, email.subject)
    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox(0)
        expect = ['contato@eventex.com.br', 'b166er1980@hotmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.asserIn('Anderson Martins', email.body)
        self.asserIn('12345678901', email.body)
        self.asserIn('b166er1980@hotmail.com', email.body)
        self.asserIn('21 2222-2222', email.body)


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.response = self.client.post('/inscricao/', {})
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
	def test_message(self):
		data = dict(name='Anderson Martins', cpf='12345678901',
					email='b166er1980@hotmail.com', phone='21-2222-2222')
		response = self.client.post('/inscricao/', data, follow=True)
		self.assertContains(response, 'Inscrição realizada com sucesso')




'''
class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')


    def test_get(self):
        """get/must return status code 200"""
        #response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)
        #self.assertTemplateUsed(response, 'index.html')


    def test_template(self):
        """must use index.html"""
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form)



class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Anderson', cpf='12345678901',
                    email='b166er1980@hotmail.com', phone='21 2222-2222')
        response = self.client.post('/inscricao/', data)

    def tes_post(self):
        """Valid post should redirect to /inscrição/"""
        # data = dict(name= 'Anderson', cpf= '12345678901', email= 'b166er1980@hotmail.com', phone= '21 2222-2222')
        # response = self.client.post('/inscricao/', data)
        self.assertEqual(302, response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscrition_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'b166er1980@hotmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.asserIn('Anderson Martins', email.body)
        self.asserIn('12345678901', email.body)
        self.asserIn('b166er1980@hotmail.com', email.body)
        self.asserIn('21 2222-2222', email.body)


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        # response = self.client.post('/inscricao/', {})
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, subscriptionForm)

    def test_form_has_errors(self):
        from = self.response.context['form']
        self.assertTrue(form.errors)




'''