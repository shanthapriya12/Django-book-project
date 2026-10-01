from django.urls import path



from .views import (
    login_view,
    logout_view,
    book_list,
    add_book,
    book_detail,
    update_book,
    delete_book
)


app_name = 'books'


urlpatterns = [

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'add/',
        add_book,
        name='add_book'
    ),

    path(
        'list/',
        book_list,
        name='book_list'
    ),

    path(
        'detail/<int:book_id>/',
        book_detail,
        name='book_detail'
    ),

    path(
        'update/<int:book_id>/',
        update_book,
        name='update_book'
    ),

    path(
        'delete/<int:book_id>/',
        delete_book,
        name='delete_book'
    ),
    
]