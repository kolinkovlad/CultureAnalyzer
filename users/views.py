from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import (CreateView, UpdateView, DetailView, ListView,
                                  )
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from users.forms import UserRegisterForm, UserUpdateForm, GroupForm

__all__ = [
    'LoginView',
    'UserRegisterView',
    'UserUpdateView',
    'PasswordChangeView',
    'ListGroups',
    'CreateGroup',
    'UpdateGroups',
    ]


class LoginView(auth_views.LoginView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(LoginView, self).get(request, *args, **kwargs)


class UserRegisterView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(UserRegisterView, self).get(request, *args, **kwargs)


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.pk)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.pk)

    def form_valid(self, form):
        """Try to save form, and check if image was in form,
        and after save image is None, then there is a error and we
        return error to user
        """
        if form.cleaned_data['image']:
            user = form.save()
            if not user.image:
                form.add_error('__all__', 'Image can`t be saved!')
                return super().form_invalid(form)
        else:
            form.save()
        return redirect(self.get_success_url())


class PasswordChangeView(UpdateView):
    template_name = 'users/password_change.html'
    form_class = PasswordChangeForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance')
        return kwargs


class ListGroups(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Group
    context_object_name = 'group'
    template_name = 'users/group.html'
    permission_required = 'auth.view_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # In this case, only superuser will have access
        context['can_change_permissions'] = self.request.user.has_perm(
            perm='auth.change_group')
        context['can_delete_permissions'] = self.request.user.has_perm(
            perm='auth.delete_group'
            )
        return context


class UpdateGroups(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/group_permissions.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group_perm-list')
    permission_required = 'auth.change_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context


class CreateGroup(LoginRequiredMixin, PermissionRequiredMixin,
                  SuccessMessageMixin, CreateView,
                  ):
    model = get_user_model()
    form_class = GroupForm
    context_object_name = 'group'
    template_name = 'users/group_permissions.html'
    success_url = reverse_lazy('group_perm-list')
    success_message = 'Group: "%(name)s" was created successfully'
    permission_required = 'auth.add_group'
