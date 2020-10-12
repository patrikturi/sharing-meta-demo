from django.shortcuts import render


SUPPORTED_LOCALES = ['en_US', 'hu_HU']


def index(request):
    current_locale = request.GET.get('fb_locale') or request.GET.get('locale', 'en_US')

    return render(request, 'sharing/index.html', {
        'current_locale': current_locale,
        'supported_locales': SUPPORTED_LOCALES,
    })
