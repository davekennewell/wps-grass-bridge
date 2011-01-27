import ZOOGrassModuleStarter as zoo
def r_sun(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.sun", inputs, outputs)
    return 1
