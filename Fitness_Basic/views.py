from django.shortcuts import render
from .models import Post
from Calorie_Chart.models import Veg , Fruits, Carb, Protein, Fat, Others

# Create your views here.
def home(request):
	all_post = Post.objects.all()
	context = {'all_post_list':all_post}
	return render(request, 'index.html', context)

def single_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	print(post)
	return render(request, 'post_detail.html', {'post':post})

def bmr(request):
	return render(request, 'bmr.html')

def bmi(request):
	return render(request, 'bmi.html')

def tdee(request):
	return render(request, 'tdee.html')

def calorie_chart(request):
	all_veg = Veg.objects.all()
	all_fruits = Fruits.objects.all()
	all_carb = Carb.objects.all()
	all_protein = Protein.objects.all()
	all_fat = Fat.objects.all()
	all_others = Others.objects.all()

	context = {
					'all_veg_list':all_veg, 
					'all_fruit_list':all_fruits,
					'all_carb_list':all_carb,
					'all_protein_list':all_protein,
					'all_fat_list':all_fat,
					'all_others_list':all_others
					}
	return render(request, 'calorie.html', context)

def diet_chart(request):
	return render(request, 'diet_chart.html')
