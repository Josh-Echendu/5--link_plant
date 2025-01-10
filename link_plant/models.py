from django.db import models


BG_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
)

# Primary_key table
class Profile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    # From the Primary table to access a record from the foreign key table, we would use 'modelname_set', i.e 'Link_set' 
    # But bcos of the related_name = 'links' in the foreign key we use 'profile.links', to access a record from the foreign key table

    def __str__(self):
        return self.name

# Foreign_key table   
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()

    # The field 'profile' is known as profile_id which is referencing the primary key of the Profile table
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")
    
    def __str__(self):
        return f"{self.text} | {self.url}"
    