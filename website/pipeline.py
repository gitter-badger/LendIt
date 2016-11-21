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

        small_url = u'https://graph.facebook.com/{0}/' \
                    u'?fields=picture.width(25).height(25)' \
                    u'&access_token={1}'.format(
            fbuid,
            access_token,
        )

        request = urllib2.Request(url)
        email = json.loads(urllib2.urlopen(request).read()).get('email')

        request = urllib2.Request(small_url)
        small_pic_url = json.loads(urllib2.urlopen(request).read()).get('picture').get('data').get('url')
        social_auth_user, created = LenditUser.objects.update_or_create(
        	user=user,
        	defaults={
                'profile_pic_url': pic_url,
                'small_pic_url': small_pic_url,
                'email': email
            },
    	)
