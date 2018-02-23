from .forms import PostCodeForm


def postcodeform(request):
    postcode = PostCodeForm(request.POST or None)
    post_code = None
    post_code = request.POST.get("postcode")
    print("Yo Yo", post_code)
    return {"post_code":post_code}