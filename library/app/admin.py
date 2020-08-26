from django.contrib import admin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import CustomUser
from .models import Book
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

admin.site.register(CustomUser)



# Register your models here.
# class BookAdmin(ImportExportModelAdmin):   # 'id', it will create unique id for every object.
#     list_display = ('id','book_id',	'best_book_id',	'work_id',	'books_count',	'isbn',	'isbn13',	'authors',	'original_publication_year',	'original_title',	'title',	'language_code',	'average_rating',	'ratings_count',	'work_ratings_count',	'work_text_reviews_count',	'ratings_1',	'ratings_2',	'ratings_3',	'ratings_4',	'ratings_5',	'image_url',	'small_image_url') # It will display all the columns.
#     list_display_links = ('id','title')
#     list_editable = ('authors',)  # It will give you the editing opportunity
#     list_per_page = 10  # It will show the item you give.Like, you gave 10.That means you will can see the 10 items of all the items.
#     search_fields = ('title','authors','book_id','isbn') # It will create a search filed
#     # list_filter = ('gender','date_added') # It will allow you to filtering each item.

admin.site.register(Book)  # It will register these items in admin panel
admin.site.unregister(Group)  # It will remove the Group section from Authentication and authorization in admin panel.
