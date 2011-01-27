import ZOOGrassModuleStarter as zoo
def r_surf_contour(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.surf.contour", inputs, outputs)
    return 1
