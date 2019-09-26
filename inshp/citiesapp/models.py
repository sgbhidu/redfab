'''from django.db import models





class Countrie(models.Model):
    Country_ID = models.IntegerField(primary_key=True)
    CountryName = models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    continent = models.CharField(max_length=20)

    Visa = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    Events = models.CharField(max_length=20)
    Foods = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Map = models.CharField(max_length=20)
    Packages = models.CharField(max_length=20)
    Travels = models.CharField(max_length=20)
    Hotels = models.CharField(max_length=20)
    Activities = models.CharField(max_length=20)
    def __str__(self):
        return self.CountryName


class State(models.Model):
    State_ID = models.IntegerField(primary_key=True)
    State_Name= models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    country = models.OneToOneField(Countrie,on_delete=models.CASCADE,max_length=20)


    Events = models.CharField(max_length=20)
    Foods = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Map = models.CharField(max_length=20)
    Packages = models.CharField(max_length=20)
    Travels = models.CharField(max_length=20)

    Activities = models.CharField(max_length=20)
    def __str__(self):
        return self.State_Name











class Restaurant(models.Model):
    Restaurant_ID= models.IntegerField(primary_key=True)
    RestaurantName=models.CharField(max_length=20)
    URL = models.URLField()
    About = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Photos = models.ImageField(max_length=20)
    Cuisines = models.CharField(max_length=20)
    Meals = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    DietaryType = models.CharField(max_length=20)
    Features = models.CharField(max_length=20)
    Ratings = models.CharField(max_length=20)
    Reviews = models.CharField(max_length=20)
    def __str__(self):
        return self.RestaurantName

class Visa(models.Model):
    Visa_ID = models.IntegerField(primary_key=True)
    URL = models.URLField(max_length=20)
    country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE,max_length=20)
    About = models.CharField(max_length=20)
    FAQS = models.CharField(max_length=20)

    OnArival = models.CharField(max_length=20)
    def __str__(self):
        return self.Visa_ID

class Storie(models.Model):
    Article_ID = models.IntegerField(primary_key=True,auto_created=True)
    ArticleName = models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Vertical = models.CharField(max_length=20)
    #place = models.OneToOneField(Place,to_field='Places',on_delete=models.CASCADE)

    country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)
    Months = models.CharField(max_length=20)
    WrittenBy = models.CharField(max_length=20)
    Authortype = models.CharField(max_length=20)
    def __str__(self):
        return self.ArticleName



class Place(models.Model):
    Place_ID = models.IntegerField(primary_key=True)
    Places = models.CharField(max_length=20)
    URL = models.CharField(max_length=20)
    #City = models.OneToOneField(Citie,to_field='CityName',on_delete=models.CASCADE)
    State = models.OneToOneField(State,to_field='State_Name',on_delete=models.CASCADE)
    Country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)

    Description = models.CharField(max_length=20)
    Themes = models.CharField(max_length=20)
    FAQs=models.CharField(max_length=20)
    Weather=models.CharField(max_length=20)
    TimeRequired=models.CharField(max_length=20)
    Timings=models.CharField(max_length=20)
    EntryFee=models.CharField(max_length=20)
    Reviews=models.CharField(max_length=20)
    TripuppOpininon=models.CharField(max_length=20)
    Food=models.CharField(max_length=20)
    Photos=models.ImageField()
    Videos= models.FileField(upload_to='videos/', null=True, verbose_name="video")
    Map=models.CharField(max_length=20)
    HowToReach=models.CharField(max_length=200)
    Articles=models.OneToOneField(Storie,to_field='ArticleName',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.Places


class Citie(models.Model):
    City_ID=models.IntegerField(primary_key=True,unique=True)
    City_Name=models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    PlacesToVisit = models.ForeignKey(Place,on_delete=models.CASCADE)
    state = models.CharField(max_length=20)
    country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)
    Weather = models.CharField(max_length=20)
    IdealMonth = models.CharField(max_length=20)
    IdealDuration = models.CharField(max_length=20)
    NearestAirport = models.CharField(max_length=20)
    UpcomingEvents = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    MoreOnCity = models.CharField(max_length=20)
    Articles = models.ForeignKey(Storie,on_delete=models.SET_NULL,null=True)
    Reviews = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Videos = models.CharField(max_length=20)
    HowToReach = models.CharField(max_length=20)
    def __str__(self):
        return self.City_Name

class User(models.Model):
    UserID= models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    URL= models.URLField()
    Mobile=models.IntegerField(max_length=20)
    EmailId = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    city = models.OneToOneField(Citie,to_field='City_Name',on_delete=models.SET_NULL,null=True)
    state = models.OneToOneField(State,to_field='State_Name',on_delete=models.SET_NULL,null=True)
    country = models.OneToOneField(Countrie, to_field='CountryName',unique=True,on_delete=models.CASCADE)
    Language = models.CharField(max_length=20)
    Pic = models.ImageField(max_length=20)
    Facebook = models.CharField(max_length=20)
    Instagram = models.CharField(max_length=20)
    Twitter = models.CharField(max_length=20)
    Visited = models.CharField(max_length=20)
    Wishlist = models.CharField(max_length=20)
    Friends = models.CharField(max_length=20)
    Contributions = models.CharField(max_length=20)
    Reviews = models.CharField(max_length=20)
    def __str__(self):
        return self.Name



class Event(models.Model):
    Fest_ID=models.IntegerField(primary_key=True)
    FestName = models.CharField(max_length=20)
    URL = models.URLField(max_length=20)
    About = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Month = models.CharField(max_length=20)
    Partition = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    city = models.ForeignKey(Citie,on_delete=models.CASCADE)
    country = models.ForeignKey(Countrie,on_delete=models.CASCADE)
    def __str__(self):
        return self.FestName'''

from django.db import models




















class Restaurant(models.Model):
    Restaurant_ID= models.IntegerField(primary_key=True)
    RestaurantName=models.CharField(max_length=20)
    URL = models.URLField()
    About = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Photos = models.ImageField(max_length=20)
    Cuisines = models.CharField(max_length=20)
    Meals = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    DietaryType = models.CharField(max_length=20)
    Features = models.CharField(max_length=20)
    Ratings = models.CharField(max_length=20)
    Reviews = models.CharField(max_length=20)
    def __str__(self):
        return self.RestaurantName



class Storie(models.Model):
    Article_ID = models.IntegerField(primary_key=True,auto_created=True)
    ArticleName = models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Vertical = models.CharField(max_length=20)
    #place = models.OneToOneField(Place,to_field='Places',on_delete=models.CASCADE)

    #country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)
    Months = models.CharField(max_length=20)
    WrittenBy = models.CharField(max_length=20)
    Authortype = models.CharField(max_length=20)
    def __str__(self):
        return self.ArticleName









class Countrie(models.Model):
    Country_ID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    continent = models.CharField(max_length=20)

    Visa = models.CharField(max_length=20)


    Events = models.CharField(max_length=20)
    Foods = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Map = models.CharField(max_length=20)
    Packages = models.CharField(max_length=20)
    Travels = models.CharField(max_length=20)
    Hotels = models.CharField(max_length=20)
    Activities = models.CharField(max_length=20)
    def __str__(self):
        return self.CountryName

class Visa(models.Model):
    Visa_ID = models.IntegerField(primary_key=True)
    URL = models.URLField(max_length=20)
    country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE,max_length=20)
    About = models.CharField(max_length=20)
    FAQS = models.CharField(max_length=20)

    OnArival = models.CharField(max_length=20)
    def __str__(self):
        return self.Visa_ID

    
class Place(models.Model):
    Place_ID = models.AutoField(primary_key=True)
    Places = models.CharField(max_length=20)
    URL = models.CharField(max_length=20)
    #City = models.OneToOneField(Citie,to_field='CityName',on_delete=models.CASCADE)
    #state = models.OneToOneField(State,on_delete=models.CASCADE)
    Country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)

    Description = models.CharField(max_length=20)
    Themes = models.CharField(max_length=20)
    FAQs=models.CharField(max_length=20)
    Weather=models.CharField(max_length=20)
    TimeRequired=models.CharField(max_length=20)
    Timings=models.CharField(max_length=20)
    EntryFee=models.CharField(max_length=20)
    Reviews=models.CharField(max_length=20)
    TripuppOpininon=models.CharField(max_length=20)
    Food=models.CharField(max_length=20)
    Photos=models.ImageField()
    Videos= models.FileField(upload_to='videos/', null=True, verbose_name="video")
    Map=models.CharField(max_length=20)
    HowToReach=models.CharField(max_length=200)
    Articles=models.OneToOneField(Storie,to_field='ArticleName',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.Places


class State(models.Model):
    State_ID = models.AutoField(primary_key=True)
    State_Name= models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    country = models.OneToOneField(Countrie,on_delete=models.CASCADE,max_length=20)
    places=models.ForeignKey(Place,on_delete=models.CASCADE)

    Events = models.CharField(max_length=20)
    Foods = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Map = models.CharField(max_length=20)
    Packages = models.CharField(max_length=20)
    Travels = models.CharField(max_length=20)

    Activities = models.CharField(max_length=20)
    def __str__(self):
        return self.State_Name




class Citie(models.Model):
    City_ID=models.IntegerField(primary_key=True,unique=True)
    City_Name=models.CharField(max_length=20,unique=True)
    URL = models.CharField(max_length=20)
    PlacesToVisit = models.ForeignKey(Place,on_delete=models.CASCADE)
    state = models.OneToOneField(State,to_field='State_Name',max_length=20)
    country = models.OneToOneField(Countrie,to_field='CountryName',on_delete=models.CASCADE)
    Weather = models.CharField(max_length=20)
    IdealMonth = models.CharField(max_length=20)
    IdealDuration = models.CharField(max_length=20)
    NearestAirport = models.CharField(max_length=20)
    UpcomingEvents = models.CharField(max_length=20)
    About = models.CharField(max_length=20)
    MoreOnCity = models.CharField(max_length=20)
    Articles = models.ForeignKey(Storie,on_delete=models.SET_NULL,null=True)
    Reviews = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Videos = models.CharField(max_length=20)
    HowToReach = models.CharField(max_length=20)
    def __str__(self):
        return self.City_Name


class User(models.Model):
    UserID= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    URL= models.URLField()
    Mobile=models.IntegerField(max_length=20)
    EmailId = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    city = models.OneToOneField(Citie,to_field='City_Name',on_delete=models.SET_NULL,null=True)
    state = models.OneToOneField(State,to_field='State_Name',on_delete=models.SET_NULL,null=True)
    country = models.OneToOneField(Countrie, to_field='CountryName',unique=True,on_delete=models.CASCADE)
    Language = models.CharField(max_length=20)
    Pic = models.ImageField(max_length=20)
    Facebook = models.CharField(max_length=20)
    Instagram = models.CharField(max_length=20)
    Twitter = models.CharField(max_length=20)
    Visited = models.CharField(max_length=20)
    Wishlist = models.CharField(max_length=20)
    Friends = models.CharField(max_length=20)
    Contributions = models.CharField(max_length=20)
    Reviews = models.CharField(max_length=20)
    def __str__(self):
        return self.Name



class Event(models.Model):
    Fest_ID=models.IntegerField(primary_key=True)
    FestName = models.CharField(max_length=20)
    URL = models.URLField(max_length=20)
    About = models.CharField(max_length=20)
    Photos = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Month = models.CharField(max_length=20)
    Partition = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    city = models.ForeignKey(Citie,on_delete=models.CASCADE)
    country = models.ForeignKey(Countrie,on_delete=models.CASCADE)
    def __str__(self):
        return self.FestName









