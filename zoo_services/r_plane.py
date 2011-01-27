import ZOOGrassModuleStarter as zoo
def r_plane(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.plane", inputs, outputs)
    return 1
