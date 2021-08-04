# Cách chạy backend
Yêu cầu : Python3, Postgresql
- tạo venv (ở ngoài folder back-end) bằng câu lệnh:
python3 -m venv web-env (macos)
python -m venv web-env (window)
- activate venv
+ Macos/Linux: source web-env/bin/activate
+ Window: web-env\Scripts\activate.bat
- install tất cả các package ở file requirements.txt: pip3 install tênpackage
- chạy backend bằng câu lệnh: 
uvicorn back-end.main:app --reload
