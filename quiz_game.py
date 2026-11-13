class Quiz:
    """퀴즈 1개를 표현하는 클래스."""

    def __init__(self, question, choices, answer):
        # self: 지금 만들어지는 퀴즈 객체 자신
        self.question = question  # 문제 (str)
        self.choices = choices    # 보기 (list)
        self.answer = answer      # 정답 번호, 1부터 시작 (int)

    def show(self):
        """문제와 보기를 화면에 출력한다."""
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False를 반환한다."""
        return user_answer == self.answer


if __name__ == "__main__":
    # 직접 실행했을 때만 동작하는 간단한 확인용 코드
    quiz = Quiz("대한민국의 수도는?", ["부산", "서울", "대구", "인천"], 2)
    quiz.show()
    print(quiz.is_correct(2))
    print(quiz.is_correct(1))
