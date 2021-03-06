from django.urls import path
from .views import CategoryListView, CreateCategoryView, \
    UpdateCategoryView, DeleteCategoryView, \
    QuestionListView, CreateQuestionView, DeleteQuestionView, \
    UpdateQuestionView, AnswerListView, CreateAnswerView, UpdateAnswerView, \
    DeleteAnswerView

app_name = 'tutors'

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories_list'),
    path('create_category/', CreateCategoryView.as_view(),
         name='create_category'),
    path('<int:pk>/update_category/', UpdateCategoryView.as_view(),
             name='update_category'),
    path('<int:pk>/delete_category/', DeleteCategoryView.as_view(),
         name='delete_category'),

    path('<int:category_id>/questions_list/', QuestionListView.as_view(),
         name='questions_list'),
    path('<int:category_id>/create_question/', CreateQuestionView.as_view(),
         name='create_question'),
    path('<int:category_id>/update_question/<int:pk>/',
         UpdateQuestionView.as_view(),
         name='update_question'),
    path('<int:pk>/delete_question/', DeleteQuestionView.as_view(),
         name='delete_question'),

    path('<int:question_id>/answers_list/', AnswerListView.as_view(),
         name='answers_list'),
    path('<int:question_id>/create_answer/', CreateAnswerView.as_view(),
         name='create_answer'),
    path('<int:question_id>/update_answer/<int:pk>',
         UpdateAnswerView.as_view(),
         name='update_answer'),
    path('<int:pk>/delete_answer/', DeleteAnswerView.as_view(),
         name='delete_answer'),
]
