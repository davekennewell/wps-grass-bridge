import ZOOGrassModuleStarter as zoo
def r_patch(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.patch", inputs, outputs)
    return 1
