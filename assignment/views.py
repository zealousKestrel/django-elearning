from forum.models import Comment, Lesson
import json
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.http.response import JsonResponse
from .models import Assignment, Answer 
from .forms import AssignmentForm, AnsewrForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

# def assignmentCreateView(request):
#     form = AssignmentForm()
#     if request.method == "POST":
#         form = AssignmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/upload-tugas/')
#     context = {'form_assignment':form}
#     return render(request,'assignment/assignment_create.html',context)

class assignmentCreateView(CreateView):
    model = Assignment
    # form_class = AssignmentForm
    fields = ['title','lesson','content','status']
    success_url = reverse_lazy('assignment-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['content','file']
    success_url = reverse_lazy('assignment-list')

    def get_context_data(self, **kwargs):
        assignment = Assignment.objects.get(lesson__name=self.kwargs.get('lesson'),id=self.kwargs.get('pk'))
        answers = Answer.objects.filter(assignment=assignment,user=self.request.user)
        self.kwargs.update({
            'assignment':assignment,
            'answers':answers,
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.assignment = Assignment.objects.get(lesson__name=self.kwargs.get('lesson'),id=self.kwargs.get('pk'))
        return super().form_valid(form)

class assignmentListView(ListView):
    model = Assignment


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        print('='*20)
        print(request.POST.get('text'))
        images = AssignmentForm(request.POST, request.FILES)
        print(images)
    return render(request,'assignment/index.html',{})

@csrf_exempt
def upload(request):
    if request.method == "POST":
        print('='*50)
        print(request.POST)
        print('='*50)
        pass
    return JsonResponse({'a':'ok'})
