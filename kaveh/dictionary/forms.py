from django import forms
from .models import WordModel


# class WordForm(forms.Form):
#     title = forms.CharField(max_length=255, label="word")
#     mean = forms.CharField()
#     type = forms.CharField(max_length=64, required=True)
#     origin = forms.CharField(max_length=64, required=False)
#     example = forms.CharField()

class WordForm(forms.ModelForm):
    class Meta:
        model = WordModel
        fields = ("title", "mean", "type", "origin", "example")
#
# class TypeWordModel(MyAbstractModel):
#     name = models.CharField(max_length=64, unique=True)
#
#
# class WordModel(WordAbstractModel):
#     origin = models.ForeignKey("WordModel", on_delete=models.CASCADE, related_name="branches")
#     type = models.ManyToManyField("TypeWordModel", related_name="words", )
#
#
# class ExtraMeanModel(WordAbstractModel):
#     title = models.ForeignKey("WordModel", on_delete=models.CASCADE, related_name="extra_means")
