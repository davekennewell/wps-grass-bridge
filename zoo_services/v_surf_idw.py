import ZOOGrassModuleStarter as zoo
def v_surf_idw(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.surf.idw", inputs, outputs)
    return 1
