from django.shortcuts import render




def WelcomeView(request):
	return render(request, 'welcome.html')
