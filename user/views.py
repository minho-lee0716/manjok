from django.views import View
from django.http import JsonResponse, HttpResponse

import json

class SignInView(View):
    def post(self, request):
        payload = json.loads(request.body)
        phone_number = payload.get('phone_number', None)
        password = payload.get('password', None)

        if phone_number is None or password is None:
            return HttpResponse(400)

        if phone_number == '01012345678' and password == 'a123':
            return HttpResponse()
        else:
            return HttpResponse(401)
