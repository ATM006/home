import os
import urllib,urllib.request
import logging


class url_parser(object):

    def is_url(self,url):
        if url.startswith("javascript"):
            return False
        return True

    def get_urls(self):
        url_set = set()
        if not url_parser.is_url(url):
            return url_set

        content = url_parser.get_content()

    def deal_url(self,url, base_url):
        if url.startswith('http') or url.startswith('//'):
            url = url_parser.urlparse(url, scheme='http').geturl()
        else:
            url = url_parser.urljoin(base_url, url)
        return url


    def get_content(self,url, timeout=10):
        try:
            res = urllib.request.urlopen(url,timeout=timeout)
        except urllib.request.URLError as err:
            logging.error("url open error : %s" % url)
            return None

        try:
            content = res.read()
        except Exception as err:
            logging.error("url read err : %s" % url)
            return None

        return url_parser.decode_content(content)


    def decode_content(self,content):
        if encoding == 'GB2312':
            encoding = 'GBK'
        else:
            encoding = 'utf-8'
        try:
            content = content.decode(encoding, 'ignore')
        except Exception as err:
            logging.error("Decode error: %s.", err)
            return None
        return content

    def download(self,url,local_path):
        if not os.path.exists(local_path):
            try:
                os.mkdir(local_path)
            except os.error as err:
                logging.error("mkdir " + local_path + "err :%s", err)

        try:
            path = os.path.join(local_path, url.replace('/', '_').replace(':', '_').replace('?', '_').replace('\\', '_'))
            urllib.urlretrieve(url, path, None)
        except Exception as err:
            logging.error("download url fail. url: %s" % url)
            return False
        return True
