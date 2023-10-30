from django.contrib import admin

from core.models import About, Projects, Services, Skills, Education, Experience, Testimonials, Contact


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'age', 'email', 'freelance')
    search_fields = ('name', 'profession', 'age', 'email', 'freelance')


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'github_url_project')
    search_fields = ('category', 'github_url_project')


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service',)
    search_fields = ('service',)


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    search_fields = ('skill_name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'year_start', 'year_end')
    search_fields = ('school', 'degree', 'year_start', 'year_end')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'date_start', 'date_end')
    search_fields = ('company', 'position', 'date_start', 'date_end')


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')


@admin.register(Contact)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    search_fields = ('email', 'phone')
