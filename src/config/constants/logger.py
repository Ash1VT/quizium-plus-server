SIMPLE_LOG_FORMAT = (
    "<level>{level}</level> <cyan>{name}</cyan> <level>{message}</level>"
)

COMPREHENSIVE_LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <4}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)
