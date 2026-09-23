from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def response(self, message):
        pass


class LocalModel(Model):
    def response(self, message):
        print(f"[本地模型] 回答：{message}")


class CloudModel(Model):
    def response(self, message):
        print(f"[云端模型] 回答：{message}")


def run(model: Model, message):
    model.response(message)


message = input("请输入提示词：")

if message.strip():
    run(LocalModel(), message)
    run(CloudModel(), message)
else:
    print("提示词不能为空")