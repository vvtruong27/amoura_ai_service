# Amoura AI Service

Đây là module backend AI Service cho ứng dụng hẹn hò trực tuyến Amoura. Module này được xây dựng bằng FastAPI và chịu trách nhiệm cung cấp các API cho các tính năng dựa trên Trí tuệ Nhân tạo (AI) của ứng dụng, bao gồm:

*   **AI Hỗ trợ ghép đôi (E2):** Đề xuất đối tượng phù hợp, hiển thị điểm chung.
*   **AI Phân tích hành vi giao tiếp (E3):** Phân tích cảm xúc tin nhắn, gợi ý trò chuyện.
*   **AI Kiểm duyệt nội dung & An toàn người dùng (E4):** Lọc tin nhắn tục tĩu, kiểm tra tên hợp lệ.

Module này được thiết kế để hoạt động độc lập hoặc như một microservice, tương tác với backend chính của ứng dụng Amoura.

## 📂 Cấu trúc thư mục

```text
amoura_ai_service/
├── app/                                # Mã nguồn chính của ứng dụng FastAPI
│   ├── __init__.py
│   ├── api/                            # Các router API
│   │   ├── __init__.py
│   │   └── v1/                         # Version 1 của API
│   │       ├── __init__.py
│   │       ├── endpoints/              # Các file chứa endpoints cụ thể
│   │       │   ├── __init__.py
│   │       │   ├── ai_matching.py
│   │       │   ├── ai_communication.py
│   │       │   └── ai_moderation.py
│   │       └── api.py                  # Tổng hợp các router của v1
│   ├── core/                           # Cấu hình, settings, hằng số
│   │   ├── __init__.py
│   │   └── config.py                   # Cài đặt ứng dụng
│   ├── models/                         # Pydantic models cho request/response
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── matching.py
│   │   ├── communication.py
│   │   └── moderation.py
│   ├── services/                       # Logic nghiệp vụ AI
│   │   ├── __init__.py
│   │   ├── matching_service.py
│   │   ├── communication_analysis_service.py
│   │   └── content_moderation_service.py
│   ├── utils/                          # Các hàm tiện ích
│   │   ├── __init__.py
│   └── main.py                       # File khởi tạo ứng dụng FastAPI
│
├── tests/                              # Thư mục chứa tests
│   ├── __init__.py
│   ├── conftest.py                   # Fixtures cho Pytest
│   └── test_api/                     # Tests cho API endpoints
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── test_ai_matching.py
│           ├── test_ai_communication.py
│           └── test_ai_moderation.py
│
├── .env                              # Biến môi trường (local, bị ignore)
├── .env.example                      # File mẫu cho .env
├── .gitignore                        # Các file/folder bỏ qua khi commit
├── README.md                         # Mô tả, hướng dẫn dự án
└── requirements.txt                  # Danh sách các thư viện Python
```
## 📋 Điều kiện tiên quyết

*   Python 3.12+
*   Pip (Python package installer)
*   Git

## 🚀 Bắt đầu

### 1. Clone Repository

```bash
git clone https://github.com/vvtruong27/amoura_ai_service
cd amoura_ai_service
```
### 2. Tạo và Kích hoạt Môi trường Ảo (Virtual Environment)

Nên sử dụng môi trường ảo để quản lý các gói phụ thuộc của dự án.

**Đối với Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Đối với macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sau khi kích hoạt, bạn sẽ thấy (.venv) ở đầu dòng lệnh.

### 3. Cài đặt Các Gói Phụ thuộc

```bash
pip install -r requirements.txt
```

File requirements.txt chứa danh sách tất cả các thư viện Python cần thiết cho dự án.

### 4. Cấu hình Biến Môi trường

```bash
cp .env.example .env
```

Mở file .env và cập nhật các giá trị cần thiết (ví dụ: API keys cho các dịch vụ AI bên thứ ba nếu có, đường dẫn tới model, ...).

### 5. Chạy Ứng dụng (Development)

```bash
uvicorn app.main:app --reload
```

*   **app.main:app:** Trỏ tới instance app của FastAPI trong file app/main.py.
*   **--reload:** Tự động tải lại server khi có thay đổi trong code (chỉ dùng cho development).

Sau khi server khởi động, bạn có thể truy cập ứng dụng tại: http://localhost:8000

## 📖 Tài liệu API (Swagger UI & ReDoc)

FastAPI tự động tạo tài liệu API tương tác. Sau khi ứng dụng đang chạy, bạn có thể truy cập:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Tại đây, bạn có thể xem tất cả các endpoint, schema request/response và thử nghiệm API trực tiếp.

## 🧪 Chạy Tests

Dự án sử dụng pytest để kiểm thử. Để chạy tất cả các test:

```bash
pytest
```