from django.db import models


class Obj(models.Model):
    name = models.CharField(max_length=30)
    short = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.short

    class Meta:
        unique_together = ('name', 'short')


class Attribute(models.Model):
    attribute = models.CharField(max_length=30)
    short = models.CharField(max_length=3, unique=True)

    def __unicode__(self):
        return self.short

    class Meta:
        unique_together = ('attribute', 'short')


class ObjAtt(models.Model):
    obj = models.ForeignKey(Obj)
    att = models.ForeignKey(Attribute)

    def obj_name(self):
        return self.obj.name

    def obj_short(self):
        return self.obj.short

    def att_name(self):
        return self.att.attribute

    def att_short(self):
        return self.att.short

    def __unicode__(self):
        return '%s: %s' % (self.obj.short, self.att.short)

    class Meta:
        unique_together = ('obj', 'att')
