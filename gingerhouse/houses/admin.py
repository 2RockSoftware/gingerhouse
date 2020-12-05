from django.contrib import admin


from gingerhouse.houses.models import Category, GingerHouse, Vote


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class GingerHouseAdmin(admin.ModelAdmin):
    list_display = ("name", "vote_count")
    
    def vote_count(self, obj):
        return obj.vote_set.all().count()


class VoteAdmin(admin.ModelAdmin):
    list_display = ("email", "ginger_house")
    list_filter = ("ginger_house", "ginger_house__category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(GingerHouse, GingerHouseAdmin)
admin.site.register(Vote, VoteAdmin)
