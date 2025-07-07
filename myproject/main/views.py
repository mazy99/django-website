from django.shortcuts import render

def home_view(request):
    """
    Render the home page.
    """
    services = [
   {'title': 'Разработка корпоративных порталов и внутренних систем', 'icon': 'main/img/corp_portals.png'},
    {'title': 'Создание интернет-магазинов и e-commerce платформ', 'icon': 'main/img/internet.png'},
    {'title': 'Проектирование и реализация REST API', 'icon': 'main/img/api.png'},
    {'title': 'Интеграция с внешними сервисами и платёжными системами', 'icon': 'main/img/pay.png'},
    {'title': 'UX/UI-дизайн и прототипирование', 'icon': 'main/img/ux.png'},
    {'title': 'Техническая поддержка и сопровождение проектов', 'icon': 'main/img/support.png'},
    {'title': 'Миграция и оптимизация существующих решений', 'icon': 'main/img/migration.png'},
]
    return render(request, 'main/home.html', {'title': 'Главная страница', 'services': services})

def about_view(request):
    """
    Render the about page with complete team and company data.
    """
    team = [
        {
            'name': 'Алексей Петров',
            'role': 'Ведущий разработчик Django/Python',
            'bio': '10+ лет опыта в веб-разработке. Специализация: высоконагруженные системы.',
            'photo': 'main/img/team/alex.png'
        },
        {
            'name': 'Мария Смирнова',
            'role': 'UX/UI дизайнер',
            'bio': 'Создаёт интуитивно понятные интерфейсы с 2016 года.',
            'photo': 'main/img/team/maria.png'
        },
        {
            'name': 'Игорь Васильев',
            'role': 'Project Manager',
            'bio': 'Координирует команды и следит за сроками реализации проектов.',
            'photo': 'main/img/team/igor.png'
        },
        {
            'name': 'Анна Козлова',
            'role': 'Бизнес-аналитик',
            'bio': 'Превращает бизнес-требования в технические спецификации.',
            'photo': 'main/img/team/anna.png'
        },
    ]
    
    context = {
        'about': 'О нашей компании',
        'team': team,
        'stats': {
            'projects': 50,
            'years': 3,
            'clients': 100,
        }
    }
    
    return render(request, 'main/about.html', context)