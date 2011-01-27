import ZOOGrassModuleStarter as zoo
def r_texture(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.texture", inputs, outputs)
    return 1
