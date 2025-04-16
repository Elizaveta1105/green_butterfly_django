from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app_spendings.models import covert_uah_to_usd
from .forms import SectionForm
from .models import Section


@login_required
def get_sections(request):
    sections = Section.objects.filter(user=request.user).all()
    sum_curr = Section.get_total_sum_currency(request.user)

    return render(request, template_name='app_sections/sections.html', context={"sections": sections,
                                                                                "sum_curr": sum_curr})


@login_required
def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.user = request.user
            section.sum_currency = covert_uah_to_usd(section.sum_uah)
            section.save()
            return redirect(to='app_sections:sections')
    else:
        form = SectionForm()

    return render(request, template_name='app_sections/create.html', context={"form": form})


@login_required
def edit_section(request, section_id):
    section = Section.objects.get(id=section_id, user=request.user)
    if request.method == 'POST':

        new_name = request.POST.get('name', section.name)
        new_comment = request.POST.get('comment', section.comment)
        is_completed = request.POST.get('completed') == 'on'

        Section.objects.filter(id=section_id, user=request.user).update(name=new_name, comment=new_comment, completed=is_completed)
        return redirect(to='app_sections:sections')
    return render(request, template_name='app_sections/edit.html', context={"section": section})


@login_required
def delete_section(request, section_id):
    section = Section.objects.get(id=section_id, user=request.user)
    section.delete()

    return redirect(to='app_sections:sections')

