import pymysql
from django.shortcuts import render, redirect


# 显示班级列表
# 参数列表上有一个request，切记，切记
def classes(request):
    # 连接mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123456', db='studentManager',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,title from class')
    # 返回多个值
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123456', db='studentManager',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        v = request.POST.get('title')
        cursor.execute('insert into class(title) values (%s)', [v, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def edit_class(request):
    # 点击编辑按钮，根据Id获取到class信息 传入到下一个页面中
    if request.method == 'GET':
        id = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123456', db='studentManager',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select id,title from class where id = %s', [id, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, 'edit_class.html', {'result': result})
    else:
        id = request.POST.get('id')
        title = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123456', db='studentManager',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        v = request.POST.get('title')
        cursor.execute('update class set title =%s where id=%s', [title, id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def del_class(request):
    id = request.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123456', db='studentManager',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from class where id = %s', [id, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')
