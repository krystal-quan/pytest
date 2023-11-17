1. Pytest: 
- Định nghĩa fixture thông qua @pytest.fixture -> dễ sử dụng, linh hoạt
- Pytest tự động quản lý và chạy các fixture. Các fixture có thể được sử dụng trong cùng một test hoặc chia sẻ giữa nhiều test.
- Scope có tính mở rộng: Pytest cho phép bạn đặt fixture ở cấp mô-đun, bài kiểm tra, hoặc dự án

2. Unittest
- Định nghĩa fixture được tích hợp trong unittest.TestCase, được đặt trong các phương thức setup và teardown của lớp TestCase
- Tính không linh hoạt: cần sử dụng các phương thức setup và teardown để tự động quản lý việc chuẩn bị và giải phóng tài nguyên.
- Scope hạn chế: Các fixture thường được đặt ở cấp lớp TestCase và không phải ở cấp mô-đun hoặc dự án

3. Unittest
- Không có định nghĩa fixture, fixture là 1 hàm, về cơ bản bất kỳ hàm nào cũng có thể là fixture
- Gán fixture cho test bằng @with_setup và @with_teardown
- Scope hạn chế: Không có phương thức gắn scope