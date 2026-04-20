# PythonAnywhere 部署指南 - 详细步骤

PythonAnywhere 是最友好的 Python 应用部署平台，完全免费，不需要信用卡。本指南提供完整的部署步骤。

## 前置要求

- GitHub 账户（已有）
- PythonAnywhere 免费账户
- 项目已推送到 GitHub

---

## 🚀 第一步：注册 PythonAnywhere 账户

1. **访问官网**
   - 打开 https://www.pythonanywhere.com

2. **注册账户**
   - 点击 "Sign up"
   - 选择 "Beginner" 免费计划
   - 输入用户名（会成为部署 URL 的一部分，如 `username.pythonanywhere.com`）
   - 输入邮箱和密码
   - 点击 "Create a PythonAnywhere account"

3. **验证邮箱**
   - 收到验证邮件，点击验证链接

✅ **现在你有了 PythonAnywhere 账户**

---

## 🛠️ 第二步：克隆项目仓库到 PythonAnywhere

1. **打开 Web 控制台**
   - 登录 PythonAnywhere Dashboard
   - 点击顶部 "Consoles" → "Start a new console" → "Bash"
   - 等待 Bash console 加载（通常 5-10 秒）

2. **克隆 GitHub 仓库**
   ```bash
   git clone https://github.com/innovationty/interview-tracker-api.git
   ```

   输出示例：
   ```
   Cloning into 'interview-tracker-api'...
   remote: Enumerating objects: 50, done.
   ...
   ```

3. **进入项目目录**
   ```bash
   cd interview-tracker-api
   ```

4. **查看项目文件**
   ```bash
   ls -la
   ```

   确保看到：
   ```
   README.md
   requirements.txt
   app/
   data/
   scripts/
   ...
   ```

✅ **现在项目已克隆到 PythonAnywhere**

---

## 📦 第三步：创建虚拟环境

1. **创建虚拟环境**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.12 interview-tracker
   ```

   输出示例：
   ```
   Running virtualenv with interpreter /usr/bin/python3.12
   Using real prefix '/usr'
   New python executable in /home/yourname/.virtualenvs/interview-tracker/bin/python
   ...
   ```

2. **验证虚拟环境激活**
   ```bash
   which python
   ```

   应该返回：
   ```
   /home/yourname/.virtualenvs/interview-tracker/bin/python
   ```

✅ **虚拟环境已创建**

---

## 📥 第四步：安装依赖

1. **安装 requirements.txt**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   输出示例：
   ```
   Collecting fastapi==0.115.2
   Downloading fastapi-0.115.2-py3-none-any.whl (92 kB)
   Installing collected packages: fastapi, uvicorn, ...
   Successfully installed fastapi-0.115.2 uvicorn-0.30.6 ...
   ```

2. **验证安装**
   ```bash
   pip list | grep fastapi
   ```

   应该显示：
   ```
   fastapi              0.115.2
   ```

✅ **所有依赖已安装**

---

## 🌐 第五步：配置 Web App

### 5.1 创建 Web App

1. **打开 Web Apps 配置**
   - 点击顶部 "Web" 菜单
   - 点击 "Add a new web app"

2. **选择域名**
   - 选择 "yourname.pythonanywhere.com"（可用的域名自动显示）
   - 点击 "Next"

3. **选择 Web 框架**
   - 选择 "Manual configuration"
   - 点击 "Next"

4. **选择 Python 版本**
   - 选择 "Python 3.12"
   - 点击 "Next"

✅ **Web App 框架已创建**

### 5.2 配置 WSGI 文件

1. **编辑 WSGI 配置**
   - 回到 Web Apps 页面
   - 在 "Code" 部分，点击 "WSGI configuration file"
   - 这会打开一个文件编辑器

2. **清空现有内容，粘贴以下代码**

   ```python
   import sys
   import os

   # 添加项目路径
   project_home = '/home/yourname/interview-tracker-api'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # 激活虚拟环境
   activate_this = os.path.expanduser('/home/yourname/.virtualenvs/interview-tracker/bin/activate_this.py')
   exec(open(activate_this).read(), {'__file__': activate_this})

   # 导入 FastAPI 应用
   from app.main import app

   # WSGI 应用
   application = app
   ```

   **⚠️ 重要：替换 `yourname` 为你的 PythonAnywhere 用户名**

3. **保存文件**
   - Ctrl + S（或 Cmd + S）
   - 点击 "Save"

✅ **WSGI 配置已保存**

### 5.3 配置虚拟环境路径

1. **设置虚拟环境**
   - 回到 Web Apps 页面
   - 在 "Virtualenv" 部分，输入：
     ```
     /home/yourname/.virtualenvs/interview-tracker
     ```
   - 点击 "Enter"

✅ **虚拟环境已绑定**

---

## 🔧 第六步：配置 Web App 设置

1. **设置源代码目录**
   - 在 Web Apps 页面
   - "Source code" 字段应显示：`/home/yourname/interview-tracker-api`
   - 如果需要修改，点击编辑

2. **配置静态文件（可选）**
   - 本项目不需要静态文件配置
   - FastAPI 的 Swagger UI 由应用自动提供

✅ **Web App 配置完成**

---

## ⚡ 第七步：重启 Web App

1. **重启应用**
   - 在 Web Apps 页面
   - 点击页面顶部的 "Reload" 按钮（绿色按钮）
   - 等待 1-2 秒，显示 "Last reload" 时间戳

   ```
   ✓ Reloaded at 2026-04-20 12:34:56
   ```

✅ **应用已启动**

---

## ✅ 第八步：验证部署

1. **访问应用**
   - 在浏览器中打开：`https://yourname.pythonanywhere.com`
   - 应该看到：
     ```json
     {
       "message": "Welcome to Interview Tracker API",
       "version": "1.0"
     }
     ```

2. **访问 API 文档**
   - 打开：`https://yourname.pythonanywhere.com/docs`
   - 应该看到 Swagger UI 界面，列出所有 API 端点

3. **测试 API 端点**

   **查看所有应用记录：**
   ```
   GET https://yourname.pythonanywhere.com/applications
   ```

   **查看 API 文档：**
   ```
   GET https://yourname.pythonanywhere.com/docs
   ```

   **查看摘要统计：**
   ```
   GET https://yourname.pythonanywhere.com/applications/summary
   ```

✅ **部署成功！**

---

## 📊 常见问题与解决

### Q1: 访问应用返回 "ModuleNotFoundError"

**症状：**
```
ModuleNotFoundError: No module named 'app'
```

**解决方案：**
1. 返回 Web Apps 页面
2. 检查 WSGI 文件中的路径是否正确（替换 `yourname`）
3. 确保虚拟环境路径也正确
4. 点击 "Reload"

### Q2: 数据库文件找不到

**症状：**
```
OperationalError: unable to open database file
```

**解决方案：**
```bash
# 在 Bash console 中，导入数据
cd ~/interview-tracker-api
source ~/.virtualenvs/interview-tracker/bin/activate
python scripts/import_applications_csv.py
```

### Q3: 依赖包安装失败

**症状：**
```
ERROR: Could not find a version that satisfies the requirement
```

**解决方案：**
```bash
# 确保虚拟环境激活
workon interview-tracker

# 升级 pip
pip install --upgrade pip

# 重新安装依赖
pip install -r requirements.txt
```

### Q4: 导入数据后看不到数据

**症状：** 应用运行但返回空列表

**解决方案：**
```bash
# 检查数据库是否存在
ls -la ~/interview-tracker-api/job_tracker.db

# 如果不存在，导入数据
cd ~/interview-tracker-api
python scripts/import_applications_csv.py

# 验证数据已导入
python -c "
import sqlite3
conn = sqlite3.connect('job_tracker.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM applications')
count = cursor.fetchone()[0]
print(f'Database has {count} records')
"

# 返回 Web Apps 并 Reload
```

### Q5: PythonAnywhere 超时（502 Bad Gateway）

**症状：** 访问应用返回 502 错误

**解决方案：**
1. 回到 Web Apps 页面
2. 检查 "Error log" 和 "Server log"
3. 最常见原因：WSGI 文件有语法错误
4. 修复错误后点击 "Reload"

---

## 📱 应用 URL

部署完成后，你的应用可在以下地址访问：

| 资源 | URL |
|------|-----|
| **应用主页** | `https://yourname.pythonanywhere.com` |
| **API 文档** | `https://yourname.pythonanywhere.com/docs` |
| **ReDoc 文档** | `https://yourname.pythonanywhere.com/redoc` |
| **所有应用** | `https://yourname.pythonanywhere.com/applications` |
| **应用摘要** | `https://yourname.pythonanywhere.com/applications/summary` |

---

## 🔄 更新应用（Git 部署）

每次需要更新应用时：

1. **在本地推送更新到 GitHub**
   ```bash
   git add .
   git commit -m "your message"
   git push origin main
   ```

2. **在 PythonAnywhere Bash 中拉取更新**
   ```bash
   cd ~/interview-tracker-api
   git pull origin main
   ```

3. **如果修改了依赖**
   ```bash
   workon interview-tracker
   pip install -r requirements.txt
   ```

4. **重启应用**
   - Web Apps 页面 → 点击 "Reload"

✅ **应用已更新**

---

## 📥 导入数据

### 第一次部署时导入数据

```bash
# 激活虚拟环境
workon interview-tracker

# 进入项目目录
cd ~/interview-tracker-api

# 运行导入脚本
python scripts/import_applications_csv.py
```

**预期输出：**
```
Imported 49 records from data\job_applications_seed.csv
```

### 验证数据已导入

```bash
# 打开 Bash console
python -c "
import sqlite3
conn = sqlite3.connect('job_tracker.db')
cursor = conn.cursor()

# 检查总数
cursor.execute('SELECT COUNT(*) FROM applications')
print(f'Total records: {cursor.fetchone()[0]}')

# 检查分布
cursor.execute('SELECT status, COUNT(*) FROM applications GROUP BY status')
print('\nStatus breakdown:')
for status, count in cursor.fetchall():
    print(f'  {status}: {count}')
"
```

---

## 🎯 实际示例

假设你的 PythonAnywhere 用户名是 `zhangsan`：

### WSGI 文件内容（替换后）：

```python
import sys
import os

# 添加项目路径
project_home = '/home/zhangsan/interview-tracker-api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境
activate_this = os.path.expanduser('/home/zhangsan/.virtualenvs/interview-tracker/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

# 导入 FastAPI 应用
from app.main import app

# WSGI 应用
application = app
```

### 应用 URL：
- 主页：`https://zhangsan.pythonanywhere.com`
- API 文档：`https://zhangsan.pythonanywhere.com/docs`

---

## 🔒 安全建议

1. **启用 HTTPS**
   - PythonAnywhere 默认启用 HTTPS（所有请求自动重定向）
   - 无需额外配置

2. **隐藏数据库文件**
   - 数据库文件 `job_tracker.db` 已包含在 `.gitignore`
   - 不会被推送到 GitHub

3. **定期备份**
   - 定期下载 `job_tracker.db` 备份
   - 在 Files 标签下载数据库文件

---

## 💡 性能优化建议

1. **使用 PostgreSQL**（PythonAnywhere 支持）
   - 比 SQLite 更稳定
   - 需要付费或学生账户升级

2. **添加缓存**
   - 将 API 响应缓存 5-10 分钟
   - 减少数据库查询

3. **异步操作**
   - FastAPI 已支持异步，无需修改

---

## 📞 获取帮助

- **PythonAnywhere 文档**：https://help.pythonanywhere.com
- **PythonAnywhere 论坛**：https://www.pythonanywhere.com/forums
- **FastAPI 文档**：https://fastapi.tiangolo.com

---

## ✨ 完成清单

- [ ] 注册 PythonAnywhere 账户
- [ ] 克隆项目仓库
- [ ] 创建虚拟环境
- [ ] 安装依赖包
- [ ] 创建 Web App
- [ ] 配置 WSGI 文件（替换用户名）
- [ ] 设置虚拟环境路径
- [ ] 重启 Web App
- [ ] 验证应用可访问
- [ ] 导入数据（可选，如果需要）
- [ ] 在浏览器中打开 /docs 查看 API

完成以上步骤后，应用即可在线访问！🚀
