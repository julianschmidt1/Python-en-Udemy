import logging

logger=logging
logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s %(filename)s : %(lineno)s %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])
if __name__ == '__main__':
    logging.warning("msj warning")
    logging.info("Mensaje info")
    logging.debug("Mensaje debug")
    logging.error("mensaje error")