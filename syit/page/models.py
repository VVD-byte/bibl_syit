from django.db import models
import datetime
import textract
import os

month = {
    'янв': 'Jan',
    'фев': 'Feb',
    'мар': 'Mar',
    'апр': 'Apr',
    'май': 'May',
    'июн': 'Jun',
    'июл': 'Jul',
    'авг': 'Aug',
    'сен': 'Sep',
    'окт': 'Oct',
    'ноя': 'Nov',
    'дек': 'Dec',
}

dic = {'ь':'', 'ъ':'', 'а':'a', 'б':'b', 'в':'v',
       'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'zh',
       'з':'z', 'и':'i','й':'i', 'к':'k', 'л':'l',
       'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r',
       'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'kh',
       'ц':'tc', 'ч':'ch', 'ш':'sh', 'щ':'shch',
       'ы':'y', 'э':'e', 'ю':'iu', 'я':'ia', ' ':'_'}

class life(models.Model):
    file_name = models.CharField(null = False, max_length = 150)
    date = models.DateTimeField(auto_now = False, auto_created = False)
    str_date = models.CharField(max_length = 30)
    tag = models.CharField(max_length = 20)
    heading = models.CharField(max_length = 100)
    page_text = models.TextField()
    text = models.TextField()
    slug = models.CharField(max_length = 100)

    def save(self, *args, **kwargs):
        from .views import life_left, life_left_years
        if self.file_name:
            if os.path.exists(self.file_name):
                self.tag = self.tag.upper()
                try:
                    life_left[self.tag] += 1
                    for item, i in life_left_years.items:
                        if self.date.year in item:
                            life_left_years[i][self.date.year] += 1
                            break
                except:
                    pass ########################добавить обработку добавления новых значений life_left_no_years
                text = textract.process(self.file_name).decode('utf-8').split('\n\n')
                self.heading = text[0]
                time = ' '.join([text[1].split()[0], month.get(text[1].split()[1][:3].lower(), 'May'), text[1].split()[2]])
                self.date = datetime.datetime.strptime(time, '%d %b %Y')
                self.str_date = text[1]
                slug = ''
                for i in self.heading.lower():
                    slug += dic.get(i, '_')
                self.slug = slug.upper()
                self.text = '\n\n'.join(text[2:])
                super(life, self).save(*args, **kwargs)
            else:
                assert (f"ERROR FILE DON'T EXIST {self.file_name}")

class work(models.Model):
    name_file = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now = False, auto_created = False)
    title = models.CharField(max_length = 250)
    title_low = models.CharField(max_length = 150)

class lines(models.Model):
    years = models.IntegerField()
    text = models.TextField()
    image1 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image2 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image3 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image4 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)