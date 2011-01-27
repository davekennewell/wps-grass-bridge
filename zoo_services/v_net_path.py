import ZOOGrassModuleStarter as zoo
def v_net_path(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.path", inputs, outputs)
    return 1
