from django.test import TestCase
from model_mommy import mommy


class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    # verificar se está retornando o nome correto
    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    # verificar se está retornando o nome correto
    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    # verificar se está retornando o nome correto
    def test_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)
