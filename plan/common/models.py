from datetime import datetime

from django.db import models

class UserSet(models.Model):
    slug = models.SlugField()
    course = models.ForeignKey('Course')
#    semester = models.ForeignKey('Semester')
    groups = models.ManyToManyField('Group', blank=True, null=True)

    exclude = models.ManyToManyField('Lecture', blank=True, null=True)

    class Meta:
        unique_together = (('slug', 'course'),)
        ordering = ('slug', 'course')

    def __unicode__(self):
        return '%s - %s' % (self.slug, self.course)

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    optional = models.BooleanField()

    def __unicode__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    full_name = models.TextField(blank=True)
    url = models.URLField(verify_exists=False, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Semester(models.Model):
    SPRING = 0
    FALL = 1
    TYPES = (
        (SPRING, 'spring'),
        (FALL, 'fall'),
    )
    year = models.PositiveSmallIntegerField(choices=[(x,x) for x in range(datetime.now().year-1,datetime.now().year+2)])
    type = models.PositiveSmallIntegerField(choices=TYPES)

    def __unicode__(self):
        return '%s %s' % (self.get_type_display(), self.year)

    class Meta:
        ordering = ('-year', '-type')

#class Exam(models.Model):
#    time = models.DateTimeField()
#    duration = models.PositiveSmallIntegerField()
#
#    semester = models.ForeignKey(Semester)
#    course = models.ForeignKey(Course)

class Week(models.Model):
    number = models.PositiveSmallIntegerField(choices=[(x,x) for x in range(1,53)], unique=True)

    def __unicode__(self):
        return 'week %s' % self.number

    class Meta:
        ordering = ('number',)

#class Lecturer(models.Model):
#    name = models.CharField(max_length=200)

class Lecture(models.Model):
    START = [(i, '%02d:15' % i) for i in range(8,21)]
    END = [(i, '%02d:00' % i) for i in range(9,22)]

    DAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
    )

    course = models.ForeignKey(Course)
    semester = models.ForeignKey(Semester)

    day = models.PositiveSmallIntegerField(choices=DAYS)

    start_time = models.PositiveSmallIntegerField(choices=START)
    end_time  = models.PositiveSmallIntegerField(choices=END)

    room = models.ForeignKey(Room, blank=True, null=True)
    type = models.ForeignKey(Type, blank=True, null=True)
    weeks = models.ManyToManyField(Week, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)
#    lectures = models.ManyToManyField(Lecturer, blank=True, null=True)


    def __unicode__(self):
        return u'%s: %s-%s on %s' % (self.course, self.get_start_time_display(), self.get_end_time_display(), self.get_day_display())

    class Meta:
        ordering = ('course', 'day', 'start_time')
