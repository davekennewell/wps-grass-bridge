import ZOOGrassModuleStarter as zoo
def r_solute_transport(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.solute.transport", inputs, outputs)
    return 1
