import logging


class CentralLogger:

    def log_for_woj(self, mod_name, log_type, e):
        logger = logging.getLogger(mod_name)
        if log_type == 'ERROR':
            f_handler = logging.FileHandler('JHULogFile.log')
            f_handler.setLevel(logging.ERROR)
            f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(f_handler)
            logger.error('Error raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'DEBUG':
            logger.debug('Debug info raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'WARNING':
            logger.debug('Warning raised in %s. Details are: %s', mod_name, e)
