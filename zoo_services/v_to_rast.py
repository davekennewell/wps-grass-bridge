#####################################################
# This service was generated using wps-grass-bridge #
#####################################################
import ZOOGrassModuleStarter as zoo
def v_to_rast(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.to.rast", inputs, outputs)
    return 3
