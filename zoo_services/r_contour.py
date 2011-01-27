import ZOOGrassModuleStarter as zoo
def r_contour(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.contour", inputs, outputs)
    return 1
