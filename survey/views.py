from django.shortcuts import render, redirect
from .forms import SurveyForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SurveySubmitSerializer
from django.conf import settings

def landing(request):

    mac = request.GET.get('usermac', '')
    ip = request.GET.get('userip', '')
    ap_ip = request.GET.get('apip', '')

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)

            #jika pake ruije
            #survey.mac_address = request.POST.get('mac')
            #survey.ip_address = request.POST.get('ip')
            # survey.ap_ip = request.POST.get('ap_ip')

            survey.mac_address = "TEST-MAC"
            survey.ip_address = "127.0.0.1"
            survey.ap_ip = "TEST-AP"

            survey.save()

            return redirect("/")

            # return redirect(f"http://{survey.ap_ip}/portal/login?usermac={survey.mac_address}")
    else:
        form = SurveyForm()

    return render(request, 'survey/landing.html', {
        'form': form,
        # 'mac': mac,
        # 'ip': ip,
        # 'ap_ip': ap_ip
    })

class SurveySubmitAPIView(APIView):

    def post(self, request):

        if request.headers.get("X-API-KEY") != settings.API_SECRET_KEY:
            return Response(
                {"error": "Unauthorized"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = SurveySubmitSerializer(data=request.data)

        if serializer.is_valid():
            survey = serializer.save()

            return Response({
                "status": "success",
                "message": "Survey berhasil disimpan",

            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)