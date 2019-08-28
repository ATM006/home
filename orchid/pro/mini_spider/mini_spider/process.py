import logging
import queue
import spider_thread
import configparser

class spider_process(object):

    def __init__(self):
        self.queue = queue.Queue()
        self.url_list_file = "urls"
        self.output_directory = "output"
        self.max_depth = 1
        self.crawl_interval = 1
        self.crawl_timeout = 10
        self.target_url = ".*\.(gif|png|jpg|bmp)$"
        self.thread_count = 1
        self.total_set = set()
        return

    def __str__(self):
        return self.__getattribute__('url_list_file')

    def set_config(self, url_list_file, output_directory, max_depth, crawl_interval,crawl_timeout, target_url, thread_count):

        self.url_list_file = url_list_file
        self.output_directory = output_directory
        self.max_depth = max_depth
        self.crawl_interval = crawl_interval
        self.crawl_timeout = crawl_timeout
        self.target_url = target_url
        self.thread_count = thread_count

        self.set_up()

        if not self.set_url_queue_by_file():
            return False

        return True

    def set_up(self):
        self.url_list_file = os.path.join(os.getcwd(), self.url_list_file)
        self.output_directory = self.set_full_dir(self.output_directory)


    def set_config_by_file(self, file):

        if len(file) < 1:
            logging.error("the path of file error.file: %s." % file)
            return False
        cf =configparser.ConfigParser()
        try:
            cf.read(file)
        except Exception as err:
            logging.error("get conf file error: %s" % err)
            return False
        try:
            set_result = self.set_config(cf.get("spider", "url_list_file"),
                                         cf.get("spider", "output_directory"),
                 cf.getint("spider", "max_depth"), cf.getint("spider", "crawl_interval"),
                 cf.getint("spider", "crawl_timeout"), cf.get("spider", "target_url"),
                 cf.getint("spider", "thread_count"))
        except Exception as err:
            logging.error("conf file format error: %s" % err)
            return False
        return set_result

    def set_url_queue_by_file(self):

        try:
            with open(self.url_list_file) as urls:
                for url in urls:
                    if len(url.strip(' ')) < 1:
                        continue
                    self.queue.put(UrlLeaf(url=url, level=0))
        except Exception as err:
            logging.error("get url from file error: %s ." % err)
            return False
        return True


    def set_full_dir(self, path):

        output_dir = os.path.join(os.getcwd(), path)
        if not os.path.exists(output_dir):
            try:
                os.mkdir(output_dir)
            except os.error as err:
                logging.error("mkdir output dir error: %s. " % err)
        return str(output_dir)

    def start_work(self):

        thread_list = []

        for i in range(self.thread_count):
            thread = spider_thread.spider_thread(self.queue, self.crawl_timeout, self.crawl_interval,
                                                self.output_directory, self.max_depth,
                                                self.target_url, self.total_set)
            thread_list.append(thread)
            logging.info("thread %d start..." % i)
            thread.start()
        for thread in thread_list:
            thread.join()
            logging.info("a thread done")
        self.queue.join()
        logging.info("queue is all done")
        return