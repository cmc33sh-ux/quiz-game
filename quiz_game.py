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


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        # 기본 퀴즈 5개 (주제: 상식)
        self.quizzes = [
            Quiz("대한민국의 수도는?", ["부산", "서울", "대구", "인천"], 2),
            Quiz("태양계에서 가장 큰 행성은?", ["지구", "화성", "목성", "토성"], 3),
            Quiz("물의 화학식은?", ["CO2", "H2O", "O2", "NaCl"], 2),
            Quiz("1년은 몇 개월일까?", ["10개월", "11개월", "12개월", "13개월"], 3),
            Quiz("무지개는 몇 가지 색일까?", ["5색", "6색", "7색", "8색"], 3),
        ]
        self.best_score = 0

    def show_menu(self):
        """메뉴를 출력한다."""
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def show_quiz_list(self):
        """등록된 퀴즈 목록을 출력한다."""
        print(f"\n[퀴즈 목록] 총 {len(self.quizzes)}개")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"  {i}. {quiz.question}")

    def play(self):
        """퀴즈를 하나씩 풀고, 맞힌 개수를 점수로 계산한다."""
        score = 0
        for quiz in self.quizzes:
            quiz.show()
            try:
                user_answer = int(input("정답 번호: "))
            except ValueError:
                # 숫자가 아닌 값을 입력하면 오답으로 처리
                user_answer = 0

            if quiz.is_correct(user_answer):
                print("정답입니다! ✅")
                score += 1
            else:
                print(f"틀렸습니다! ❌ 정답은 {quiz.answer}번입니다.")

        print(f"\n결과: {len(self.quizzes)}개 중 {score}개 정답!")
        if score > self.best_score:
            self.best_score = score
            print("🎉 최고 점수를 갱신했습니다!")

    def add_quiz(self):
        """사용자에게 문제, 보기 4개, 정답 번호를 입력받아 퀴즈를 추가한다."""
        question = input("\n문제를 입력하세요: ").strip()
        if not question:
            print("문제가 비어 있어 취소합니다.")
            return

        choices = []
        for i in range(1, 5):
            choices.append(input(f"보기 {i}: ").strip())

        try:
            answer = int(input("정답 번호(1~4): "))
        except ValueError:
            print("숫자를 입력해야 합니다. 퀴즈 추가를 취소합니다.")
            return

        if answer < 1 or answer > 4:
            print("정답 번호는 1~4 사이여야 합니다. 퀴즈 추가를 취소합니다.")
            return

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다!")

    def show_score(self):
        """최고 점수를 출력한다."""
        print(f"\n최고 점수: {self.best_score}점")

    def run(self):
        """메뉴를 반복해서 보여주고, 선택한 번호에 맞게 동작한다."""
        while True:
            self.show_menu()
            choice = input("번호를 선택하세요: ")

            if choice == "1":
                self.play()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("아직 준비 중이거나 잘못된 번호입니다.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()
