from django.shortcuts import render, redirect
from .models import Cat, Cat_Details
from .forms import CatAdoptionForm
from django.utils import timezone
from users import views

class CatWithPhoto:
    def __init__(self, cat_object, cat_image):
        self.cat_obj = cat_object
        self.cat_img = cat_image

def index(request):
    latest_cat_list = []
    cat_list = Cat.objects.filter(adopted=False).order_by('pub_date')
    for cat in cat_list:
        cat_details = Cat_Details.objects.get(details=cat.pk)
        latest_cat_list.append(CatWithPhoto(cat, cat_details.cat_photo))

    adopted_cat_list = []
    adopted_cats = Cat.objects.filter(adopted=True).order_by('-adoption_date')
    for cat in adopted_cats:
        cat_details = Cat_Details.objects.get(details=cat.pk)
        adopted_cat_list.append(CatWithPhoto(cat, cat_details.cat_photo))
        if len(adopted_cat_list) == 3:
            break

    context = {
        'latest_cat_list': latest_cat_list,
        'adopted_cat_list': adopted_cat_list,
    }
    return render(request,'adoptions/index.html', context)

def detail(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    cat_details = Cat_Details.objects.get(details=cat.pk)
    return render(request, 'adoptions/detail.html', {'cat':cat, 'cat_details':cat_details})

def contact(request):
    return render(request, 'adoptions/contact.html')

def recently_adopted(request):
    adopted_cat_list = []
    adopted_cats = Cat.objects.filter(adopted=True).order_by('-adoption_date')
    for cat in adopted_cats:
        cat_details = Cat_Details.objects.get(details=cat.pk)
        adopted_cat_list.append(CatWithPhoto(cat, cat_details.cat_photo))
    return render(request,'adoptions/recently_adopted.html', {'adopted_cat_list': adopted_cat_list})


def adopt_cat(request, cat_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    form = CatAdoptionForm()
    cat = Cat.objects.get(pk=cat_id)
    cat_details = Cat_Details.objects.get(details=cat.pk)
    if request.method == "POST":
        print(request.POST["want_the_cat"])
        print(request.POST["had_a_cat"])
        print(request.POST["keep_in_contact"])
        print(request.POST["other_mentions"])
        want_the_cat = request.POST["want_the_cat"]
        if str(want_the_cat) != "1":
            print("Do not want the cat?")
            return render(request, 'adoptions/not_adopted.html')


        cat.adopted = True
        cat.adoption_date = timezone.now()
        cat.human = request.user
        cat.save()

        return redirect('/cats')

    return render(request, 'adoptions/adopt_cat.html', {'cat':cat, 'cat_details':cat_details, 'form':form})
