import json
from typing import List

from edPrograms.schemas import ExamInfo


def get_total_mark(exams:List[ExamInfo]):
    mark = 0
    for i in exams:
        mark+= i.mark
    return mark
