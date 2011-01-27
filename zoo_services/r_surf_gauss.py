import ZOOGrassModuleStarter as zoo
def r_surf_gauss(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.surf.gauss", inputs, outputs)
    return 1
