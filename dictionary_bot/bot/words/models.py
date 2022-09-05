from django.db import models

class Word(models.Model):
    title = models.CharField(
        verbose_name = 'Word',
        max_length = 100,
    )
    definition = models.TextField(
        verbose_name = 'Meaning',
    )

    def __str__(self):
        return f'{self.title}: {self.definition}'
    
    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
