from django.contrib import admin
from .models import Post


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return (),

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = ((k, v)for k, v in changelist.get_filters_params().items()if k != self.parameter_name)
        yield all_choice


class titlevvv(InputFilter):
    title = 'Input Data'
    parameter_name = 'input_data'

    def queryset(self, request, queryset):
        if self.value() is not None:
            input_data_keywords = self.value()
            return queryset.filter(
                title__contains=input_data_keywords
            )


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = [titlevvv]
    search_fields = ['title']
    list_display_links = ['id']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        print(search_term)
        # print("use", queryset[0])
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(id=search_term_as_int)
        return queryset, use_distinct


admin.site.register(Post, PostModelAdmin)
