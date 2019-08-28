import logging
import re
import time
import threading,url_parser,url_leaf


class spider_thread(threading.Thread):

    def __init__(self, queue, timeout, interval, file_path, max_depth, target_url, total_set):
        threading.Thread.__init__(self)
        self.queue = queue
        self.timeout = timeout
        self.interval = interval
        self.file_path = file_path
        self.max_depth = max_depth
        self.target_url = target_url
        self.total_set = total_set
        self.lock = threading.Lock()

    def need_download(self, url):

        if not url_parser.is_url(url):
            return False
        try:
            pattern = re.compile(self.target_url)
        except Exception as err:
            logging.error("the target url is not re..compile fail: %s" % self.target_url)
            return False
        if len(url.strip(' ')) < 1 or not pattern.match(url.strip(' ')):
            return False
        if url in self.total_set:
            return False
        return True

    def run(self):

        while True:
            try:
                url_leaf = self.queue.get(block=True, timeout=self.timeout)
            except Exception as err:
                logging.info("this thread can not get a task. job done.")
                break

            self.queue.task_done()
            time.sleep(self.interval)

            if self.need_download(url_leaf.url):
                url_parser.url_parser.download(self.file_path, url_leaf.url)
            self.lock.acquire()
            self.total_set.add(url_leaf.url)
            self.lock.release()

            sub_urls = url_parser.url_parser.get_urls(url_leaf.url)
            new_level = url_leaf.level + 1
            if new_level > self.max_depth:
                continue

            for url in sub_urls:
                url_leaf_temp = url_leaf.url_leaf(url,new_level)
                self.queue.put(url_leaf_temp)



