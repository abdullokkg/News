from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from utils.views import group_queryset
from .managers import CategoryManager
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel,TranslatedFields
from parler.managers import TranslatableManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(TranslatableModel):
    slug = models.SlugField(verbose_name=_("slug"),unique=True,blank=True,null=True)
    translations = TranslatedFields(
        name = models.CharField(verbose_name=_("name"),max_length=200),
    )
    

    custom = CategoryManager()

    objects = TranslatableManager()

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)

            counter = 1
            original_slug = self.slug
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
            super().save(*args, **kwargs)

    
    @property
    def get_group_blogs(self):
        return group_queryset(3,self.blog_set.all())
    @property
    def get_group_blogs_2(self):
        return group_queryset(2,self.blog_set.all())
    @property
    def get_group_blogs_6(self):
        return group_queryset(6,self.blog_set.all())


    def __str__(self):
        return f"{self.safe_translation_getter('name',any_language=True)}"
    
    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")
    
class Tags(models.Model):
    name = models.CharField(verbose_name=_("name"),max_length=200)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Taglar")

class Blog(models.Model):
    class StatusEnum(models.TextChoices):
        PUBLISHED = 'published',_("Chop Etilgan")
        DRAFT = 'draft',_("Qoralama")
    author = models.ForeignKey('user.Author',verbose_name=_("author"),on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(verbose_name=_("title"),max_length=200)
    text = CKEditor5Field('Text',config_name="extends")
    image = models.ImageField(upload_to="Blog_images/")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    status = models.CharField(verbose_name=_("status"),max_length=200,choices=StatusEnum.choices,default=StatusEnum.PUBLISHED)

    like = models.ManyToManyField(User, related_name="likes")
    seen = models.ManyToManyField(User, related_name="seens")
    hash_tag = models.ManyToManyField(Tags)

    datetime = models.DateTimeField(auto_now_add=True)
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Bloglar")

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.blog} {self.text }"
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Commentlar")

