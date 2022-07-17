import logging


class CentralLogger:

    def log_for_woj(self, mod_name, log_type, e):
        logger = logging.getLogger(mod_name)
        if log_type == 'ERROR':
            logger.error('Error raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'DEBUG':
            logger.debug('Debug info raised in %s. Details are: %s', mod_name, e)
        elif log_type == 'WARNING':
            logger.debug('Warning raised in %s. Details are: %s', mod_name, e)
