开始学习前，如果代码已经上传到远程仓库：
git pull
学习和练习完成后：
# 1. 查看哪些文件发生了变化
git status

# 2. 检查具体改了什么
```
git diff
```

查看“还没有暂存”的修改。

```
git diff --cached
```

查看“已经暂存、下次commit将会提交”的内容。

按q退出

# 3. 运行代码，确认没有明显错误
python 01_python_basics/variables.py

# 4. 添加本次完成的文件
git add 01_python_basics/variables.py

# 5. 提交
git commit -m "learn(p10): practice Python variables"



commit是将当前在暂存区的文件全部提交，不同用途文件最好分开commit

# 6. 上传Github
git push

## 7.取消当前全部暂存

```
git restore --staged .
```









