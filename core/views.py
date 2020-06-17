from django.views.generic import TemplateView
from .models import Servico, Funcionario, Features


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # order_by('?') - organizar de ordem aleatoria
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        context['recursos_esq'] = Features.objects.filter(posicao='Direita').all()
        context['recursos_dir'] = Features.objects.filter(posicao='Esquerda').all()
        return context
