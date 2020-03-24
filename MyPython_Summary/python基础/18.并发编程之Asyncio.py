# # 多线程的局限性：
# # 1.多线程的运行过程容易被打断，因此可能出现race condition的情况
# # 2.线程切换本身存在一定的损耗，线程数不能无限增加，因此如果I/O操作非常heavy，多线程可能满足不了高效率，高质量需求
#
# # Sync VS Async(同步vs异步)
# # Sync:操作一个接一个的执行，写一个操作必须等上一个操作完成后才能执行
# # Async：指不同操作间可以相互交替执行，如果其中的某个操作被block了，程序并不会等待，而是会找出可执行的操作继续执行
#
# # Asyncio的工作原理：和其他Python程序一样，是单线程的，但是可以进行多个不同任务(task)，这里的任务，就是特殊的future对象
# # 这些不同的任务，被一个叫event loop的对象控制
# # 对于Asyncio来说，它的任务在运行时不会被外部的一些因素打断，因此Asyncio内的操作不会出现race condition的情况，所以不用担心线程安全问题
#
#
# # Asyncio版本的下载网站内容
# import asyncio
# import aiohttp
# import time
#
#
# async def download_one(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             print('Read {} from {}'.format(resp.content_length, url))
#
# async def download_all(sites):
#     tasks = [asyncio.create_task(download_one(site)) for site in sites]
#     await asyncio.gather(*tasks)
#
# def main():
#     sites = [
#         'https://en.wikipedia.org/wiki/Portal:Arts',
#         'https://en.wikipedia.org/wiki/Portal:History',
#         'https://en.wikipedia.org/wiki/Portal:Society',
#         'https://en.wikipedia.org/wiki/Portal:Biography',
#         'https://en.wikipedia.org/wiki/Portal:Mathematics',
#         'https://en.wikipedia.org/wiki/Portal:Technology',
#         'https://en.wikipedia.org/wiki/Portal:Geography',
#         'https://en.wikipedia.org/wiki/Portal:Science',
#         'https://en.wikipedia.org/wiki/Computer_science',
#         'https://en.wikipedia.org/wiki/Python_(programming_language)',
#         'https://en.wikipedia.org/wiki/Java_(programming_language)',
#         'https://en.wikipedia.org/wiki/PHP',
#         'https://en.wikipedia.org/wiki/Node.js',
#         'https://en.wikipedia.org/wiki/The_C_Programming_Language',
#         'https://en.wikipedia.org/wiki/Go_(programming_language)'
#     ]
#     start_time = time.perf_counter()
#     asyncio.run(download_all(sites))
#     end_time = time.perf_counter()
#     print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
#
# if __name__ == '__main__':
#     main()
#
# # 这里的Async和await关键字是Asyncio的最新写法，表示这个语句/函数时无阻塞(no-block)的
#
# # 多线程和Asyncio的选择：
# # 1.如果是 I/O bound，并且 I/O 操作很慢，需要很多任务 / 线程协同实现，那么使用 Asyncio 更合适。
# # 2.如果是 I/O bound，但是 I/O 操作很快，只需要有限数量的任务 / 线程，那么使用多线程就可以了。
# # 3.如果是 CPU bound，则需要使用多进程来提高程序运行效率
#
# # Asyncio中的任务，在运行的情况下不会被打断，在I/O操作heavy 的场景下，Asyncio比多线程的运行效率更高，因为Asyncio内部任务切换的损耗
# # 远比线程切换的损耗小
#
#
