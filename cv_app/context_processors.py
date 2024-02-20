menu = [
        {'name': 'Home', 'url_name': 'home'},
        {'name': 'About', 'url_name': 'about'},
        {'name': 'Skills', 'url_name': 'skills'},
        {'name': 'Portfolio', 'url_name': 'portfolio'},
        {'name': 'Contact', 'url_name': 'contact'},
        {'name': 'Blog', 'url_name': 'blog'},
    ]


def get_menu(request):
    return {'mainmenu': menu,}
