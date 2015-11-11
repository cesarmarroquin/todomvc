from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import DetailUpdateTodo

urlpatterns = [
    url(r'^todos/$', 'api.views.list_create_todos'),
    url(r'^todos/(?P<pk>\d+)', DetailUpdateTodo.as_view(), name='api_todo_detail_update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
