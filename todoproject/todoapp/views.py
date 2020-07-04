from django.shortcuts import render
from django.http import HttpResponseRedirect
import sqlalchemy, sqlalchemy.orm
from .models import Base, Clients
from django.contrib import messages
import asyncio
import time
from aiohttp import ClientSession

connection_setup = "mysql://root:s1n1s1n1@localhost:3306/mysql"
engine = sqlalchemy.create_engine(connection_setup)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)



def todoappView(request):

    all_data = session.query(Clients).all()
    return render(request, 'todolist.html',
    {'all_items':all_data})

def addTodoView(request):
    name = request.POST['content_name']
    city = request.POST['content_city']
    age = request.POST['content_age']



    if not name or not city or not age:
        messages.add_message(request, messages.SUCCESS,'All fields are required')
        return HttpResponseRedirect('/')
    else:
        new_item = Clients(name=name, city=city, age=age)
        time.sleep(10)
        session.add(new_item)
        session.commit()
        messages.success(request, 'все данные успешно сохранены')

        return HttpResponseRedirect('/')

def deleteTodoView(request, i):
    obj = session.query(Clients).filter_by(id=i).one()
    session.delete(obj)
    session.commit()

    return HttpResponseRedirect('/')


