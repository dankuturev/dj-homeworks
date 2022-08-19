from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_counter = 0
        scopes = []
        for form in self.forms:
            if form.cleaned_data.get('tag'):
                if form.cleaned_data.get('tag').name in scopes:
                    raise ValidationError('Раздел уже существует')
                else:
                    scopes.append(form.cleaned_data.get('tag').name)
            if form.cleaned_data.get('is_main'):
                main_tag_counter += 1
        if main_tag_counter == 0:
            raise ValidationError('Не назначен основной раздел!')
        elif main_tag_counter > 1:
            raise ValidationError('Основной раздел может быть только один!')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
    inlines = [ScopeInline]

