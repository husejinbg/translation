from django.conf import settings

def ioi_settings(request):
    return {'settings': {
        'SITE_TITLE': 'EGOI 2022 Task Translation System',
        'CONTEST_TITLE': 'EGOI 2022',
        'CONTEST_FULL_TITLE': 'European Girls’ Olympiad in Informatics 2022',
        'CONTEST_DATE': 'October 16\u201323th, 2022',
        'CONTEST_PLACE': 'Antalya, Turkey',
        'TIME_ZONE': settings.TIME_ZONE,
        'IMAGES_URL': '/media/images/',
    }}
