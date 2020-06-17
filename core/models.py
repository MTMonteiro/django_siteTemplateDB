from django.db import models

from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-status-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rockete', 'Foguete'),
    )
    servico = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=13, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe',
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name: 'Funcinário'
        verbose_name_plural: 'Funcinários'

    def __str__(self):
        return self.nome


class Features(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop-phone'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Planos'),
        ('lni-leaf', 'Folha'),
    )
    POSICAO_CHOICE = (
        ('Esquerda', 'esquerda'),
        ('Direita', 'direita')
    )
    recurso = models.CharField('Recurso', max_length=50)
    descricao = models.CharField('Descrição', max_length=120)
    icone = models.CharField('Ícone', max_length=16, choices=ICONE_CHOICES)
    posicao = models.CharField('Posição', max_length=10, choices=POSICAO_CHOICE, default='Esquerda')

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso
