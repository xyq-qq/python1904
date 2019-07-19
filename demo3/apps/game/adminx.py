import xadmin
from .models import Account,Hero,Pet,Petdetail,Goods,Othergoods,Warsprit,Attck,Arms,Ads,Notice,News,NewsDetail

xadmin.site.register(Account)
xadmin.site.register(Hero)
xadmin.site.register(Pet)
xadmin.site.register(Petdetail)
xadmin.site.register(Goods)
xadmin.site.register(Othergoods)
xadmin.site.register(Warsprit)
xadmin.site.register(Attck)
xadmin.site.register(Arms)
xadmin.site.register(Ads)
xadmin.site.register(Notice)
xadmin.site.register(News)
class NewsDetailAdmin:
    style_fields={'content':'ueditor'}

xadmin.site.register(NewsDetail,NewsDetailAdmin)


