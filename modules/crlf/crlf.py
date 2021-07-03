import config
import utils
from log import logger
from utils import invokeCommand

def runcrlfpy(urls_file:str,result_file:str) :
    cmd=f" {config.gwen_crlfpy_command} -v 4 -u  {urls_file}  -O  {result_file}  -t 80"
    logger.log('info', f'Running crlfpy with command {cmd}')
    invokeCommand(cmd)




def crlfWrapper():
    runcrlfpy(config.waybackurls_withquery_live_file,config.crlfpy_result_file)
    utils.filterNegativeFile(config.crlfpy_result_file)
