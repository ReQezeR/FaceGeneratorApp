from rest_framework import routers
from FaceProviderApp import views as FPA_views

router = routers.DefaultRouter()
router.register(r'Image', FPA_views.ImageViewset)
router.register(r'LeftEarVector', FPA_views.LeftEarVectorViewset)
router.register(r'RightEarVector', FPA_views.RightEarVectorViewset)
router.register(r'LeftEyeVector', FPA_views.LeftEyeVectorViewset)
router.register(r'RightEyeVector', FPA_views.RightEyeVectorViewset)
router.register(r'HairVector', FPA_views.HairVectorViewset)
router.register(r'MouthVector', FPA_views.MouthVectorViewset)
router.register(r'NoseVector', FPA_views.NoseVectorViewset)
router.register(r'LeftEyebrowVector', FPA_views.LeftEyebrowVectorViewset)
router.register(r'RightEyebrowVector', FPA_views.RightEyebrowVectorViewset)
router.register(r'SuitVector', FPA_views.SuitVectorViewset)
