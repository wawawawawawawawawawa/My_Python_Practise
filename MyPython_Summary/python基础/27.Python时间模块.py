# time模块：提供两种时间表达方式：
# 1.假定一个零点基准，偏移长度换算为按秒的数值型
# 2.由9个整数组成的元组struct_time表示的时间


# datetime模块：常用类有四个
# 1.date：日期类，包括属性年月日以及相关方法
# 2.time：时间类，包括属性时分秒等及相关方法
# 3.datetime：日期时间，继承与date，包括属性年月日时分秒等及相关方法，其中年月日必须参数
# 4.timedelta: 两个datetime值的差，比如相差几天，几小时，几分等


# 除了以上两个模块，calendar模块还提供一些实用的功能，比如：
# 年月的日历图
# 闰年判断
# 月有几天等

# time模块：
import time

# 1.当前时间浮点数
seconds = time.time()
print(seconds)
# 2.时间数组
local_time = time.localtime(seconds)
print(local_time)
# 3.时间字符串
# time类的 asctime 方法，转换 struct_time 为时间字符串
str_time = time.asctime(local_time)
print(str_time)
# 4.格式化时间字符串
format_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(format_time)
# 5.转化字符时间为时间数组,注意这里的第二个参数的时间格式，要匹配上第一个参数的时间格式
str_to_struct = time.strptime(format_time, '%Y-%m-%d %H:%M:%S')
print(str_to_struct)

# datetime模块：
from datetime import date, datetime, time, timedelta

# 1.date
# 打印当前日期
tod = date.today()
print(tod)
# 打印当前日期字符串
str_date = date.strftime(tod, '%Y-%m-%d')
print(str_date)
# 字符日期转日期，date类没有strptime方法,它的子类datetime才有
str_to_date = datetime.strptime('2020-02-22', '%Y-%m-%d')
print(str_to_date)

# 2.datetime
# 打印当前时间
right = datetime.now()
print(right)
# 当前时间转字符串显示
str_time = datetime.strftime(right, '%Y-%m-%d %H:%M:%S')
print(str_time)
# 字符时间转时间类型
str_to_time = datetime.strptime('2020-02-22 15:12:33', '%Y-%m-%d %H:%M:%S')
print(str_to_time)


# 3.timedelta:求两个datetime类型值的差，返回差几天，差几个小时等
# 就算距离女朋友生日还有几天
def get_days_girlfriend(birthday):
    import re
    splits = re.split(r'[-.\s+/]', birthday)
    splits = [s for s in splits if s]
    if len(splits) < 3:
        raise ValueError('输入格式不正确，至少包括年月日')
    splits = splits[:3]
    birthday = datetime.strptime('-'.join(splits), '%Y-%m-%d')
    tod = date.today()
    delta = birthday.date() - tod  # 这一步的.date()使得birthday返回了date类型的对象的年月日
    return delta.days


print(get_days_girlfriend('2020-04-08'))

# 绘制年的日历图
import calendar

mydate = date.today()
year_calendar_str = calendar.calendar(2020)
print(f'{mydate.year}年的日历图：{year_calendar_str}')

# 月的日历图
month_calendar_str = calendar.month(mydate.year, mydate.month)
print(f"{mydate.year}年{mydate.month}月的日历图：{month_calendar_str}\n")

# 判断是否是闰年
is_leap = calendar.isleap(mydate.year)
print(f"{mydate.year}是闰年" if is_leap else f"{mydate.year}不是闰年")

# 判断月有几天
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f"{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday + 1}天\n")  # 0-6对应周一到周日
print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')




