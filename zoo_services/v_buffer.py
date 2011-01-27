import ZOOGrassModuleStarter as zoo
def v_buffer(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.buffer", inputs, outputs)
    return 1
