import ZOOGrassModuleStarter as zoo
def r_random_surface(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.random.surface", inputs, outputs)
    return 1
