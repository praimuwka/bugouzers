import csv

from const import SPECS_PATH, PLAN_STRINGS_PATH


def get_all_programms():
    programms = set()
    with open(SPECS_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # programms.add(row["Title"].split()[0])
            programms.add(row["Title"])
    return programms


def get_disciplines(spec_name: str, is_subject=False):
    with open(SPECS_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        ids = []
        for row in reader:
            if row["Title"] == spec_name:
                ids.append(row["ID"])

        with open(PLAN_STRINGS_PATH, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            disciplines = []
            for id in ids:
                for row in reader:
                    if row["type"] != "subject" and is_subject:
                        continue
                    if row["planId"] == id:
                        disciplines.append({"id": row["id"], "subject": row["subject"]})

        return disciplines



def get_new_subj(old, new):
    result = []
    for i in new:
        flag = 0
        for j in old:
            if i["subject"] == j["subject"]:
                flag = 1
                break
        if flag:result.append(i)
    return result


