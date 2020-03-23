# # 事件循环启动一个统一的调度器，让调度器决定一个时刻去运行哪个任务，于是省却了多线程中启动线程，管理线程，同步锁等开销
# import time
# import asyncio
# import random
#
#
# # def crawl_page(url):
# #     print('crawling {}'.format(url))
# #     sleep_time = int(url.split('_')[-1])
# #     time.sleep(sleep_time)
# #     print('OK {}'.format(url))
# #
# #
# # def main(urls):
# #     for url in urls:
# #         crawl_page(url)
# #
# # main(['url_1', 'url_2', 'url_3', 'url_4'])
# # # 这里的运行时间会是10s，及每次执行的累计
# #
# # async def crawl_page(url):
# #     print('crawling {}'.format(url))
# #     sleep_time = int(url.split('_')[-1])
# #     await asyncio.sleep(sleep_time)
# #     print('OK {}'.format(url))
# #
# #
# # async def main(urls):
# #     for url in urls:
# #         await crawl_page(url)
# #
# # asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# # # 这里的红线不影响运行
# # # 这是协程写的异步程序，这里使用async修饰声明异步函数，使得crawl_page和main都变成异步函数，而调用异步函数便可以得到一个协程对象(coroutine object)
# #
# # # 写成常用的三种执行方法：
# # # 方式一：await：await执行的效果和python正常执行是一样的，也就是说程序会阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续
# # # 代码中await asyncio.sleep(sleep_time)会在这里休息若干秒，await crawl_page(url)则会执行crawl_page()函数
# # # 方式二：使用asyncio.create_task()来创建任务
# # # 方式三：需要使用asyncio.run来触发运行，这是python3.7之后才有的特性
# # # 因为await是同步调用，所以这个版本还是运行10s，相当于使用异步接口写了同步代码
# #
# #
# # async def crawl_page(url):
# #     print('crawling {}'.format(url))
# #     sleep_time = int(url.split('_')[-1])
# #     await asyncio.sleep(sleep_time)
# #     print('OK {}'.format(url))
# #
# #
# # async def main(urls):
# #     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
# #     for task in tasks:
# #         await task
# # asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# # # 这里*task是解包列表，将列表变成了函数的参数，与之相对应的是 **dict将字典变成了函数的参数
# #
# # # 解密协程的运行
# # async def worker_1():
# #     print('worker_1start')
# #     await asyncio.sleep(1)
# #     print('worker1_end')
# #
# #
# # async def worker_2():
# #     print('worker_2start')
# #     await asyncio.sleep(1)
# #     print('worker_2end')
# #
# # async def main():
# #     print("before await")
# #     await worker_1()
# #     print("awaited worker_1")
# #     await worker_2()
# #     print("awaited worker_2")
# #
# # asyncio.run(main())
# # # 这是使用await的方式
# #
# #
# # async def worker_3():
# #     print('worker_3start')
# #     await asyncio.sleep(1)
# #     print('worker3_end')
# #
# #
# # async def worker_4():
# #     print('worker_4start')
# #     await asyncio.sleep(1)
# #     print('worker_4end')
# #
# # async def main():
# #     task1 = asyncio.create_task(worker_3())
# #     task2 = asyncio.create_task(worker_4())
# #     print('before await')
# #     await task1
# #     print('waited worked3')
# #     await task2
# #     print('waited worked4')
# # asyncio.run(main())
# # # 这是异步调用task版本
# #
# #
# # # 给协程限定运行时间以及错误处理
# # async def worker_5():
# #     await asyncio.sleep(1)
# #     return 1
# #
# #
# # async def worker_6():
# #     await asyncio.sleep(1)
# #     return 2/0
# #
# #
# # async def worker_7():
# #     await asyncio.sleep(3)
# #     return 3
# #
# #
# # async def main():
# #     task_1 = asyncio.create_task(worker_5())
# #     task_2 = asyncio.create_task(worker_6())
# #     task_3 = asyncio.create_task(worker_7())
# #
# #     await asyncio.sleep(2)
# #     task_3.cancel()
# #
# #     res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
# #     print(res)
# #
# # asyncio.run(main())
# # # 结果中第一个正常运行，第二个出现运行错误，第三个执行时间过程被cancel掉了，都表现在结果res中
# # # 需要注意的是return_exceptions=True,没有这个参数就需要try—catch捕捉异常
#
#
# # 协程版的生产者与消费者模型
# async def consumer(queue, id):
#     while True:
#         val = await queue.get()
#         print('{} get a val {}'.format(id, val))
#         await asyncio.sleep(1)
#
# 
# async def producer(queue, id):
#     for i in range(5):
#         val = random.randint(1, 10)
#         await queue.put(val)
#         print('{} put a val {}'.format(id, val))
#         await asyncio.sleep(1)
#
#
# async def main():
#     queue = asyncio.Queue()
#     consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
#     consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))
#
#     producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
#     producer_2 = asyncio.create_task(producer(queue, 'producer_2'))
#
#     await asyncio.sleep(10)
#     consumer_1.cancel()
#     consumer_2.cancel()
#
#     await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)
# asyncio.run(main())
#
# # 这章有个爬虫项目实战先放下了