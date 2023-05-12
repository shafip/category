from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.views.generic import ListView
import json
from django.http import JsonResponse
from django.contrib import messages
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.
def home(request):

        return render(request, 'home.html')


def CategoryForms(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat-table')
        else:

            content = {'form': form}
            return render(request, 'categoryform.html', content)
    else:
        form = CategoryForm()
        dict = {
            'form': form
        }
        return render(request, 'categoryform.html', dict)


@login_required(login_url='login')
def serchcategory(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Category.objects.filter(Name__icontains=q)
        # multiple_q = Q(Q(Name__icontains=q) | Q(last_name__icontains=q))
        # data = Category.objects.filter(multiple_q)
    else:
        data = Category.objects.order_by('-id')
    context = {
        'data': data
        }
    return render(request, 'categoryview.html', context)

# def search_view(request):
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         results = Course.objects.filter(Name__icontains=query)
#         data = {'results': list(results.values())}
#         return JsonResponse(data)
#     else:   data = Course.objects.order_by('-id')
#     context = {
#         'data': data
#         }
#     return render(request, 'categoryview.html', context)







@login_required
def updatecat(request, pk):
    mod = Category.objects.get(id=pk)
    form = CategoryForm(instance=mod)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=mod)
        if form.is_valid():
            form.save()
            return redirect('cat-table')
    context = {'form': form}
    return render(request, 'catupdate.html', context)



# def enableview(request, pk):
#     enable = get_object_or_404(Category, id=pk)
#     if enable.is_active == True:
#         enable.save()
#         data = QueryDict(request.body)
#         print(data)
#     else:
#         enable.is_active = True
#         enable.save()
#     return serchcategory(request)


# @csrf_exempt
# def enableview(request):
#     data = QueryDict(request.body)
#     category_id = data.get('userid')
#     enable = Category.objects.get(id=category_id)
#     if enable.is_active:
#         enable.is_active = True
#     else:
#         enable.is_active = True
#         enable.save()
#         return redirect('cat-table')
@csrf_exempt
def enableview(request):
    data = QueryDict(request.body)
    category_id = data.get('userid')
    enable = Category.objects.get(id=category_id)
    if enable.is_active:
        enable.is_active = True

    else:
        enable.is_active = True
        enable.save()
    return redirect('cat-table')

# def enableview(request):
#     print("hi")
#     enable = get_object_or_404(Category)
#     if enable.is_active == True:
#          data = QueryDict(request.body)
#          enable.id = data.get('userid')
#          print('hello')
#          enable.save()
#     else:
#          enable.is_active = True
#          enable.save()
#     return serchcategory(request)





def disableview(request, pk):
    disa = get_object_or_404(Category, id=pk)
    if disa.is_active == False:

        disa.save()
    else:
        disa.is_active = False
        disa.save()
    return serchcategory(request)


@login_required
def subforms(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subtable')
        else:
            print(form.errors)
            content = {'form': form}
            return render(request, 'subcat/subform.html', content)
    else:
        form = SubCategoryForm()
        dform = {
            'forms': form
        }
        return render(request, 'subcat/subform.html', dform)



@login_required(login_url='login')
def serchsubcategory(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = SubCategory.objects.filter(Field_Name__icontains=q)

        # multiple_q = Q(Q(Category_name__icontains=q) | Q(Field_Name__icontains=q))
        # data = SubCategory.objects.filter(multiple_q)
    else:
        data = SubCategory.objects.order_by('-id')
    context = {
        'data': data
    }
    return render(request, 'subcat/subtable.html', context)



@login_required
def updatesub(request, pk):
    mod = SubCategory.objects.get(id=pk)
    form = SubCategoryForm(instance=mod)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=mod)
        if form.is_valid():
            form.save()
            return redirect('subtable')
    context = {'form': form}
    return render(request, 'subcat/subupdate.html', context)


# def enablesub(request, pk):
#     sub = get_object_or_404(SubCategory, id=pk)
#     if sub.is_active == True:
#         sub.save()
#     else:
#         sub.is_active = True
#         sub.save()
#     # return serchsubcategory(request)
@csrf_exempt
def subenableview(request):
    data = QueryDict(request.body)
    subcategory_id = data.get('userid')
    try:
        enable = SubCategory.objects.get(id=subcategory_id)
        if enable.is_active:
            enable.is_active = True
        else:
            enable.is_active = True
        enable.save()
    except SubCategory.DoesNotExist:
        pass
    return serchsubcategory (request)


@login_required
def disablesub(request, pk):
    disa = get_object_or_404(SubCategory, id=pk)
    if disa.is_active == False:

        disa.save()
    else:
        disa.is_active = False
        disa.save()
    return serchsubcategory(request)

@login_required
def delete(request, pk):
    mod = SubCategory.objects.get(id=pk)
    form = SubCategoryForm(instance=mod)
    mod.delete()
    return redirect('subtable')


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import CourseForm
from django.views.generic import ListView


class CourseView(View):
    form_class = CourseForm
    initial = {'key': 'value'}
    template_name = 'courses/courseform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cotable')
        else:
            print(form.errors)
            content = {'form': form}
            return render(request, self.template_name,content)







# @method_decorator(login_required, name='dispatch')
# class CourseTable(ListView):
#
#     model = Course
#     ordering = ['-id']
#     template_name = 'courses/coursetable.html'
#     context_object_name = 'ctable'
@method_decorator(login_required, name='dispatch')
class CourseTable(ListView):
    template_name = 'courses/coursetable.html'
    context_object_name = 'ctable'
    ordering = ['-id']

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            queryset = Course.objects.filter(Q(course_name__icontains=q))
        else:
            queryset = Course.objects.order_by('-id')
        return queryset





from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from django.http import HttpResponse
class UpdateViews(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/update.html'

from django.http import HttpResponseRedirect

# class DeleteView(View):
#
#     def get(self, request, pk):
#
#         task = get_object_or_404(Course, id=pk)
#         if task.is_active == True:
#             task.save()
#         else:
#             task.is_active = True
#             task.save()
#
#             return redirect('cotable')
####################
@csrf_exempt
def co_disable(request):
    data = QueryDict(request.body)
    course_id = data.get('userid')
    try:
        enable = Course.objects.get(id=course_id)
        if enable.is_active:
            enable.is_active = True
        else:
            enable.is_active = True
        enable.save()
    except Course.DoesNotExist:
        pass
    return redirect('cotable')

class EnableView(View):

    def get(self, request, pk):

        task = get_object_or_404(Course, id=pk)
        if task.is_active == False:
            task.save()
        else:
            task.is_active = False
            task.save()

            return redirect('cotable')









from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='profile')
def profile(request):
    return render(request, 'home.html')

class TopicView(View):
    form_class = TopicForm
    initial = {'key': 'value'}
    template_name = 'topic/topicform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return redirect('topictable')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class TopicTable(ListView):
    model = Subject
    template_name = 'topic/topictable.html'
    context_object_name = 'topictable'
    ordering = ['-id']

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            queryset = Subject.objects.filter(Q(subjects__icontains=q))
        else:
            queryset = Subject.objects.order_by('-id')
        return queryset
#
#
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


class UpdateTopicView(UpdateView):
    model = Subject
    form_class = TopicForm
    template_name = 'topic/update.html'

class DeleteViewTopic(View):

    def get(self, request, pk):
        topictask = get_object_or_404(Subject, id=pk)
        if topictask.is_active == True:
            topictask.save()
        else:
            topictask.is_active = True
            topictask.save()
            return redirect('topictable')


# @csrf_exempt
# def to_disable(request):
#     print("hi")
#     data = QueryDict(request.body)
#     topic_id = data.get('userid')
#     enable = Subject.objects.get(id=topic_id)
#     if enable.is_active:
#         enable.is_active = True
#     else:
#         enable.is_active = True
#         enable.save()
#         return redirect('topictable')



class EnableViewTopic(View):

    def get(self, request, pk):

        topictask = get_object_or_404(Subject, id=pk)
        if topictask.is_active == False:
            topictask.is_active = False
            topictask.save()
        else:
            topictask.is_active = False
            topictask.save()

            return redirect('topictable')

        return HttpResponse("Topic enabled")






# def my_view(request):
#     form = CagorySelect()
#     products = Category.objects.all()
#     if request.method == 'POST':
#         category_id = request.POST['category']
#         category = Category.objects.get(id=category_id)
#         products = products.filter(category=category)
#     return render(request, 'categoryview.html', {'form': form, 'products': products})
#

from .filters import CategoryFilter

def show_category(request):
    context = {}

    filter_category = CategoryFilter(
        request.GET,
        queryset=Category.objects.all()

    )

    context['categorydata'] = filter_category

    return render(request,'sample.html',context=context)


@login_required(login_url='login')
def coursepageview(request):
    data = Course.objects.order_by('-id')
    page = Paginator(data,5 )
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request,'courses/coursetable.html',context)
