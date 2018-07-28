from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField()
    your_age = forms.DateField()



class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True) #empty in the database
    title           = models.CharField(
                            max_length=240,
                            verbose_name='Post title',
                            unique=True,
                            error_messages={
                                "unique": "This title is not unique, please try again.",
                                "blank": "This field is not full, please try again."
                            },
                            help_text='Must be a unique title.')
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
