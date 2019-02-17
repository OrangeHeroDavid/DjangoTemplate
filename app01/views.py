from django.shortcuts import render
import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        return '好嗨呦 感觉人生到达了巅峰'

    def __str__(self):
        return "<Person object: {}-{}>".format(self.name, self.age)


def template_test(request):
    string = 'hello world'
    num = '1'
    liit1 = ['alex', 'peiqi', 'tailiang']
    dict1 = {'name': 'alex', "age": 84, 'keys': 'xxxxx'}

    p1 = Person('OrangeHeroDavid', 25)

    return render(request,
                  'template_test.html', {
                      'name': 'alex',
                      'string': string,
                      'num': num,
                      'liit1': liit1,
                      'dict1': dict1,
                      'p1': p1,
                      'kong': [11111, 22222],
                      'filesize': 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
                      'long_str': """You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
            """,
                      'now': datetime.datetime.now(),
                      'js': """
                    <script>
                    
                        for (var i=0;i<5;i++){
                            alert('11111')
                        }
                    </script>""",
                      'a': '<a href="https://www.cnblogs.com/maple-shaw/articles/9333821.html">点击</a>'

                  })


def template_tags(request):
    return render(request, 'template_tags.html', {
        'list1': [['alex', 'peiqi', 'tailiang'], ['alex1', 'peiqi1', 'tailiang1']],
        'kong': ['alex', 'peiqi', 'tailiang'],
        'user_list': ['alex', 'peiqi', 'tailiang'],
    })
