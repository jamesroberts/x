# Performance tests

All tests run on single computer with Intel 9900K overclocked to 5.00Ghz on all cores.

8 Threads, 200 Connections, 30 seconds using `wrk` benchmark tool

```
wrk -c200 -d30 -t8 http://localhost:5000/get
```

Simple "Hello World" GET Request.

## Basic Flask Server
|Thread Stats|   Avg|      Stdev|     Max|   +/- Stdev|
|------------|------|-----------|--------|------------|
| Latency    |94.52ms   |65.87ms   |1.78s    |98.03%
| Req/Sec    |187.64    |83.34     |383.00   |69.62%

43949 requests in 30.02s, 6.54MB read

**Requests/sec:   1463.76**

Transfer/sec:    223.00KB


## Bjoern single process
|Thread Stats|   Avg|      Stdev|     Max|   +/- Stdev|
|------------|------|-----------|--------|------------|
|Latency    |34.87ms   |48.84ms   |1.24s    |98.99%
|Req/Sec    |811.31    |113.43    |2.27k    |91.74%

192624 requests in 30.02s, 19.47MB read

**Requests/sec:   6415.86**
  
Transfer/sec:    664.14KB


## Multiple Bjoern processes (8 processes)
|Thread Stats|   Avg|      Stdev|     Max|   +/- Stdev|
|------------|------|-----------|--------|------------|
|Latency     |4.55ms    |1.07ms  |13.94ms   |62.85%
|Req/Sec     |5.51k     |256.07  |6.49k     |70.21%
  
1317160 requests in 30.01s, 133.15MB read

**Requests/sec:  43891.98**

Transfer/sec:      4.44MB


## Bjoern (17 processes)
|Thread Stats|   Avg|      Stdev|     Max|   +/- Stdev|
|------------|------|-----------|--------|------------|
|Latency     |3.79ms   | 3.66ms | 63.70ms   |93.13%
|Req/Sec     |7.69k    | 1.12k  | 11.70k    |74.71%
  
1836815 requests in 30.01s, 199.70MB read

**Requests/sec:  61201.32**

Transfer/sec:      6.65MB

## Gunicorn (17 processes)
|Thread Stats|   Avg|      Stdev|     Max|   +/- Stdev|
|------------|------|-----------|--------|------------|
|Latency     |8.44ms   |29.23ms |880.07ms   |98.36%
|Req/Sec     |2.79k    |1.02k   |5.45k      |60.94%
  
662136 requests in 30.07s, 103.56MB read

**Requests/sec:  22020.43**

Transfer/sec:      3.44MB


