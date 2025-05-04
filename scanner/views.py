from django.shortcuts import render
from .forms import ScanForm
from .utils import detect_xss_sql

def scan_view(request):
    result = []
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = detect_xss_sql(user_input)
    else:
        form = ScanForm()
    return render(request, 'scanner/scan.html', {'form': form, 'result': result})
