#coding:utf-8
import logging
import logging.handlers
import os,subprocess
#日志系统，写入日志文件，每天凌晨切换日志
class Logger():
    def __init__(self, logname, loglevel, logger):
        '''
           指定保存日志的日志文件名，日志级别，以及handler名称---日志级别暂时未用到
           将日志存入到指定的文件中
        '''

        # 创建日志文件
        if not os.path.exists(logname):
            folder = os.path.dirname(logname)

            if not os.path.exists(folder):
                cmds = ['mkdir', folder]
                subprocess.check_output(cmds, shell=False)

            cmds = ['touch', logname]
            subprocess.check_output(cmds, shell=False)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件，并切换日志
        sf = logging.handlers.TimedRotatingFileHandler(logname,'midnight',1)
        sf.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s')
        sf.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(sf)


    def getlog(self):
        return self.logger
