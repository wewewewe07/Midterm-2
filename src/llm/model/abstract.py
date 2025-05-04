class LLM:
    # Biến lưu số lượng token đầu vào và đầu ra của mô hình
    input_token: int = 0
    output_token: int = 0

    def __call__(self, message, **kwargs) -> str:
        raise NotImplementedError()

    def stream(self, message, **kwargs):
        """
        Xử lý luồng dữ liệu (streaming) từ mô hình AI.
        Thích hợp cho các ứng dụng như chatbot cần phản hồi theo thời gian thực.
        """
        raise NotImplementedError()

    def batch_call(self, messages, **kwargs):
        """
        Xử lý nhiều yêu cầu cùng một lúc (batch processing).
        Giúp tối ưu hóa hiệu suất khi cần tạo nhiều phản hồi đồng thời.
        """
        raise NotImplementedError()

    def retrieve(self):
        """
        Phương thức dùng để truy xuất dữ liệu hoặc trạng thái của mô hình.
        Tùy thuộc vào mô hình cụ thể, có thể dùng để lấy thông tin về token, logs, v.v.
        """
        raise NotImplementedError()

    def reset_token(self):
        """
        Đặt lại số lượng token đầu vào và đầu ra về 0.
        Thích hợp để theo dõi việc sử dụng token theo từng phiên hoặc yêu cầu.
        """
        self.input_token = 0
        self.output_token = 0

    def usage(self):
        """
        Trả về số lượng token đã sử dụng trong quá trình xử lý.
        :return: Một dictionary chứa số lượng token đầu vào và đầu ra.
        """
        return {
            'input_token': self.input_token,
            'output_token': self.output_token
        }