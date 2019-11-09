"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet,BannerViewset,HotSearchViewset,IndexCategoryViewset
from apps.users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset,AddressViewset
from trade.views import ShoppingCartViewSet,OrderViewSet

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods-list")

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

router.register(r'codes', SmsCodeViewset, base_name="codes")

router.register(r'users', UserViewset, base_name="users")

# 收藏
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 留言
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 热词搜索
router.register(r'hotsearchs', HotSearchViewset, base_name="hotsearchs")

# 收货地址
router.register(r'address', AddressViewset, base_name="address")

# 轮播图
router.register(r'banners', BannerViewset, base_name="banners")

# 购物车
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

# 订单相关
router.register(r'orders', OrderViewSet, base_name="orders")

# 首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页
    # url(r'goods/$',goods_list,name='goods-list'),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='暮雪生鲜')),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口
    url(r'^login/$', obtain_jwt_token),
]
