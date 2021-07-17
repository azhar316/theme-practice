from django.views.generic import TemplateView


class LoginView(TemplateView):

    template_name = 'theme/company-login.html'


class SignupView(TemplateView):

    template_name = 'theme/company-signup.html'


class DetailView(TemplateView):

    template_name = 'theme/company-detail.html'


class PeopleView(TemplateView):

    template_name = 'theme/company-people.html'


class TaskView(TemplateView):

    template_name = 'theme/company-task.html'


class TaskDetailView(TemplateView):

    template_name = 'theme/company-task-detail.html'


class SettingsView(TemplateView):

    template_name = 'theme/company-settings.html'
