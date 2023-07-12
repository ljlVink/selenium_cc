# selenium_cc

Using selenium(ChromeDriver) multithreading to access the same website at high speed

usage

```sh
python main.py -h
```

```sh
python main.py -t 15 -pg 15 -url http://www.bing.com/ -d 1
```

`-t` means Thread.

`-pg` means pages per thread.

`-url` means the url we`ll visit.

`-d` Delay time before opening the next page (second)

