import getopt,sys
import logging,log
import process



def version():
    print("version 0.0.1")


def main():

    log.init_log("./log/spider")
    spider = process.spider_process()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vhc:")
    except getopt.GetoptError as err:
        logging.error("get option error : %s." % err)
        return
    for o, a in opts:
        print("XXX")
        if o == "-v":
            version()
            return
        elif o == "-h":
            print("帮助!")
            return
        elif o == "-c":
            spider.set_config_by_file(a)

        else:
            print("没有"+o+"参数")
            return
    spider.start_work()
    return

if __name__ == "__main__":
    main()
