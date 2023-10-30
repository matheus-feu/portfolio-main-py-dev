from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from linkpreview import LinkGrabber, Link, LinkPreview

from core.forms import ContactForm
from core.models import *


class IndexView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar e-mail!')
        return super(IndexView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about_data'] = About.objects.first()
        context['skills_data'] = Skills.objects.all()
        context['experience_data'] = Experience.objects.all()
        context['education_data'] = Education.objects.all()
        context['services_data'] = Services.objects.all()
        context['testimonials_data'] = Testimonials.objects.all()
        context['contact_data'] = Contact.objects.first()

        context['projects_data'] = []

        for project in Projects.objects.all():
            url = project.github_url_project
            grabber = LinkGrabber(
                initial_timeout=20,
                maxsize=1048576,
                receive_timeout=10,
                chunk_size=1024,
            )
            content, url = grabber.get_content(url)
            link = Link(url, content)
            preview = LinkPreview(link, parser='lxml')

            project.link_preview = {
                'title': preview.title,
                'description': preview.description,
                'image': preview.image,
            }
            context['projects_data'].append(project)

        return context


def get_link_preview(request):
    url = request.GET.get('url')

    grabber = LinkGrabber(
        initial_timeout=20,
        maxsize=1048576,
        receive_timeout=10,
        chunk_size=1024,
    )
    content, url = grabber.get_content(url)
    link = Link(url, content)
    preview = LinkPreview(link, parser='lxml')

    preview_info = {
        'title': preview.title,
        'description': preview.description,
        'image': preview.image,
    }

    return JsonResponse(preview_info)
