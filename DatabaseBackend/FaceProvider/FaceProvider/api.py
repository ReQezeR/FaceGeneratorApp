from rest_framework import routers
from FaceProviderApp import views as FPA_views

router = routers.DefaultRouter()
router.register(r'Image', FPA_views.ImageViewset)
router.register(r'Image', FPA_views.LeftEarVectorViewset)
router.register(r'Image', FPA_views.RightEarVectorViewset)
router.register(r'Image', FPA_views.LeftEyeVectorViewset)
router.register(r'Image', FPA_views.RightEyeVectorViewset)
router.register(r'Image', FPA_views.HairVectorViewset)
router.register(r'Image', FPA_views.MouthVectorViewset)
router.register(r'Image', FPA_views.NoseVectorViewset)
router.register(r'Image', FPA_views.LeftEyebrowVectorViewset)
router.register(r'Image', FPA_views.RightEyebrowVectorViewset)
router.register(r'Image', FPA_views.SuitVectorViewset)
