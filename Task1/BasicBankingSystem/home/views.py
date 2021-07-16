from typing import ContextManager
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from home.models import *
from django.contrib import messages
# Create your views here.
def home(request):
    #return HttpResponse("Welcome")
    return render(request,'index.html')

def customers(request):
    accounts = Accounts.objects.all()
    context = {'accounts':accounts}
    return render(request,'customers.html',context)

def createAnAccount(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        dateofbirth = request.POST['dateofbirth']
        balance = request.POST['balance']
        acc_no = accountNumDetails()
        ins = Accounts(firstName=firstname, lastName=lastname, email=email, dateOfBirth=dateofbirth, balance=balance, accountNumber=acc_no)
        ins.save()
        messages.success(request,"Account created successfully!")
        return redirect('customers')
        
        
    return render(request,'createAnAccount.html')

def accountNumDetails():
    if Accounts.objects.count() == 0:
        return f'{1:04d}'
    x = Accounts.objects.last()
    y = int(x.accountNumber)+1
    return f'{y:04d}'

def transfer(request):
    if request.method == 'POST':
        fromAccNo = request.POST["fromAccNo"]
        toAccNo = request.POST["toAccNo"]
        amount = int(request.POST["amount"])
        try:
            temp = Accounts.objects.filter(accountNumber = fromAccNo)
            sent_amount = temp.first().balance
            temp = Accounts.objects.filter(accountNumber = toAccNo)
            received_amount = temp.first().balance
        except:
            messages.error(request,'Transaction Failed! Account Not Found')
        else:
            if (sent_amount-500)> amount:
                new_bal = received_amount + amount
                rem_bal = sent_amount - amount
                temp = Accounts.objects.filter(accountNumber = fromAccNo).first()
                temp.balance = rem_bal
                temp.save()
                temp = Accounts.objects.filter(accountNumber = toAccNo).first()
                temp.balance = new_bal
                temp.save()
                ins2 = Transaction(TransactionId = transId(), FromAccNo = fromAccNo, ToAccNo = toAccNo, Amount = amount)
                ins2.save()
                messages.success(request,"Succesfull! Your Transaction had been completed.")
            else:
                messages.error(request,"Insufficient Balnce in Sender's Account")
        return redirect('customers')


    return render(request,'transfer.html')

def transId():
    if Transaction.objects.count() == 0:
        return f'{1:09d}'
    x = Transaction.objects.last()
    y = int(x.TransactionId)+1
    return f'{y:09d}'

def accountDetails(request,pk):
    result = get_object_or_404(Accounts,pk=pk)
    context = {'result':result}
    return render(request,'accountDetails.html',context)

def transferHistory(request):
    transactions = Transaction.objects.all()
    context = {'transactions':transactions}
    return render(request,'transferHistory.html',context)