import ZOOGrassModuleStarter as zoo
def v_segment(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.segment", inputs, outputs)
    return 1
