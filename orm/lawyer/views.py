from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *
import datetime


def check_form(request_form):
    fio = request_form['name'].split(' ')
    if len(fio) == 3:
        l_name = fio[0]
        f_name = fio[1]
        m_name = fio[2]
    elif len(fio) == 2:
        l_name = fio[0]
        f_name = fio[1]
        m_name = ''
    elif len(fio) == 1:
        l_name = ''
        f_name = fio[0]
        m_name = ''
    else:
        l_name = ''
        f_name = ''
        m_name = ''
    passport = request_form['passport']
    tel = request_form['phone']
    client_id = add_client(f_name, m_name, l_name, passport, tel)

    content = request_form['content']
    if len(request_form['option-cases']) > 0:
        case = CasesType.objects.get(pk=request_form['option-cases'])
    else:
        case = ''
    service = Services.objects.get(pk=request_form['option-service'])
    lawyers = Lawyers.objects.filter(id_scope=request_form['option-scope'])

    case_id = add_case(service, content, client_id, lawyers[0], service, case)

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    date = tomorrow.strftime('%Y-%m-%d') + ' 12:00'

    reg_id = registration(id_client=client_id,  id_lawyer=lawyers[0], id_service=service,
                          id_case_type=case, date=date)
    return reg_id, f'{client_id.l_name} {client_id.f_name} {client_id.m_name}', date


def add_client(f_name, m_name, l_name, passport, tel):
    client = Clients(f_name=f_name, m_name=m_name, l_name=l_name, passport=passport, tel=tel)
    client.save()
    return client


def add_case(name, content, id_client, id_lawyer, id_service, id_case_type):
    case = Cases(name=name, content=content, id_client=id_client, id_lawyer=id_lawyer, id_service=id_service,
                 id_case_type=id_case_type)
    case.save()
    return case.id


def registration(id_client,  id_lawyer, id_service, id_case_type, date):
    reg = Registration(id_client=id_client, id_lawyer=id_lawyer, id_service=id_service,
                       id_case_type=id_case_type, date=date)
    reg.save()
    return reg.id


def index(request):
    menu = [{'title': 'Записаться', 'url': 'client', 'active': False},
            {'title': 'Найти запись', 'url': 'search', 'active': False}]
    return render(request, 'lawyer/index.html', context={'menu': menu})


def client(request):
    menu = [{'title': 'Записаться', 'url': 'client', 'active': True},
            {'title': 'Найти запись', 'url': 'search', 'active': False}]

    if request.method == 'POST':
        request_form = request.POST
        reg_id, name, date = check_form(request_form)
        return thanks(request, reg_id, name, date)
    else:
        cases_type = CasesType.objects.all()
        scope = Scope.objects.all()
        services = Services.objects.all()
        context = {
            'menu': menu,
            'cases': cases_type,
            'scope': scope,
            'services': services,
        }
        return render(request, 'lawyer/client.html', context=context)


def thanks(request, reg_id, name, date):
    menu = [{'title': 'Записаться', 'url': 'client', 'active': False},
            {'title': 'Найти запись', 'url': 'search', 'active': False}]
    context = {
        'menu': menu,
        'reg': reg_id,
        'name': name,
        'date': date
    }
    return render(request, 'lawyer/thanks.html', context=context)


def search(request):
    menu = [{'title': 'Записаться', 'url': 'client', 'active': False},
            {'title': 'Найти запись', 'url': 'search', 'active': True}]
    case = False

    if request.method == 'POST':
        search_form = request.POST
        name = search_form['name'].lower()
        try:
            reg = Registration.objects.get(pk=int(search_form['num']))
            if name in reg.id_client.f_name.lower() or name in reg.id_client.l_name.lower() or \
                    name in reg.id_client.m_name.lower():
                case = [reg.id, reg.id_client.f_name + ' ' + reg.id_client.l_name, reg.id_service.type,
                        reg.id_case_type.type, reg.id_service.cost, reg.date]
        except:
            pass

    context = {
        'menu': menu,
        'case': case,
    }
    return render(request, 'lawyer/search.html', context=context)
