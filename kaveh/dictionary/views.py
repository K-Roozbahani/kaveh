from django.shortcuts import render, get_object_or_404
from django import views
from .forms import WordForm
from .models import WordModel


class WordRetrieveView(views.View):
    def post(self, request, pk=None):
        """if pk=none add new word by Form Dictionary
        get pk!=none update word"""

        if pk is None:
            form = WordForm(data=request.POST)
            if form.is_valid():
                form.save()
                context = {"word", form.instance}
                return render(request, "word_retrieve.html", context)
            else:
                return self.get(request=request, form=form)

    def get(self, request, pk=None, form=None):
        """if pk return word
            if pk is none return form word
             if form return error in form"""

        if pk is not None:
            word = get_object_or_404(WordModel, pk=pk)
            context = {"word": word}
            return render(request, "word_retrieve.html", context)

        elif pk is None:
            form = WordForm()
            context = {"form": form}
            return render(request, "add_word.html", context)

        elif form:
            context = {"form": form}
            return render(request, "add_word.html", context)
