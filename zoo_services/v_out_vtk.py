import ZOOGrassModuleStarter as zoo
def v_out_vtk(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.out.vtk", inputs, outputs)
    return 1
