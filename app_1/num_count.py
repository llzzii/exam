import json
import docx
import re
from app_1.models import Exam
from app_1.models import ExamType
from django.core.paginator import Paginator
from django.core import serializers
import django
django.setup()


def uploadFile(request):
    # contains = json.loads(_open_andreadfile(request))
    if request.FILES.get("files", None).name.find(".txt"):
        contains = _open_andreadfile_txt(request)
    else:
        contains = _open_andreadfile(request)
    typeName = request.POST["type"]
    if(typeName == ''):
        typeName = request.FILES.get("files", None).name.split(".txt")[0]
    ExamList = []
    if contains:
        # Exam.objects.create(number=contains['number'], title=contains['title'],
        #                     answer=contains['answer'], resolve=contains[
        #     'resolve'], keys=contains['keys'])
        for contain in contains:
            a_pattern = re.compile('A([\\．\\.]|\\.)')
            b_pattern = re.compile('B[\\．\\.]')
            c_pattern = re.compile('C[\\．\\.]')
            d_pattern = re.compile('D[\\．\\.]')
            if len(a_pattern.findall(contain["keys"])) == 1 and len(b_pattern.findall(contain["keys"])) == 1:
                a_keys = re.findall(
                    "A[\\．\\.](.+?)B[\\．\\.]", contain["keys"])[0].strip()
                b_keys = re.findall(
                    "B[\\．\\.](.+?)C[\\．\\.]", contain["keys"])[0].strip()
                c_keys = re.findall(
                    "C[\\．\\.](.+?)D[\\．\\.]", contain["keys"])[0].strip()
                d_keys = contain["keys"].split('D.')[1].strip()
            if len(a_pattern.findall(contain["keys"])) == 2 and len(b_pattern.findall(contain["keys"])) == 2:
                a_keys = re.findall("A[\\．\\.](.+?)B[\\．\\.]", contain["keys"])[0].strip()+"-##-" + \
                    re.findall("A[\\．\\.](.+?)B[\\．\\.]",
                               contain["keys"])[1].strip()
                b_keys = re.findall("B[\\．\\.](.+?)C[\\．\\.]", contain["keys"])[0].strip()+"-##-" + \
                    re.findall("B[\\．\\.](.+?)C[\\．\\.]",
                               contain["keys"])[1].strip()
                c_keys = re.findall("C[\\．\\.](.+?)D[\\．\\.]", contain["keys"])[0].strip()+"-##-" + \
                    re.findall("C[\\．\\.](.+?)D[\\．\\.]",
                               contain["keys"])[1].strip()
                if len(re.compile('D．').findall(contain["keys"])) > 1:
                    d_keys = re.findall("D[\\．\\.](.+?)A[\\．\\.]", contain["keys"])[
                        0].strip()+"-##-" + contain["keys"].split('D．')[2].strip()
                if len(re.compile('D\\.').findall(contain["keys"])) > 1:
                    d_keys = re.findall("D[\\．\\.](.+?)A[\\．\\.]", contain["keys"])[
                        0].strip()+"-##-" + contain["keys"].split('D.')[2].strip()
            ExamList.append(Exam(number=contain["number"].strip(), title=contain["title"].strip(), type=typeName,
                                 answer=contain["answer"].strip(), resolve=contain["resolve"].strip(), a_key=a_keys, b_key=b_keys, c_key=c_keys, d_key=d_keys, keys=contain["keys"].strip()))
        Exam.objects.bulk_create(ExamList)
        ExamType.objects.get_or_create(type=typeName)

        list = Exam.objects.filter(type=typeName)
        return list
    else:
        models.result.objects.create(number=contains['number'], title=contains['title'],
                                     answer=contains['answer'], resolve=contains[
                                         'resolve'], keys=contains['keys'])


def _open_andreadfile(request):
    File = request.FILES.get("files", None)
    log_out_str = "./app_1/logs_files/" + File.name
    # log_content = open(log_out_str, "r", encoding="utf-8")
    log_content = docx.Document(log_out_str)
    parags = log_content.paragraphs
    allList = []
    for b in [parags[i:i + 7] for i in range(0, len(parags), 7)]:
        print(b)
        keys = b[1].text.split("\n")
        _result_list = json.dumps(
            {'number': b[0].text, 'title': keys[0], 'answer': b[3].text, 'resolve': b[5].text, 'a_keys': keys[1], 'b_keys': keys[2], 'c_keys': keys[3], 'd_keys': keys[4]})
        print(_result_list)
        allList.append(_result_list)
    return allList


def _open_andreadfile_txt(request):
    File = request.FILES.get("files", None)
    log_out_str = "./app_1/logs_files/" + File.name
    log_content = open(log_out_str, "r", encoding='utf-8')
    s = log_content.read()
    lists = re.split('试题\d+\(201\d+年[上下]半年试题.*\)', s)
    file_list = []
    for file_str in lists:
        if file_str.find('试题答案') > -1:
            title = re.sub('\n', '', re.split('（\d+）', file_str)[0])
            answer = re.findall("试题分析(.+?)试题答案", re.sub('\n', '', file_str))[0]
            resolve = re.sub('\n', '', file_str.split("试题答案")[1])
            keys = re.findall("（\d*）(.+?)试题分析", re.sub('\n', '', file_str))[0]
            _result_list = {'number': '', 'title': title,
                            'answer': answer, 'resolve': resolve, 'keys': keys}
            file_list.append(_result_list)
    log_content.close()
    return file_list


def getDataByType(request):
    if request.method == 'GET':
        typeName = request.GET.get('type')
        page = request.GET.get('page')
        if not page:
            page = 1
        else:
            page = int(page)
        datas = Exam.objects.filter(type=typeName)
        paginator = Paginator(datas, 10)  # 对数据进行分页，每页三条
        pageData = paginator.page(page)  # 获取具体页的数据
        page_data = []  # 对数据进行json结构化，json只接受字典对象
        for data in pageData:

            page_data.append(
                {
                    "title": data.title,
                    "a_key": data.a_key,
                    "b_key": data.b_key,
                    "c_key": data.c_key,
                    "d_key": data.d_key,
                    "answer": data.answer,
                    "resolve": data.resolve,
                    "id": data.id
                }
            )
        result = {
            "pageData": page_data,
            "totalnum": paginator.num_pages
        }
        return result


def getTypeData(request):
    datas = serializers.serialize("json", ExamType.objects.all())
    return datas


def load(request):
    # datas = Exam.objects.all()
    datas = serializers.serialize("json", Exam.objects.all())
    # pagenum = request.GET.get('page')
    # if pagenum is None:
    #     pagenum = 1
    # 构建分页器对象,datas,10=每页显示的个数
    # paginator = Paginator(datas, 10)
    # 获取第n页的页面对象
    # page = paginator.page(pagenum)
    # Paginator和Page的常用API
    # page.previous_page_number()
    # page.next_page_number()
    # page.has_previous()
    # page.has_next()
    # 构造页面渲染的数据
    '''
    渲染需要的数据:
    - 当前页列表
    - 分页页码范围
    - 当前页的页码
    '''
    # data = {
    #     # 当前列表
    #     'page': page.object_list,
    #     # 分页页码范围
    #     # 'pagerange': paginator.page_range,
    #     # 总条数
    #     "total": paginator.count,
    #     # 总页数
    #     "pageTatal": paginator.num_pages,
    #     # 当前页的页码
    #     'currentpage': paginator.page_range.stop,
    # }
    return datas
