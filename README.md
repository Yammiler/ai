<h1>AI_HUS_2023_EEI: Nhập môn AI</h1>
<h3>Bài báo cáo của nhóm đi nghiên cứu chuyên sâu về học máy. Học máy được hiểu là quá trình thực hiện một nhiệm vụ T từ kinh nghiệm E, nếu hiệu suất thực hiện công việc T đạt được là P được cải thiện theo kinh nghiệm E theo thời gian. Điều đó giống như bài toán tính ngược so với một ánh xạ y=X.w, từ đó tìm được hàm chuyển đổi w đúng.Từ hàm tuyến tính w xác định cuối cùng, cứ mỗi dữ liệu làm test đưa vào sẽ cho ra một label được dự đoán là tốt/tệ (1/0)</h3>
<h3>Hướng nghiên cứu của bài toán là là sử dụng những comment trên các trang mạng điện tử để có thể kết luận sản phẩm trên có đủ uy tín để có thể sử dụng không.Bài toán mà chúng tôi giải quyết là một bài toán học máy có giảm sát, tử để đưa ra dự đoán xem comment trên là tốt hay tệ.</h3>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/problem.png">
<hr/>
<h2 style="justify:center">1. Thu thập dữ liệu dữ liệu bằng selenium</h2>
<h4>Selenium là một dự án ô mã nguồn mở cho một loạt các công cụ và thư viện nhằm hỗ trợ tự động hóa trình duyệt tạo các bài kiểm tra chức năng trên hầu hết các trình duyệt web hiện đại. Ưu điểm của Selenium là miễn phí, chỉ cần IDE và trình duyệt web, và hỗ trợ nhiều ngôn ngữ lập trình</h4>
<h4>Những thành phần cần thiết để làm việc với Selenium</h4>
<h5>- Import thư viện</h5>
<h5>- Browser to WebDriver</h5>
<h5>- Open website</h5>
<h5>- Find an elment</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/thanhphan_Selenium.png">
<h4>Tiếp theo là các bước xây dựng bộ dữ liệu với BT riêng của chúng tôi:</h4>
<h5>Chuyển tới trang Tiki: bằng driver.get()</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/Tiki_link.png">
<h5>Di chuyển danh sách Item:</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/Take_product.png">
<h5>Lấy Comment: find.element()</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/comment.png">
<h3>Tổng kết tất cả các quá trình trên được mô tả qua video: https://user-images.githubusercontent.com/92799704/226243896-b7ec4d18-8eaa-4099-81fa-f291f846b76c.mp4</h3>
<hr/>
<h2 style="justify:center">2. Sử dụng mô hình Bert để đánh giá chất lượng sản phẩm dựa trên Đánh giá của người dùng</h2>
<h3>2.1 Mô hình Bert và thư viện hỗ trợ Hugging Face</h3>
<h4>Mô hình Transformer: có khả năng đào tạo song song (training parallelization) cho phép đào tạo trên các tập dữ lớn hơn. Mô hình Tranformer gồm 2 thành phần:</h4>
<h5>Encoder: dùng để học vector biểu của câu với mong muốn rằng vector này mang thông tin hoàn hảo của câu đó</h5>
<h5>Decoder: thực hiện chức năng chuyển vector biểu diễn kia thành ngôn ngữ đích</h5>
<h4>Mô hình Bert(Bidirectional Encoder Representation from Transformer): là mô hình học sẵn hay còn gọi là Pre-Train Model. Nên tảng của mô hình BERT là sử dụng Transformer là một mô hình attention (attention mechanism) học mối tương quan giữa các từ (hoặc 1 phần của từ) trong một văn bản. Nhưng mô hình Bert chỉ tập trung vào Encoder</h4>
<h4>Hugging Face là một công ty công nghệ, phát triển các sản phẩm liên quan đến xử lý ngôn ngữ tự nhiên (NLP) và học máy (ML). Phát triển các công cụ và thư viện mã nguồn mở giúp xử lý và phân tích dữ liệu ngôn ngữ tự nhiên. VD như: Tranformer, Tokenizers, Datasets. Trong bài toán này ta sẽ dùng Tranformer và Tokenizers của thư viện này</h4>

<h4>Con data ta đã tự thu thập tại phần 1. Tuy nhiên data tự thu thập được không thể tự đánh giá là tốt hay tệ (1/0). Chúng tôi đã tự đánh label cho chúng. Bài toán này được thử nghiệm với tập dữ liệu bao gồm 1644 comment</h4>
<h3>2.2 Triển khai mô hình</h3>
<h4>Mô hình được triển khai theo các bước sau:</h4>
<h5>- Cài đặt thư viện TRANSFORMER của HUGGING FACE đơn giản</h5>
<h5>- Load MÔ HÌNH BERT và load kho từ TOKENIZER ỨNG VỚI MÔ HÌNH BERT</h5>
<h5>- TOKENIZER toàn bộ dữ liệu biến các đoạn văn bản text thành các con số máy tính có thể hiểu được</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/trienkhai_model.png">
<h5>- MÔ HÌNH BERT</h5>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/BertModel.png">
<hr/>
<h2 style="justify:center">3. Đánh giá và kết luận</h2>
<h4>Hàm predict: Dự đoan kết quả của tập Xtest trả về 1/0</h4>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/predict.png">
<h4>Khi đó ta sẽ đưa ra được mực độ chính xác của mô hình: kết quả 80%</h4>
<img src="https://github.com/paintOfUs/AI_HUS_2023_EEI/blob/main/img/Evaluate.png">
<h3>Đễ xuất của bài toán: Không chỉ dừng lại ở các trang thương mại điện tử, mà cách thức đánh giá trên còn phù hợp với đa ngành nghệ: chất lượng dịch vụ, y tế, giáo dục,...</h3>
<hr>
<h6>Note: Các hình ảnh được sử dụng đều lấy được từ báo cáo chính của nhóm trong thuyết trình học phần nhập môn AI</h4>
