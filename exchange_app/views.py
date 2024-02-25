from django.shortcuts import render
import requests
def exchange(request):

    response = requests.get(url='https://v6.exchangerate-api.com/v6/fc8f46bfb18bbcc4c1728af9/latest/USD').json()
    currencies = response.get("conversion_rates")

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        return render(request, 'exchange_app/index.html', context)

    if request.method == 'POST' and 'amount' in request.POST:

        amount = (request.POST.get('amount'))
        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if isfloat(amount):
            if request.POST['from_curr'] and request.POST['to_curr']:

                from_curr = request.POST['from_curr']
                to_curr = request.POST['to_curr']
                result = round((currencies[to_curr] / currencies[from_curr]) * float(amount), 2)
                context = {
                    "currencies": currencies,
                    'result': result,
                    'amount': amount,
                    'to_curr': to_curr,
                    'from_curr': from_curr
                }
                return render(request, 'exchange_app/index.html', context)
            else:
                result = 'Please Choose Currencies'
                context = {
                    "currencies": currencies,
                    'result': result,
                    'amount': amount,




                }
                return render(request, 'exchange_app/index.html', context)

        else:
            result = 'Please Enter a Real Number'
            context = {
                "currencies": currencies,
                'result': result
            }
            return render(request, 'exchange_app/index.html', context)







