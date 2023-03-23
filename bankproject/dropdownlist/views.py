from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

import dropdownlist
from .forms import firstnameCreationForm
from .models import firstname, Branch


def firstname_create_view(request):
    form = firstnameCreationForm()
    if request.method == 'POST':
        form = firstnameCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstname_add')
    return render(request, 'firstname/forms.html', {'form': form})


def firstname_update_view(request, pk):
    firstname = get_object_or_404(dropdownlist, pk=pk)
    form = firstnameCreationForm(instance=firstname)
    if request.method == 'POST':
        form = firstnameCreationForm(request.POST, instance=firstname)
        if form.is_valid():
            form.save()
            return redirect('firstname_change', pk=pk)
    return render(request, 'firstname/home.html', {'form': form})


# AJAX
def load_branch(request):
    district_id = request.GET.get('district_id')
    branch = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'firstname/branch_dropdown_list_options.html', {'branch': branch})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)



