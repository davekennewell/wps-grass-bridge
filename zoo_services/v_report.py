import ZOOGrassModuleStarter as zoo
def v_report(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.report", inputs, outputs)
    return 1
