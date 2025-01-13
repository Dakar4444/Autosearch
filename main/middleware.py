from django.shortcuts import redirect

class CaptchaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('captcha_verified', False) and request.path not in ['/captcha/']:
            return redirect('captcha_page')  # Перенаправляем на страницу капчи
        return self.get_response(request)
