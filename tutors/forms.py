from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Fieldset, Layout, Field, HTML
from django import forms
from django.db.models import Q

from tutors.models import CategoryQuestion, Question, Answer


class CategoryCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    parent_category = forms.ModelChoiceField(
        queryset=CategoryQuestion.objects.all(),
        required=False)

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)

        if self.instance.id:
            queryset = CategoryQuestion.objects.filter(
                ~Q(pk__in=(
                    self.instance.id, *self.instance.childrens_pk_list)))
        else:
            queryset = CategoryQuestion.objects.all()
        self.fields['parent_category'].queryset = queryset
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('save', 'Save', css_class='btn-dark '
                                                               'mt-5'))
        self.helper.add_input(Button('cancel', 'Cancel',
                                     css_class='btn-light mt-5',
                                     onclick="javascript:location.href = "
                                             "'/category_question';"))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset('Create category ',
                     css_class='border-top border-bottom mt-5'),
            Fieldset('',
                     Field('parent_category', css_class='ml-5'),
                     Field('name', css_class='ml-5'),
                     css_class='border-bottom mt-5')
        )

    class Meta:
        model = CategoryQuestion
        fields = '__all__'


class QuestionCreateForm(forms.ModelForm):
    question_text = forms.CharField(max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super(QuestionCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-question'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                'Create/Update question', css_class='display-4'),
            Fieldset('', Field('question_text'),
                     css_class='border-top border-bottom'),
            Fieldset('',
                     Submit('save', 'Save', css_class='btn-success mt-3'),
                     HTML("""<a class='btn btn-outline-success mt-3' 
                     href="{%url 'tutors:questions_list' category_id=c.id%}">
                     Cancel</a>"""),
                     )
        )

    class Meta:
        model = Question
        fields = ['question_text', ]


class AnswerCreateForm(forms.ModelForm):
    answer_text = forms.CharField(max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super(AnswerCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-answer'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                'Create/Update answer', css_class='display-4'),
            Fieldset('',
                     Field('answer_text'),
                     css_class='border-top border-bottom'),
            Fieldset('',
                     Submit('save', 'Save', css_class='btn-success mt-3'),
                     HTML("""<a class='btn btn-outline-success mt-3' 
                     href="{%url 'tutors:answers_list' question_id=q.id%}">
                     Cancel</a>"""))
        )

    class Meta:
        model = Answer
        fields = ['answer_text', ]
