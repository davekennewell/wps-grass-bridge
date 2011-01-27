import ZOOGrassModuleStarter as zoo
def v_net_visibility(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.visibility", inputs, outputs)
    return 1
