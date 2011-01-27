import ZOOGrassModuleStarter as zoo
def v_surf_rst(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.surf.rst", inputs, outputs)
    return 1
