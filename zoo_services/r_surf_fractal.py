import ZOOGrassModuleStarter as zoo
def r_surf_fractal(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.surf.fractal", inputs, outputs)
    return 1
