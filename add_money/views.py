from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import AddMoneyForm
from .models import add_money

# Create your views here.

def add(request):
    if request.method=='POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    form=AddMoneyForm()
    context={
        'form':form
    }
    return render[request,'add_money.html',context]

def display(request):
    records = add_money.objects.all()
    total = sum(item.how_much for item in records)
    return render(request, 'display.html', {'records': records, 'total': total})

def update(request, pk):
    obj = add_money.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddMoneyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = AddMoneyForm(instance=obj)   
    return render(request, 'add_money.html', {'form': form})
    
def delete(request, pk):
    qs = add_money.objects.filter(pk=pk)
    if not qs.exists():
        return HttpResponse("Record not found")
    qs.delete()
    return redirect('display')