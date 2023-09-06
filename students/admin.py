from django.contrib import admin

from students.models import StudentWallet


class SA(admin.ModelAdmin):
    list_display = ('id', 'student', 'donates')


admin.site.register(StudentWallet, SA)
