from loguru import logger

logger.info("hello world")

logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

logger.add("a.log", format="{time:YYYY-MM-DD  HH:mm:ss}  |  {level}  | {module}  |  {message}", level="DEBUG")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

logger.info("我的名字叫{}，今天星期{}", "小争", "2")
