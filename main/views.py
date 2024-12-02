from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from catalog.forms import VKParserForm
from catalog.models import Catalogs, Gallery
from catalog.web_parser import parse_vk_group_posts
from main.forms import UploadMultipleImagesForm


def index(request):

    distinct_catalogs= Catalogs.objects.filter(is_approved=True).prefetch_related('photos').all().order_by('gos_number', '-id').distinct('gos_number')
    catalogs = distinct_catalogs[:10]

    catalogs_with_photo = []
    for catalog in catalogs:
        first_photo = catalog.photos.first()
        catalogs_with_photo.append({
            'catalog': catalog,
            'first_photo': first_photo,
        })

    return render(request, 'main/index.html', {'catalogs_with_photo': catalogs_with_photo})


def search(request):

    if request.method =='GET':
        series1 = request.GET.get('series1')
        number = request.GET.get('number')
        series2 = request.GET.get('series2')

        full_number = f"{series1}{number}{series2}"

        results = Catalogs.objects.filter(gos_number=full_number, is_approved=True)

        return render(request, 'main/search_results.html', {'results': results})
    

def download(request):
    if request.method == 'POST':
        form = UploadMultipleImagesForm(request.POST, request.FILES)
        if form.is_valid():
            #print("Форма валидна")
            catalog = Catalogs(gos_number=form.cleaned_data['gos_number'], slug='фото добавлено пользователем', description='Нет', is_approved=False)
            catalog.save()
            
            #print("Содержимое request.FILES:", request.FILES)
            #print("Ключи request.FILES:", request.FILES.keys())
            for image in request.FILES.getlist('images'):
                #print("Тут изображение!")
                gallery_photo = Gallery(photo=image, catalogs=catalog)
                gallery_photo.save()

            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UploadMultipleImagesForm()

    return render(request, 'main/download.html', {'form':form})


#----------------------------Представления для страницы модерации!----------------------------------#

@user_passes_test(lambda u: u.is_superuser)
def admin_approval_list(request):
    # Отображаем только данные, которые ещё не одобрены

    catalogs = Catalogs.objects.filter(is_approved=False).prefetch_related('photos')
    return render(request, 'catalog/approval_list.html', {'catalogs': catalogs})


def delete_photo(request, catalog_id, photo_id):
    photo = get_object_or_404(Gallery, id=photo_id, catalogs=catalog_id)

    if request.method == 'POST':
        photo.delete()  # Здесь вызовется метод delete из модели Gallery, который удалит файл
        return redirect(reverse('admin_approval_list'))
    return redirect(reverse('admin_approval_list'))


def edit_gos_number(request, catalog_id):
    if request.method == 'POST':
        catalog = get_object_or_404(Catalogs, id=catalog_id)
        new_gos_number = request.POST.get('gos_number')
        
        if new_gos_number:
            catalog.gos_number = new_gos_number
            catalog.save()  # Сохраняем изменения в базе данных
            
        return redirect('admin_approval_list')  # Перенаправляем обратно на страницу модерации


def approve_catalog(request, catalog_id):
    # Администратор одобряет данные
    catalog = get_object_or_404(Catalogs, id=catalog_id)
    catalog.is_approved = True
    catalog.save()
    return redirect('admin_approval_list')


def delete_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalogs, id=catalog_id)
    catalog.delete()  # Удаляем объект из базы данных
    return redirect('admin_approval_list')  # Возвращаемся на страницу модерации

#---------------------------------------------------------------------------------------------------#


def moderation_view(request):
    if request.method == 'POST':
        form = VKParserForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            group_id = form.cleaned_data['group_id']
            
            # Запуск парсера с введёнными значениями
            parse_vk_group_posts(group_id=group_id, token=token)
            
            # Сообщение об успешном завершении
            return render(request, 'catalog/parser_page.html', {'form': form, 'message': 'Парсинг завершён успешно!'})
    else:
        form = VKParserForm()
    
    return render(request, 'catalog/parser_page.html', {'form': form})


#---------------------------------------------------------------------------------------------------#

def catalog(request):
    catalogs= Catalogs.objects.filter(is_approved=True).prefetch_related('photos').all().distinct('gos_number')

    catalogs_with_photo = []
    for catalog in catalogs:
        first_photo = catalog.photos.first()
        catalogs_with_photo.append({
            'catalog': catalog,
            'first_photo': first_photo,
        })

    return render(request, 'catalog/catalog.html', {'catalogs_with_photo': catalogs_with_photo})


def history_car(request, number):

    gos_numb = Catalogs.objects.filter(gos_number=number, is_approved=True)

    context = {
        'gos_numb': gos_numb,
    }

    return render(request, 'main/history_car.html', context=context)