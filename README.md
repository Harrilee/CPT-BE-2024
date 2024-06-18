## Setup

- Create a `.env` file in the root of your project directory and add the following lines, replacing the placeholder values with your actual configuration details:

```bash
SECRET_KEY=your-256-bit-secret
DB_NAME=cpt
DB_USER=<database_username>
DB_PASSWORD=<database_password>
DB_HOST=<database_host>
DB_PORT=3306 || <database_port>
CORS_ALLOWED_ORIGINS=<comma-separated_origions>
```

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## 推送消息及用户认证方式

### 推送普通提醒消息（不含链接）
- Blued站内信：Blued uid
- 阿里云短信推送：通过screening survey收集的手机号
- 微信：通过screening survey收集的微信号，仅限于前两种方式无法联系到的参与者

### 推送重要消息（网站链接、JD购物卡）
- Blued站内信：所有链接需要加入Blued uid

### 接收来自用户的消息
- 微信：需用户提供手机号以定位用户数据

### 身份认证与数据集成
- 阿里云短信验证：RA下载数据后，手动在网站中建立加密手机号白名单，用户使用手机短信验证码登录

### 用户进度追踪
- 后端：使用加密手机号

### 备注
- 绑定Blued uid码和手机号
- 所有问卷星问卷需接入网站
- 问卷星能否自动筛查eligible的参与者待考察
