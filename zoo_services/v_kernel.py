import ZOOGrassModuleStarter as zoo
def v_kernel(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.kernel", inputs, outputs)
    return 1
