from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Text
import re
import json


class Crypt(object):
    _dic = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    _dic_len = len(_dic)

    @classmethod
    def __shift_msg(cls, text, shift):
        """
        Shift function
        """
        text = re.sub(r'[^a-z\s]', '', text.lower())
        res = []
        for char in text:
            if char in cls._dic:
                sym = cls._dic[(cls._dic.index(char) + shift) % cls._dic_len]
            else:
                sym = char
            res.append(sym)
        txt = "".join(res)
        txt = re.sub(r'\s+', ' ', txt)
        return txt

    @classmethod
    def encrypt_msg(cls, text, shift):
        """
        Performs character shift to the right.
        """
        return cls.__shift_msg(text, shift)

    @classmethod
    def decrypt_msg(cls, text, shift):
        """
        Performs character shift to the left.
        """
        return cls.__shift_msg(text, -shift)


@require_http_methods(['POST'])
def get_text(request):
    """
    Returns text from database by "id"
    """
    if request.is_ajax():
        js_data = json.loads(request.body.decode("utf-8"))
        try:
            t = Text.objects.get(id=js_data.get('id')).text
        except Text.DoesNotExist:
            t = 'Error text not found'
        return JsonResponse({'text': t})
    else:
        return JsonResponse({'msg': 'No ajax request'})


class IndexView(View):
    template_name = 'appCrypt/index.html'

    def get(self, request):
        data = {}
        data['text_list'] = Text.objects.all()
        return render(request, self.template_name, {'data': data})

    def post(self, request):
        if request.is_ajax():
            data = json.loads(request.body.decode("utf-8"))
            text = data.get('text')
            shift = int(data.get('shift'))
            tp = data.get('tp')

            if tp == 'encode_msg':
                out_msg = Crypt.encrypt_msg(text, shift)
            elif tp == 'decode_msg':
                out_msg = Crypt.decrypt_msg(text, shift)
            else:
                out_msg = 'No types'
            return JsonResponse({'out_msg': out_msg})
        else:
            JsonResponse({'msg': 'This is no ajax request'}, status=400)
