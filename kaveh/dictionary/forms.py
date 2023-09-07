from django import forms


class WordForm(forms.Form):
    title = forms.CharField(max_length=255, label="word")
    mean = forms.Textarea()
    type = forms.CharField(max_length=64, required=True)
    origin = forms.CharField(max_length=64, required=False)
    example = forms.Textarea()
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