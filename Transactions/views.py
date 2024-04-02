from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm
from django.contrib import messages

# def transactions(request):
#     title = 'Welcome: This is the Home Page'
#     context = {
# 	"title": title,
# 	}
#     return render(request, "transactionsDashboard.html",context)


def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect("/transactions/transactions")
    context = {
	"form": form,
	"title": "New Invoice",
 	"total_invoices": total_invoices,
	"queryset": queryset,
	}
    return render(request, "invoiceEntry.html", context)
    
    
    
def transactions(request):
    title = 'Transactions'
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    
    if request.method == 'POST':
        queryset = Invoice.objects.filter(name__icontains=form['name'].value())
    
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    
    return render(request, "transactionsDashboard.html", context)

def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/transactions/transactions')
    context = {
        "form":form
            }
    return render(request, 'invoiceEntry.html', context)


def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/transactions/transactions')
    return render(request, 'delete_invoice.html')
