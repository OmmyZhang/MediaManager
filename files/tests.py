from django.test import TestCase
# Create your tests here.
def test_file():
    if request.method == "POST":
        File = request.FILES.get("Upload_file",None)
        
