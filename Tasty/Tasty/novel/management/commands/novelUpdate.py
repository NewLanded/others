from django.core.management.base import BaseCommand, CommandError
from spider.novel import Novel
from LOG.logger import Logger

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='+', type=str)

    def handle(self, *args, **options):
        for i in options['arguments']:
            if i == 'updateNovel':
                from spider.urlList import urlList
                novel = Novel()
                logger = Logger(logname='/root/Log/spider/novel.log', loglevel=1, logger="novel_time").getlog()
                for url in urlList:
                    try:
                        novel.start(url)
                    except:
                        logger.error('novelUpdate Faild-----'+url)

#        for i in options['arg']:
#            self.stdout.write
