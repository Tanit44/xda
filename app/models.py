from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(default = 'Admin', max_length = 100)

class UserType(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Gender(models.Model):
    gname = models.CharField(max_length=225)

    def __str__(self):
        return self.gname

class Level(models.Model):
    lname = models.CharField(max_length=225)

    def __str__(self):
        return self.lname

class Pro(models.Model):
    pname = models.CharField(max_length=225)

    def __str__(self):
        return self.pname

class Edu(models.Model):
    ename = models.CharField(max_length=225)

    def __str__(self):
        return self.ename
    
class TableAll(models.Model):
    nId_person = models.CharField(verbose_name='รหัส', max_length=100)
    cGender = models.CharField(verbose_name='เพศ',max_length=19, blank=True, null=True)
    cFname = models.CharField(verbose_name='ชื่อ-นามสกุล',max_length=100)
    nAge = models.IntegerField(verbose_name='อายุ',blank=True,null=True)
    cLevel = models.CharField(verbose_name='ธรรมวุฒิ',max_length = 100, blank=True, null=True)
    cEdu = models.CharField(verbose_name='การศึกษา',max_length = 100, blank=True, null=True)
    cCareer = models.CharField(verbose_name='อาชีพ',max_length = 100, blank=True, null=True)
    cRoom = models.CharField(verbose_name='พุทธสถาน',max_length = 100, blank = True, null = True)
    cRoom_c = models.CharField(verbose_name='พุทธสถาน(จีน)',max_length = 100, blank = True, null = True)
    cPro = models.CharField(verbose_name='อ.ถ่ายทอดเบิกธรรม',max_length = 100, blank=True, null=True)
    cPro_c = models.CharField(verbose_name='อ.ถ่ายทอดเบิกธรรม(จีน)',max_length = 100, blank = True, null = True)
    cDate_c = models.CharField(verbose_name='วันรับธรรมะ(ภาษาจีน)',max_length = 100, blank = True, null = True)
    cDate_dc = models.CharField(verbose_name='วันรับธรรมะ(จีน)',max_length = 100, blank = True, null = True)
    cTdate = models.CharField(verbose_name='วันรับธรรมะ(ไทย)',max_length = 100, blank = True, null = True)
    dDate = models.DateField(verbose_name='วันรับธรรมะ',blank = True, null = True)
    cRec = models.CharField(verbose_name='อ.แนะนำ',max_length = 100, blank = True, null = True)
    cSup = models.CharField(verbose_name='อ.รับรอง',max_length = 100, blank = True, null = True)
    cAddress = models.CharField(verbose_name='ที่อยู่',max_length = 100, blank = True, null = True)
    cMtel = models.CharField(verbose_name='โทรศัพท์มือถือ',max_length = 100, blank = True, null = True)
    cHtel = models.CharField(verbose_name='โทรศัพท์บ้าน',max_length = 100, blank = True, null = True)
    cName = models.CharField(verbose_name='ชื่อจีน',max_length=100,blank=True,null=True)
    c3dd = models.CharField(max_length = 100, blank = True, null = True)# 3 วัน (ว/ด/ป)
    c3dl = models.CharField(max_length = 100, blank = True, null = True)# 3 วัน (สถานธรรม)
    cMd = models.CharField(max_length = 100, blank = True, null = True)# หมิงเต๋อ (ว/ด/ป)
    cMl = models.CharField(max_length = 100, blank = True, null = True)# หมิงเต๋อ (สถานธรรม)
    cSd = models.CharField(max_length = 100, blank = True, null = True)# ซินหมิน (ว/ด/ป)
    cSl = models.CharField(max_length = 100, blank = True, null = True)# ซินหมิน (สถานธรรม)
    cJd = models.CharField(max_length = 100, blank = True, null = True)# จื่อซั่น (ว/ด/ป)
    cJl = models.CharField(max_length = 100, blank = True, null = True)# จื่อซั่น (สถานธรรม)
    cPt1 = models.CharField(max_length = 3, blank = True, null = True)
    cPt2 = models.CharField(max_length = 3, blank = True, null = True)
    cPt3 = models.CharField(max_length = 3, blank = True, null = True)
    cPt4 = models.CharField(max_length = 3, blank = True, null = True)
    cPt5 = models.CharField(max_length = 3, blank = True, null = True)
    cPt6 = models.CharField(max_length = 3, blank = True, null = True)
    cCd = models.CharField(max_length = 100, blank = True, null = True)
    cCl = models.CharField(max_length = 100, blank = True, null = True)
    cCp = models.CharField(max_length = 100, blank = True, null = True)
    cUd = models.CharField(max_length = 100, blank = True, null = True)
    cUl = models.CharField(max_length = 100, blank = True, null = True)
    cUp = models.CharField(max_length = 100, blank = True, null = True)
    cRd = models.CharField(max_length = 100, blank = True, null = True)
    cRl = models.CharField(max_length = 100, blank = True, null = True)
    cRp = models.CharField(max_length = 100, blank = True, null = True)
    cPd = models.CharField(max_length = 100, blank = True, null = True)
    cPl = models.CharField(max_length = 100, blank = True, null = True)
    cPp = models.CharField(max_length = 100, blank = True, null = True)
    cJvd = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงเอวี๋ยน (ว/ด/ป)
    cJvl = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงเอวี๋ยน (สถานธรรม)
    cJvp = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงเอวี๋ยน (ตฉซ)
    cTjd = models.CharField(max_length = 100, blank = True, null = True)
    cTjl = models.CharField(max_length = 100, blank = True, null = True)
    cTjp = models.CharField(max_length = 100, blank = True, null = True)
    cJcd = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงซือ (ว/ด/ป)
    cJcl = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงซือ (สถานธรรม)
    cJcp = models.CharField(max_length = 100, blank = True, null = True)# เจี่ยงซือ (ตฉซ)
    cPrd = models.CharField(max_length = 100, blank = True, null = True)
    cPrl = models.CharField(max_length = 100, blank = True, null = True)
    cPrp = models.CharField(max_length = 100, blank = True, null = True)
    cb3d = models.BooleanField(default=False) # 3 วัน check-box
    cbM = models.BooleanField(default=False) # หมิงเต๋อ check-box
    cbS = models.BooleanField(default=False) # ซินหมิน check-box
    cbJ = models.BooleanField(default=False) # จื่อซั่น check-box
    cbJv = models.BooleanField(default=False) # เจี่ยงเอวี๋ยน check-box
    cbJc = models.BooleanField(default=False) # เจี่ยงซือ check-box
    cbReview = models.BooleanField(default=False) # ชั้น ทบทวน check-box
    cbAdv = models.BooleanField(default=False) # ชั้น พระสูตร check-box
    cbDd = models.BooleanField(default=False) # วันเสียชืวิต check-box
    cDd = models.CharField(max_length = 100, blank = True, null = True)# วันเสียชืวิต (ว/ด/ป)
    cJv_detail = models.TextField(blank = True, null = True) # เจี่ยงเอวี๋ยน รายละเอียดการศึกษา 
    cJc_detail = models.TextField(blank = True, null = True) # เจี่ยงซือ รายละเอียดการศึกษา 
    cReview_detail = models.TextField(blank = True, null = True) # ชั้น ทบทวน รายละเอียดการศึกษา 
    cAdv_detail = models.TextField(blank = True, null = True) # ชั้น พระสูตร รายละเอียดการศึกษา 

# รวม กทม
class Bkk(TableAll): # name of alltable bkk
    pass
# กทม ย่อย
class Bkk1(Bkk): # name of alltable bkk1
    pass
# หมิงซิน
class Bkk101(Bkk1): # name of of table
    pass
# หมิงฮุย
class Bkk102(Bkk1): # name of of table
    pass
# ฉือเฉิง
class Bkk103(Bkk1): # name of of table
    pass

class Bkk104(Bkk1): # name of of table
    pass

# รวมสระแก้ว
class Skw(TableAll): # name of alltable skw
    pass
# กบินทร์บุรี
class Skw1(Skw): # name of alltable skw1
    pass
# ฝ่าเซิ่ง
class Skw101(Skw1): # name of of table
    pass
# ฉืออี
class Skw102(Skw1): # name of of table
    pass
# ฉือจิ้ง  
class Skw103(Skw1): # name of of table
    pass
    
class Skw104(Skw1): # name of of table
    pass

# อรัญประเทศ
class Skw3(Skw): # name of alltable skw3
    pass
# ซิ่นเต๋อ
class Skw301(Skw3): # name of of table
    pass

class Skw302(Skw3): # name of of table
    pass

class Skw303(Skw3): # name of of table
    pass

class Skw304(Skw3): # name of of table
    pass

# รวมโคราช
class Nma(TableAll): # name of alltable Nma
    pass
# โคราช ย่อย 1
class Nma1(Nma): # name of alltable nma1
    pass
# ฉืออี้
class Nma101(Nma1): # name of of table
    pass
# ฉือซิน
class Nma102(Nma1): # name of of table
    pass
    
class Nma103(Nma1): # name of of table
    pass
    
class Nma104(Nma1): # name of of table
    pass

# รวมพิษณุโลก
class Plk(TableAll): # name of alltable Plk
    pass
# พิษณุโลก ย่อย 1
class Plk1(Plk): # name of alltable plk1
    pass
# เต้าเซิง
class Plk101(Plk1): # name of of table
    pass

class Plk102(Plk1): # name of of table
    pass
    
class Plk103(Plk1): # name of of table
    pass
    
class Plk104(Plk1): # name of of table
    pass
