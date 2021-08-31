import os
from typing import Any
import datetime
from pytz import timezone

class TextLogger():
    def __init__(self, saveDir) -> None:
        self.saveDir = os.path.join(saveDir, 'log.txt')
    
    def __call__(self, msg: str) -> Any:
        now = datetime.datetime.now(timezone('Asia/Seoul'))
        with open(self.saveDir, mode='a+', encoding='utf-8') as f:
            print(msg)
            f.writelines(f'\n[{now}]\t{msg}')