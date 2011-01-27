import ZOOGrassModuleStarter as zoo
def v_parallel(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.parallel", inputs, outputs)
    return 1
