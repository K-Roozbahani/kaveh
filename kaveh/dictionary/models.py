from django.db import models


class MyAbstractModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class WordAbstractModel(MyAbstractModel):
    title = models.CharField(max_length=255, unique=True)
    mean = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class TypeWordModel(MyAbstractModel):
    name = models.CharField(max_length=64, unique=True)


class WordModel(WordAbstractModel):
    origin = models.ForeignKey("WordModel", on_delete=models.CASCADE, related_name="branches", null=True, blank=True)
    type = models.ManyToManyField("TypeWordModel", related_name="words", null=True, blank=True)
    example = models.TextField(null=True, blank=True)


class ExtraMeanModel(WordAbstractModel):
    title = models.ForeignKey("WordModel", on_delete=models.CASCADE, related_name="extra_means")
