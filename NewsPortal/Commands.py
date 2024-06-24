


# 1)   Создать двух пользователей (с помощью метода User.objects.create_user('username')).

# from news.models import *
#
# u1 = User.objects.create_user('Василий')
# u2 = User.objects.create_user('Иван')

# 2)   Создать два объекта модели Author, связанные с пользователями.
#
# a1 = Author.objects.create(user=u1)
# a2 = a1 = Author.objects.create(user=u2)


# 3)   Добавить 4 категории в модель Category.
#
# cat1=Category.objects.create(name='Спорт')
# cat2=Category.objects.create(name='Политика')
# cat3=Category.objects.create(name='Погода')
# cat4=Category.objects.create(name='Здоровье')


# 4)   Добавить 2 статьи и 1 новость.

# Post.objects.create(author_id=1, pole_ar_ne='AR',zagolovok='Билан восхитил фанатов съемкой для журнала: Ты выглядишь на 20 лет')
# Post.objects.create(author_id=1,pole_ar_ne='AR',zagolovok='Мария Кожевникова раскрыла имя четвертого сына')
# Post.objects.create(author_id=2,pole_ar_ne='NE',zagolovok='Маслянистый слой на лобовом стекле: что делать и как избавиться')


# 5)   Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)

# PostCategory.objects.create(category_id=4,post_id=2)
# PostCategory.objects.create(category_id=4,post_id=1)
# PostCategory.objects.create(category_id=3,post_id=3)

# 6)   Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

# Comment.objects.create(text_comment='Вот это новость',comment_id=1,post_comment_id=2)
# Comment.objects.create(text_comment='Познавательно',comment_id=2,post_comment_id=3)
# Comment.objects.create(text_comment='Во дает',comment_id=2,post_comment_id=1)



# 7)   Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

#  post=Post.objects.all()
# >>> post[1].like()
# >>> post[0].like()
# >>> post[2].like()
# >>> post[2].like()
# >>> post[0].like()
# >>> post[1].like()
# >>> post[0].like()
# >>> post[2].like()
# >>> post[1].like()
# >>> post[0].like()
# >>> post[0].dislike()
# >>> post[0].dislike()

# >>> comment=Comment.objects.all()
# >>> comment[0].like()
# >>> comment[1].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[2].like()
# >>> comment[1].like()
# >>> comment[1].like()
# >>> comment[0].like()
# >>> comment[2].dislike()
# >>> comment[2].dislike()
# >>> comment[2].dislike()



# 8)   Обновить рейтинги пользователей.


# authors=Author.objects.all()
# >>> authors[0].uptade_rating()
# >>> authors[1].uptade_rating()


# 9)   Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

# Author.objects.all().order_by('-rating').values('user_id__username','rating')[0]


# 10)   Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

# b=Post.objects.all().order_by('-rating').values('add_time','author_id__user_id__username','rating','text')[0]
# >>> b['preview']=Post.objects.all().order_by('-rating').first().preview()


# 11)   Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

# post=Post.objects.all().order_by('-rating')[0]
# Comment.objects.filter(post_comment_id=post).values('time_comment','comment_id__username','rating_comment')


