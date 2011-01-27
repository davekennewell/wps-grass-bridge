import ZOOGrassModuleStarter as zoo
def r_regression_line(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.regression.line", inputs, outputs)
    return 1
