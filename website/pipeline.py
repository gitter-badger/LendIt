from website.models import LenditUser
from django.conf import settings
from django.template.loader import render_to_string
import urllib2
import json

def user_profile_picture(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        pic_url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
        fbuid = response['id']
        access_token = response['access_token']

        url = u'https://graph.facebook.com/{0}/' \
              u'?fields=email' \
              u'&access_token={1}'.format(
            fbuid,
            access_token,
        )

        request = urllib2.Request(url)
        email = json.loads(urllib2.urlopen(request).read()).get('email')
    social_auth_user, created = LenditUser.objects.update_or_create(
    	user=user,
    	defaults={'profile_pic_url': pic_url, 'email': email},
    	)
