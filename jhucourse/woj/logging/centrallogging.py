import logging


class CentralLogger:

    def log_for_woj(self, mod_name, log_type, e):
        logger = logging.getLogger(mod_name)

        f_handler = logging.FileHandler('JHULogFile.log')
        f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        c_handler = logging.StreamHandler()
        c_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

        logger.addHandler(f_handler)
        logger.addHandler(c_handler)
        logger.setLevel(logging.DEBUG)

        if log_type == 'ERROR':
            f_handler.setLevel(logging.ERROR)
            logger.error('Error raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'DEBUG':
            c_handler.setLevel(logging.DEBUG)
            logger.debug('Debug info raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'INFO':
            f_handler.setLevel(logging.INFO)
            logger.info('Information raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'WARNING':
            f_handler.setLevel(logging.WARNING)
            logger.warning('Warning raised in %s. Details are: %s', mod_name, e)
