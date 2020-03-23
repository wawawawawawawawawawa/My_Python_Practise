# 并发(Concurrency)：某个特定的时刻只允许一个操作发生
# 并行(Parallelism): 多进程(multi-processing)，取决于cpu核数（

# 并发的两种形式：
# threading:操作系统知道每个线程的所有信息，因此他会在适当的时候做线程切换，容易出现资源竞争(race condition)
# asyncio:主程序要想切换任务，必须得到此任务可以被切换的通知，可以避免race condition

# 对比：
# 并发多用于I/O操作比较频繁的场景，比如在网站下载文件
# 并行更多用于CPU heavy的场景

# 单线程方式实现下载任务
import requests
import time
import concurrent.futures
import threading


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    for site in sites:
        download_one(site)

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()
# 展示多单线程版本，会发现绝大多数的时间都浪费在I/O等待上


def download_one1(url):
    resp = requests.get(url)
    print('Read {} from{}'.format(len(resp.content), url))


def download_all1(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executer:
        executer.map(download_one, sites)

# 下面的代码和单线程版相同
# 这里创建一个线程池，总共有5线程可以分配使用.executer.map()，表示对sites中的每一个元素，并发的调用download_one1()
# 这里也可以使用并行的方式
# with concurrent.futures.ProcessPoolExecutor() as executer:
# 函数ProcessPoolExecutor表示创建进程池，，使用多个进程并行的执行程序，这里我们通常省略进程数目的参数，因为系统会自动返回CPU核数


# Futures模块
# Python中的Futures模块位于concurrent.futures和asyncio中，他们都表示带有延迟的操作。Futures会将处于等待状态的操作包裹起来放在
# 队列中，这些操作的状态随时可查询

# Executor类：Futures中的Executor类,当我们执行executor.submit(func)时，他便会安排里面的func()函数执行
# done()方法：表示相对应的操作是否完成，True表示完成，False表示未完成，它是非阻断(non-blocking)函数，会立即返回结果
# add_done_callback(fn):表示Futures完成后，相对应的参数函数fn，会被通知并执行调用
# result():表示档future完成后，返回其对应的结果或异常
# as_completed(fs):针对给定的future迭代器fs，再其完成后，返回完成后的迭代器

# 所以上面的例子也可以这样表示
def download_all2(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()

# 这里首先调用executor.submit()将下载每一个网站的内容都放进future队列to_do,等待执行，然后㐊as_completed()函数，在future完成后，便输出结果






