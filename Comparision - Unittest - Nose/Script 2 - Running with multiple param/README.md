1. Unittest nếu test với nhiều param
- Code "nested" hơn (Sử dụng with)
- Sử dụng thư viện ngoài (Parameterized)
- https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python
2. Với Pytest
- Code "flat" hơn, không nested như unittest
- Support @pytest.mark.parametrize hỗ trợ multiparam
3. Với Nose(Nose2)
- Phải viết thêm 1 hàm phụ để có thể sinh nhiều test với nhiều biến
- Code bị "nested"