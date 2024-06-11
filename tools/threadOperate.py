import threading

class RegisterThread(threading.Thread):
    def __init__(self, task_name):
        super().__init__()
        self.task_name = task_name

    def run(self):
        print(f"开始执行任务：{self.task_name}")
        # 在这里添加你的任务代码
        print(f"任务 {self.task_name} 完成")

if __name__=="__main__":
    # 创建并启动多个线程
    task1 = RegisterThread("任务1")
    task2 = RegisterThread("任务2")

    task1.start()
    task2.start()

    # 等待所有线程完成
    # task1.join()
    # task2.join()

    print("所有任务已完成")
