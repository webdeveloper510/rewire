from django.conf import settings
from django.utils import translation

from django.utils.deprecation import MiddlewareMixin


class ForceDefaultLanguageMiddleware(MiddlewareMixin):
    #     """
#     Ignore Accept-Language HTTP headers
    
#     This will force the I18N machinery to always choose settings.LANGUAGE_CODE
#     as the default initial language, unless another one is set via sessions or cookies
    
#     Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
#     namely django.middleware.locale.LocaleMiddleware
#     """
      def process_request(self, request):
        # print("ss",request.LANGUAGE_CODE)
        if request.META.__contains__('HTTP_ACCEPT_LANGUAGE'):
            del request.META['HTTP_ACCEPT_LANGUAGE']