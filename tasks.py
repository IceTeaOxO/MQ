
from __future__ import absolute_import, unicode_literals
from AppCelery import app


@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    
    result = add.delay(4, 4)
    print(f"Task ID: {result.id}")
    print(result.backend)
    
    # 获取任务结果（可能会阻塞，直到任务完成）
    output = result.get(timeout=10)
    print(f"Task result: {output}")
    
    # 获取任务状态
    status = result.status
    print(f"Task status: {status}")