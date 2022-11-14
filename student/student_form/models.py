from django.db import models

from student_form.validators import gmail_validation



class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        validators=[gmail_validation],
    )
    age = models.IntegerField(


        blank=False,

        null=True,

        

    )

    CLASS_CHOICES =(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12")
)

    Class = models.CharField(
        max_length = 20,
        choices = CLASS_CHOICES,
        default = '1'
        )


    content = models.TextField()
