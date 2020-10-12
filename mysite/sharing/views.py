from django.shortcuts import render


SUPPORTED_LOCALES = ['en_us', 'hu_hu']


def index(request):
    current_locale = request.GET.get('fb_locale') or request.GET.get('locale', 'en_us')

    return render(request, 'sharing/index.html', {
        'current_locale': current_locale,
        'supported_locales': SUPPORTED_LOCALES,
    })
