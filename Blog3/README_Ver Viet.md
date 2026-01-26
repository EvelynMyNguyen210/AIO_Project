Blog này tập trung nói về cách tạo một chatbor và cách deploy chatbot.

# 1. Giới thiệu chatbot và xác định phạm vi hoạt động
## 1.1 Giới thiệu chatbot? 
Ở bài viết này, ta tạo ra một chatbot có thể trả lời các câu hỏi mà người dùng nhập vào. Chatbot sẽ được triển khai trên server, không phải trên máy tính cá nhân, do đó người dùng có thể truy cập thông qua trình duyệt và chatbot luôn sẵn sàng trả lời bất cứ lúc nào. 

📌 Sơ đồ minh hoạ:
User → Web UI → Chatbot Backend → AI Model → Response

### Vai trò của từng khối:
-	User: Người sử dụng chatbot, đặt ra yêu cầu và câu hỏi cho chatbot.
-	Web UI: Giao diện người dùng trên web, giúp người dùng tương tác với chatbot và các chức năng khác thông qua trình duyệt.
-	Chatbot Backend: Trung tâm xử lí logic và luồng hội thoại, câu hỏi của người dùng sẽ được xử lí để tạo ra câu trả lời.
-	AI Model: Cung cấp khả năng hiểu ngôn ngữ của người dùng, từ đó sinh ra câu trả lời.
-	Response: Phản hồi từ chatbot sẽ được sinh ra và hiển thị trên trình duyệt.

## 1.2 Xác định các chức năng và phạm vi của chatbot:
Vì blog này tập trung vào việc xây dựng một chatbot đơn giản và triển khai trên web, do đó các yêu cầu về chức năng và phạm vi sẽ được giới hạn để phù hợp với công suất phản hồi:

Only accept text input:
Giới hạn đầu vào của chatbot là câu hỏi dạng chuỗi để tiết kiệm thời gian phản hồi. Phạm vi câu hỏi không giới hạn.

Customizable system prompt / personality: (Phần này có thêm ảnh đính kèm?)
Đây là các tính năng được tích hợp trên Web UI, người dùng có thể tùy chỉnh các thông số để phản hồi của chatbot đa dạng hơn: 
-	Multilingual support: Người dùng có thể input câu hỏi dạng song ngữ (cụ thể là tiếng Anh hoặc tiếng Việt)
-	Basic safety / content filtering: Lọc các từ khóa, từ ngữ nhạy cảm. 
-	Temperature / creativity slider: Điều chỉnh mức độ thông minh của chatbot. Người dùng có thể tinh chỉnh bằng cách kéo thanh trượt (Slide bar).
-	Response length control: Giới hạn độ dài của phản hồi.
-	Clear chat / restart button: Xóa lịch sử đoạn hội thoại.

# 2. Triển khai code chatbot
## 2.1 Choose tech stack
Ở blog này ta sẽ lựa chọn các công cụ chính sau để làm chatbot:

Ngôn ngữ lập trình: Python
-	Python được chọn làm ngôn ngữ chính để thiết kế chatbot dựa trên ưu điểm về cú pháp đơn giản, lượng thư viện lớn trong quá trình làm chatbot.

Model framework: Hugging Face
-	Hugging Face là nền tảng mã nguồn mở về AI, bao gồm các tập dữ liệu, mô hình AI lớn. Việc sử dụng Hugging Face sẽ giúp chúng ta dễ dàng tìm kiếm và sử dụng các mô hình AI phù hợp.

Model deployment: Hugging Face Space
-	Huggin Face Space hỗ trợ triển khai model đơn giản, phù hợp với các dự án nhỏ.

Web deployment: Streamlit
-	Streamlit được chọn để tạo Web UI cho chatbot nhờ vào khả năng tương thích với Python cao, dễ phát triển, phù hợp với dự án chatbot nhỏ và không yêu cầu kiến thức lớn về lập trình frontend.



# 3.1. Recommended deployment platforms
Khi triển khai một AI chatbot, việc chọn nền tảng deploy phù hợp ảnh hưởng trực tiếp đến độ dễ triển khai, chi phí và trải nghiệm demo. Hiện nay có nhiều lựa chọn khác nhau, mỗi nền tảng phù hợp với một mục tiêu riêng.
Bảng dưới đây so sánh một số nền tảng phổ biến để deploy chatbot, từ demo học tập cho đến ứng dụng thực tế.
| Platform                | Hugging Face Spaces        | Streamlit Cloud    | Render           | Cloudflare Workers       | Vercel                   |
| ----------------------- | -------------------------- | ------------------ | ---------------- | ------------------------ | ------------------------ |
| **Mức độ dễ dùng**      | ⭐⭐⭐⭐⭐ Rất dễ               | ⭐⭐⭐⭐ Dễ            | ⭐⭐⭐ Trung bình   | ⭐⭐ Khó                   | ⭐⭐⭐ Trung bình           |
| **Hỗ trợ UI chatbot**   | Có sẵn (Gradio, Streamlit) | Có sẵn (Streamlit) | Không có sẵn     | Không có                 | Không có                 |
| **Triển khai model AI** | Rất phù hợp cho ML/LLM     | Phù hợp demo nhẹ   | Phải tự cấu hình | Không phù hợp model nặng | Không phù hợp model nặng |
| **Thiết lập ban đầu**   | Tạo Space, upload code     | Kết nối GitHub     | Cấu hình service | Viết worker script       | Cấu hình project         |
| **Chi phí**             | Miễn phí cho demo          | Miễn phí giới hạn  | Có free tier     | Miễn phí theo request    | Miễn phí giới hạn        |
| **Hiệu năng**           | Trung bình                 | Trung bình         | Tốt              | Rất tốt (API)            | Rất tốt (frontend/API)   |
| **Mục đích phù hợp**    | Demo, học tập, showcase AI | Demo nhanh         | App backend nhỏ  | API backend              | Web app + API            |
| **Khả năng chia sẻ**    | Link public ngay           | Link public        | Link public      | Link public              | Link public              |

**Nhận xét nhanh từng nền tảng**
**Hugging Face Spaces**
Là lựa chọn phù hợp nhất cho demo chatbot AI vì hỗ trợ trực tiếp các mô hình học máy và có sẵn UI chat. Phù hợp cho sinh viên, blog kỹ thuật và showcase project.

**Streamlit Cloud**
Phù hợp khi chatbot được xây dựng bằng Streamlit. Dễ dùng nhưng khả năng chạy mô hình nặng và tùy chỉnh hệ thống thấp hơn Hugging Face Spaces.

**Render**
Phù hợp để deploy backend chatbot dạng API. Tuy nhiên, cần tự xây dựng giao diện và cấu hình nhiều hơn, không lý tưởng cho demo nhanh.

**Cloudflare Workers**
Rất mạnh cho API và hệ thống production nhẹ, nhưng không phù hợp để chạy trực tiếp mô hình AI lớn. Thường dùng khi chatbot gọi AI API bên ngoài.

**Vercel**
Phù hợp cho frontend và API serverless. Tuy nhiên, việc deploy chatbot AI thường cần kết hợp với dịch vụ AI khác, không tối ưu cho demo LLM chạy trực tiếp.

**Vì sao blog này chọn Hugging Face Spaces?**
Với mục tiêu deploy chatbot miễn phí, dễ triển khai và có demo trực quan, Hugging Face Spaces đáp ứng tốt nhất các yêu cầu:
- Không cần thiết lập DevOps phức tạp
- Hỗ trợ sẵn UI chat bằng Gradio
- Có thể chạy trực tiếp mô hình AI
- Phù hợp để chia sẻ link demo trong blog và GitHub README
  
Do đó, Hugging Face Spaces được chọn làm nền tảng deploy cho chatbot trong bài viết này.

# 4. Những giới hạn của bản deploy miễn phí
Mặc dù việc deploy chatbot bằng Hugging Face Spaces mang lại nhiều lợi ích cho demo và học tập, phiên bản miễn phí vẫn tồn tại một số giới hạn nhất định.

Trước hết, **tốc độ phản hồi** của chatbot có thể chưa cao, đặc biệt khi mô hình cần tải lại hoặc khi có nhiều người truy cập cùng lúc. Điều này là bình thường với các nền tảng miễn phí, nơi tài nguyên CPU và bộ nhớ bị giới hạn.

Thứ hai, giới hạn tài nguyên là yếu tố cần cân nhắc. Các mô hình lớn hoặc yêu cầu GPU mạnh có thể không chạy ổn định trong môi trường miễn phí. Vì vậy, demo thường cần sử dụng các mô hình nhẹ hoặc giới hạn độ dài câu trả lời để đảm bảo chatbot không bị treo.

Cuối cùng, bản deploy miễn phí không phù hợp cho tải lớn hoặc sử dụng thực tế quy mô cao. Đây không phải là môi trường dành cho sản phẩm thương mại, mà chủ yếu phục vụ mục đích thử nghiệm và trình diễn.

Tuy nhiên, với phạm vi của blog này, các giới hạn trên là hoàn toàn chấp nhận được. Phiên bản deploy miễn phí vẫn đủ tốt cho:
- Demo chatbot hoạt động thực tế
- Học tập và nghiên cứu
- Trình bày ý tưởng và kiến trúc hệ thống

*Deploy là bước giúp chatbot chuyển từ một chương trình chạy local thành một sản phẩm có thể sử dụng ngay trên trình duyệt. Thông qua việc deploy chatbot bằng Gradio và Hugging Face Spaces, chúng ta có thể tạo ra một bản demo hoàn chỉnh mà không cần đầu tư hạ tầng phức tạp hay chi phí cao.
Quan trọng hơn, quá trình deploy giúp người phát triển hiểu rõ hơn về vòng đời của một ứng dụng AI thực tế: từ thiết kế phạm vi, triển khai code, cho đến đưa sản phẩm lên môi trường cloud. Khi tư duy triển khai đã rõ ràng, việc mở rộng chatbot trong tương lai—chẳng hạn như cải thiện giao diện, tối ưu hiệu năng hoặc tích hợp dữ liệu riêng—sẽ trở nên dễ dàng hơn rất nhiều.*

*Không cần hệ thống phức tạp hay ngân sách lớn, bất kỳ ai cũng có thể deploy một AI chatbot online nếu đi đúng hướng và chọn đúng công cụ.*
