from django.shortcuts import render
from django.shortcuts import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


# Напишите ваш обработчик. Используйте DATA как источник данных
def omlet(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': DATA['omlet'],
        'servings': servings
    }
    print(servings)
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': DATA['pasta'],
        'servings': servings
    }
    print(servings)
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': DATA['buter'],
        'servings': servings
    }
    print(servings)
    return render(request, 'calculator/index.html', context)


# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
