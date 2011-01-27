import ZOOGrassModuleStarter as zoo
def v_overlay(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.overlay", inputs, outputs)
    return 1
