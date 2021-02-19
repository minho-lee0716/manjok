from django.views import View
from django.http import JsonResponse, HttpResponse

import json

class SignInView(View):
    def post(self, request):
        try:
            payload = json.loads(request.body)
            phone_number = payload.get('phone_number', None)
            password = payload.get('password', None)

            if phone_number is None or password is None:
                return JsonResponse({'message':'필수 정보를 입력해야 합니다.'}, status=400)

            if phone_number == '01012345678' and password == 'a123':
                return JsonResponse({'message':'로그인 성공'}, status=200)
            else:
                return JsonResponse({'message':'휴대폰 번호 또는 비밀번호를 확인하세요.'}, status=401)
        except Exception:
            return JsonResponse({'message':'영훈이형 정신차려!'}, status=400)
