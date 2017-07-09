#coding:utf-8

from django.http import HttpResponse
import json
from novel.models import Novel,Novel_detail
from LOG.logger import Logger

# logger = Logger(logname='~/Log/novel/novelview.log', loglevel=1, logger="novelview").getlog()


def novel_list(request):
    novel_info = Novel.objects.all()
    r_novel = {}
    for novel in novel_info:
        r_novel[novel.id] = novel.novelname
    return HttpResponse(json.dumps(r_novel))

def novel_chapter_list(request):
    novel_id = request.POST.get('novelId', None)
    if novel_id:
        results = Novel_detail.objects.filter(novel_id=novel_id).order_by('-id')[:200]
        chapters = {}
        for chapter in results:
            chapters[chapter.id] = chapter.chapter_name
        return HttpResponse(json.dumps(chapters))

def novel_chapter_text(request):
    chapter_id = request.POST.get('chapterId', None)
    if chapter_id:
        result = Novel_detail.objects.filter(id=chapter_id)[0]
        chapter_text = result.chapter_text.replace(' ','<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
        return HttpResponse(json.dumps(chapter_text))

def next_chapter_text(request):
    chapter_id = request.POST.get('chapterId', None)
    novel_id = request.POST.get('novelId', None)
    if chapter_id and novel_id:
        result = Novel_detail.objects.filter(novel_id=novel_id, id__gt=chapter_id)[0]
        chapter_id = result.id
        chapter_text = result.chapter_text.replace(' ','<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
        chapter={'chapterId':chapter_id,'chapterText':chapter_text}
        return HttpResponse(json.dumps(chapter))

