from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ChangeUserInfoForm
from .models import AdvUser
from django.contrib.auth.views import PasswordChangeView
from .forms import RegisterUserForm
from django.core.signing import BadSignature
from .utilities import signer
from django.views.generic import UpdateView, CreateView, TemplateView, DeleteView
from django.contrib import messages
from django.contrib.auth import logout





def index(request):
    return render(request, 'main/index.html')

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404("Template does not exist")
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
    template_name = 'main/login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_messages = 'Личные данные пользователя изменены'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_messages = 'Пароль пользователя изменен'

class RegisterUserView(CreateView):
   model = AdvUser
   template_name = 'main/register_user.html'
   form_class = RegisterUserForm
   success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
   template_name = 'main/register_done.html'

def user_activate(request, sign):
   try:
       username = signer.unsign(sign)
   except BadSignature:
       return render(request, 'main/bad_signature.html')
   user = get_object_or_404(AdvUser, username=username)
   if user.is_activated:
       template = 'main/user_is_activated.html'
   else:
       template = 'main/activation_done.html'
       user.is_activated = True
       user.is_active = True
       user.save()
   return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        if request.POST.get('confirm') == 'yes':
            response = super().post(request, *args, **kwargs)

            logout(request)

            messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
            return response

        messages.add_message(request, messages.WARNING, 'Удаление отменено')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        return get_object_or_404(queryset, pk=self.user_id)

def by_rubric(request, pk): pass











