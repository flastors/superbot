from loguru import logger

logger.add(lambda msg: ..., format='[{time}] [{level}] [{file.name}:{line}]  {message}',
           level='DEBUG')