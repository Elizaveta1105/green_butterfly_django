from pathlib import Path

import cloudinary
from cloudinary.uploader import destroy
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import PictureForm, SpendingForm
from .models import Picture, Spending
from app_sections.models import Section
from app_spendings.models import covert_uah_to_usd


#TODO: REFACTOR TOclass ReviewsListView(ListView):
    # template_name = "reviews/review_list.html"
    # model = Review
    # context_object_name = 'reviews'


def template_name(name):
    return f"app_spendings/{name}.html"


def home(request):
    return render(request, template_name=template_name('home'), context={"msg": "Hello world"})


@login_required
def spendings(request, section_id):
    section = Section.objects.get(user=request.user, id=section_id)
    spendings = Spending.objects.filter(user=request.user, section_id=section_id).all()
    total_sum = Spending.get_total_sum_uah(request.user, section_id)
    return render(request, template_name=template_name('spendings'), context={"spendings": spendings, "section": section, "total_sum": total_sum})


@login_required
def add_spending(request, section_id):
    section = Section.objects.get(user=request.user, id=section_id)

    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            spending = form.save(commit=False)
            spending.user = request.user
            spending.section = section
            spending.sum_currency = covert_uah_to_usd(spending.sum_uah)
            spending.save()

            section.sum_uah = Spending.get_total_sum_uah(request.user, section_id)
            section.sum_currency = Spending.get_total_sum_currency(request.user, section_id)
            section.save()
            return redirect(to='app_spendings:spendings', section_id=section.id)
    else:
        form = SpendingForm(instance=Spending())

    return render(request, template_name=template_name('add_spending'), context={"form": form, "section": section})


@login_required
def edit_spending(request, section_id, spending_id):
    spending = Spending.objects.get(id=spending_id, user=request.user)
    section = spending.section

    if request.method == "POST":
        spending.name = request.POST.get("name", spending.name)
        spending.comment = request.POST.get("comment", spending.comment)
        spending.payment_date = request.POST.get("payment_date", spending.payment_date)

        uah_amount = request.POST.get("sum_uah")
        if uah_amount:
            spending.sum_uah = uah_amount
            spending.sum_currency = covert_uah_to_usd(uah_amount)

        spending.save()

        if uah_amount:
            section.sum_uah = Spending.get_total_sum_uah(request.user, section_id)
            section.sum_currency = Spending.get_total_sum_currency(request.user, section_id)
            section.save()
        return redirect(to='app_spendings:spendings', section_id=section.id)

    return render(request, template_name('edit_spending'), {"spending": spending, "section": section})


@login_required
def remove_spending(request, spending_id):
    spending = Spending.objects.get(id=spending_id, user=request.user)
    section = spending.section

    spending.delete()

    section.sum_uah = Spending.get_total_sum_uah(request.user, section.id)
    section.sum_currency = Spending.get_total_sum_currency(request.user, section.id)
    section.save()

    return redirect(to='app_spendings:spendings', section_id=section.id)


@login_required
def get_images(request, spending_id):
    spending = Spending.objects.get(user=request.user, id=spending_id)
    section = spending.section
    pics = Picture.objects.filter(user=request.user, spending_id=spending_id).all()
    return render(request, template_name='app_spendings/images.html', context={"pics": pics, "spending": spending, "section": section})


@receiver(post_save, sender=Picture)
def save_public_id(sender, instance, **kwargs):
    if instance.image and not instance.public_id:
        instance.public_id = instance.image.public_id
        instance.save()


@login_required
def upload(request, spending_id):
    spending = Spending.objects.get(user=request.user, id=spending_id)

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.spending = spending
            picture.save()
            return redirect('app_spendings:spending-images', spending_id=spending.id)
    else:
        form = PictureForm(instance=Picture())
    return render(request, template_name='app_spendings/upload.html', context={"form": form, "spending": spending})


@login_required
def edit_image(request, spending_id, pic_id):
    pic = Picture.objects.get(pk=pic_id, user=request.user)
    spending = pic.spending
    if request.method == 'POST':
        pic.description = request.POST.get('description')
        pic.save()

        return redirect(to='app_spendings:spending-images', spending_id=spending.id)
    return render(request, template_name=template_name('edit_description'), context={"pic": pic, "spending": spending})


@login_required
def remove_image(request, pic_id):
    pic = Picture.objects.get(pk=pic_id, user=request.user)

    if pic.public_id:
        destroy(pic.public_id)

    pic.delete()

    return redirect(to='app_spendings:spending-images', spending_id=pic.spending.id)
