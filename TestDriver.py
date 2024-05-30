from tests.HelloAPI.t_HelloAPI import t_HelloAPI
from tests.config.t_config import settings
from tests.schemas.TestConfigSchema import TestConfigSchema

_cfg = TestConfigSchema.FromDict(name="TestDriverConfig", all_elements=settings, logger=None)
if _cfg.EnabledTests.get('HELLO', False):
    test_Hello = t_HelloAPI()
    print("***\nRunning test_Hello:")
    test_Hello.RunAll()
    print("Done\n***")