import streamlit as st

st.set_page_config(
    page_title="Digital Image Processing",
    page_icon="🏡",
)

st.write("# :orange[Chào mừng đến với môn học xử lý ảnh số!] 🎈")
page_bg_img = '''
    <style>
    .stApp {
        background: url("https://img.freepik.com/free-vector/network-mesh-wire-digital-technology-background_1017-27428.jpg");
        background-size: cover;
    }
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# Định nghĩa CSS cho văn bản màu đen
black_text_css = """
    <style>
    .black-text {
        color: black;
    }
    </style>
"""

# Văn bản Markdown cần đổi màu
markdown_text = """
    Trong khoa học máy tính, xử lý hình ảnh kỹ thuật số là việc sử dụng các thuật toán trên máy tính để thực hiện xử lý hình ảnh trên hình ảnh kỹ thuật số. Là một danh mục con hoặc lĩnh vực xử lý tín hiệu số, xử lý hình ảnh kỹ thuật số có nhiều lợi thế so với xử lý hình ảnh tương tự. Nó cho phép phạm vi thuật toán áp dụng rộng hơn nhiều được áp dụng cho dữ liệu đầu vào và có thể tránh được các vấn đề như sự tích tụ nhiễu và méo tín hiệu trong quá trình xử lý. Vì hình ảnh được xác định theo hai chiều (có thể nhiều hơn) nên việc xử lý hình ảnh kỹ thuật số có thể được mô hình hóa dưới dạng các hệ thống đa chiều.
"""

# Thêm CSS và áp dụng lớp 'black-text' cho văn bản
styled_text = black_text_css + f'<p class="black-text">{markdown_text}</p>'

# Hiển thị văn bản đã đổi màu
st.markdown(styled_text, unsafe_allow_html=True)
