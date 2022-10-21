# 安装 pike
```
python -m pip install pika
```
# Hello World
```
➜  start git:(main) ✗ python 02receive.py
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
```
```
➜  start git:(main) ✗ python 01send.py 
 [x] Sent 'Hello World!'
➜  start git:(main) ✗ python 01send.py
 [x] Sent 'Hello World!'
```
# Work Queues
```
➜  start git:(main) ✗ python 03new_task.py "cjx"    
/data/git-projects/programing-language/Python-RabbitMQ
 [x] Sent 'cjx'
➜  start git:(main) ✗ python 03new_task.py "cjx ccx"
/data/git-projects/programing-language/Python-RabbitMQ
 [x] Sent 'cjx ccx'
➜  start git:(main) ✗ python 03new_task.py "cxy"    
/data/git-projects/programing-language/Python-RabbitMQ
 [x] Sent 'cxy'
```
```
➜  start git:(main) ✗ python 04worker.py
/data/git-projects/programing-language/Python-RabbitMQ
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'cjx'
 [x] Done
 [x] Received b'cjx ccx'
 [x] Done
 [x] Received b'cxy'
 [x] Done
```
