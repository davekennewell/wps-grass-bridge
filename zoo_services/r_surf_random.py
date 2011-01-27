import ZOOGrassModuleStarter as zoo
def r_surf_random(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.surf.random", inputs, outputs)
    return 1
