from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading
import argparse
chrome_options = Options()
chrome_options.add_argument('--headless')
if __name__=='__main__':
    parser = argparse.ArgumentParser(prog='Selenium_cc',description='Using selenium multithreading to access the same website at high speed')
    parser.add_argument('-t', '--thread',type=int,default=15,help="Threads")
    parser.add_argument('-pg', '--pages',type=int,default=30,help="Pages per thread.")
    parser.add_argument('-url','--url',type=str,required=True,help="The url to visit")
    parser.add_argument('--d','--delay',type=int,default=0,help="Delay time before opening the next page (second)")
    args = parser.parse_args()
    thread=args.thread
    url=args.url
    pages=args.pages
    delay=args.delay
    print(f'The program will visit {url} in {thread} thread(s),{pages} per one thread,total {thread*pages} times\nWait 5 seconds....')
    time.sleep(5)
    def worker(num,url):
        print(f'thread:{num}->start.')
        driver = webdriver.Chrome(options=chrome_options)
        for _ in range(pages):
            driver.execute_script("window.open('"+url+"');")
            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[-1])
            driver.close()
            driver.switch_to.window(window_handles[0])
            time.sleep(delay)
        driver.quit()
        print(f'thread:{num}->run end.')
    threads = []
    for i in range (thread):
        threads.append(threading.Thread(target=worker,args=(i,url)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()