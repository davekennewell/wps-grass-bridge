import ZOOGrassModuleStarter as zoo
def r_to_vect(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.to.vect", inputs, outputs)
    return 1
