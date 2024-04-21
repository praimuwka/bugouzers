import json


class ProgramsParser:
    def __init__(self, entrant_data, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.plans_list = json.load(file)
        self.entrant_data = entrant_data
        self.total_mark = sum([i.mark for i in self.entrant_data.exams])

    def check_marks(self,programs,plan, required_marks):
        print(plan, required_marks)
        for exam in self.entrant_data.exams:
            exam_min = required_marks.get(exam.name, -1)
            if exam_min == -1 or exam.mark < exam_min:
                return 0
        programs.append(plan)
    def get_education_programs(self) -> list:
        programs = []
        print(self.entrant_data.is_budget)
        for plan in self.plans_list:
            required_exams_info = {
                plan["Предмет 1"]: plan.get("Мин. балл 1"),
                plan["Предмет 2"]: plan.get("Мин. балл 2"),
                plan["Предмет 3"]: plan.get("Мин. балл 3")
            }
            if self.entrant_data.is_budget:
                if not self.entrant_data.is_budget and plan["Цена"] > self.entrant_data.price:
                    print("Слишком низкая цена")
                    continue
                if plan["Балл"] - self.total_mark>10:
                        print("Низкий балл")
                        continue
                self.check_marks(programs,plan,required_exams_info)
            if not self.entrant_data.is_budget:
                self.check_marks(programs, plan, required_exams_info)
        return programs
