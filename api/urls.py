from api.v1.urls import urlpatterns as api_v1_urls
from api.v2.urls import urlpatterns as api_v2_urls

urlpatterns = []
urlpatterns.extend(api_v1_urls)
urlpatterns.extend(api_v2_urls)
