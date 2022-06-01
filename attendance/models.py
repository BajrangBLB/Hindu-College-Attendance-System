from django.db import models
from django.utils import timezone
from pandas import DataFrame

# Create your models here.
class QR(models.Model):
    code = models.CharField(max_length=100)
    no_classes = models.CharField(max_length=2, default=2)
    ctime = models.TimeField(default=timezone.now)
    cdate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.code

class Data(models.Model):
    username = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    roll_no = models.CharField(max_length=5)
    email = models.EmailField(max_length=1000)

class Room(models.Model):
    door = models.CharField(max_length=10)
    def __str__(self):
        return self.door

class Attendance(models.Model):
    class_date = models.DateField(default=timezone.now)
    code = models.CharField(max_length=1000)

    student_24 = models.CharField(max_length=1, default=0)
    student_59 = models.CharField(max_length=1, default=0)
    student_64 = models.CharField(max_length=1, default=0)
    student_144 = models.CharField(max_length=1, default=0)
    student_175 = models.CharField(max_length=1, default=0)
    student_182 = models.CharField(max_length=1, default=0)
    student_188 = models.CharField(max_length=1, default=0)
    student_219 = models.CharField(max_length=1, default=0)
    student_248 = models.CharField(max_length=1, default=0)
    student_277 = models.CharField(max_length=1, default=0)
    student_319 = models.CharField(max_length=1, default=0)
    student_320 = models.CharField(max_length=1, default=0)
    student_324 = models.CharField(max_length=1, default=0)
    student_325 = models.CharField(max_length=1, default=0)
    student_333 = models.CharField(max_length=1, default=0)
    student_346 = models.CharField(max_length=1, default=0)
    student_348 = models.CharField(max_length=1, default=0)
    student_362 = models.CharField(max_length=1, default=0)
    student_363 = models.CharField(max_length=1, default=0)
    student_367 = models.CharField(max_length=1, default=0)
    student_370 = models.CharField(max_length=1, default=0)
    student_376 = models.CharField(max_length=1, default=0)
    student_380 = models.CharField(max_length=1, default=0)
    student_422 = models.CharField(max_length=1, default=0)
    student_427 = models.CharField(max_length=1, default=0)
    student_433 = models.CharField(max_length=1, default=0)
    student_434 = models.CharField(max_length=1, default=0)
    student_436 = models.CharField(max_length=1, default=0)
    student_447 = models.CharField(max_length=1, default=0)
    student_449 = models.CharField(max_length=1, default=0)
    student_459 = models.CharField(max_length=1, default=0)
    student_466 = models.CharField(max_length=1, default=0)
    student_469 = models.CharField(max_length=1, default=0)
    student_475 = models.CharField(max_length=1, default=0)
    student_482 = models.CharField(max_length=1, default=0)
    student_486 = models.CharField(max_length=1, default=0)
    student_517 = models.CharField(max_length=1, default=0)
    student_518 = models.CharField(max_length=1, default=0)
    student_520 = models.CharField(max_length=1, default=0)
    student_528 = models.CharField(max_length=1, default=0)
    student_531 = models.CharField(max_length=1, default=0)
    student_540 = models.CharField(max_length=1, default=0)
    student_546 = models.CharField(max_length=1, default=0)
    student_550 = models.CharField(max_length=1, default=0)
    student_588 = models.CharField(max_length=1, default=0)
    student_594 = models.CharField(max_length=1, default=0)
    student_623 = models.CharField(max_length=1, default=0)
    student_641 = models.CharField(max_length=1, default=0)
    student_655 = models.CharField(max_length=1, default=0)
    student_662 = models.CharField(max_length=1, default=0)
    student_664 = models.CharField(max_length=1, default=0)
    student_682 = models.CharField(max_length=1, default=0)
    student_703 = models.CharField(max_length=1, default=0)
    student_721 = models.CharField(max_length=1, default=0)
    student_740 = models.CharField(max_length=1, default=0)
    student_748 = models.CharField(max_length=1, default=0)
    student_758 = models.CharField(max_length=1, default=0)
    student_759 = models.CharField(max_length=1, default=0)
    student_763 = models.CharField(max_length=1, default=0)
    student_779 = models.CharField(max_length=1, default=0)
    student_808 = models.CharField(max_length=1, default=0)
    student_822 = models.CharField(max_length=1, default=0)
    student_831 = models.CharField(max_length=1, default=0)
    student_839 = models.CharField(max_length=1, default=0)
    student_847 = models.CharField(max_length=1, default=0)
    student_849 = models.CharField(max_length=1, default=0)
    student_856 = models.CharField(max_length=1, default=0)
    student_857 = models.CharField(max_length=1, default=0)
    student_861 = models.CharField(max_length=1, default=0)
    student_863 = models.CharField(max_length=1, default=0)
    student_871 = models.CharField(max_length=1, default=0)
    student_872 = models.CharField(max_length=1, default=0)
    student_877 = models.CharField(max_length=1, default=0)
    student_879 = models.CharField(max_length=1, default=0)
    student_882 = models.CharField(max_length=1, default=0)
    student_889 = models.CharField(max_length=1, default=0)
    student_895 = models.CharField(max_length=1, default=0)
    student_902 = models.CharField(max_length=1, default=0)
    student_906 = models.CharField(max_length=1, default=0)
    student_911 = models.CharField(max_length=1, default=0)
    student_921 = models.CharField(max_length=1, default=0)
    student_923 = models.CharField(max_length=1, default=0)
    student_925 = models.CharField(max_length=1, default=0)
    student_929 = models.CharField(max_length=1, default=0)
    student_930 = models.CharField(max_length=1, default=0)
    student_940 = models.CharField(max_length=1, default=0)
    student_961 = models.CharField(max_length=1, default=0)
    student_983 = models.CharField(max_length=1, default=0)
    student_989 = models.CharField(max_length=1, default=0)
    student_997 = models.CharField(max_length=1, default=0)
    student_1001 = models.CharField(max_length=1, default=0)
    student_1010 = models.CharField(max_length=1, default=0)
    student_1013 = models.CharField(max_length=1, default=0)
    student_1024 = models.CharField(max_length=1, default=0)
    student_1060 = models.CharField(max_length=1, default=0)
    student_1062 = models.CharField(max_length=1, default=0)
    student_1081 = models.CharField(max_length=1, default=0)
    student_1084 = models.CharField(max_length=1, default=0)
    student_1087 = models.CharField(max_length=1, default=0)
    student_1099 = models.CharField(max_length=1, default=0)
    student_1103 = models.CharField(max_length=1, default=0)
    student_1108 = models.CharField(max_length=1, default=0)
    student_1116 = models.CharField(max_length=1, default=0)
    student_1128 = models.CharField(max_length=1, default=0)
    student_1131 = models.CharField(max_length=1, default=0)
    student_1158 = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.code

    