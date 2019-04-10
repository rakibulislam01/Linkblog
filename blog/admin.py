from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    search_fields = ['id', 'title']
    list_display_links = ['title']

    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #     print(search_term)
    #     print("use", queryset[0])
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset |= self.model.objects.filter(id=search_term_as_int)
    #     return queryset, use_distinct


admin.site.register(Post, PostModelAdmin)
