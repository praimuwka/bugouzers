import json

import httpx


class GPTClient:
    catalogue_addr = "b1gkeqvltalt7vitsmnt"
    _API_KEY = "AQVN1t1sX7UhjvX6y9SHWhz9fNzxwGpJh1XTdfL9"
    _BASE_URL: str = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    _PROMPT_JOB: str = "Ты - преподаватель с опытом и пониманием учебных программ, а также опытный рекрутёр." \
                       "Входные данные: строка с названием направления обучения" \
                       "Формат выходных данных: список из ТРЁХ профессий ЧЕРЕЗ ЗАПЯТУЮ, куда студент сможет устроиться после обучения"
    _PROMPT_COMPARE_SPECS: str = "ВХОДНЫЕ ДАННЫЕ:кратко, до 200 символов. Сделай их сравнение преспективности, ВЫБЕРИ НАИБОЛЕЕ ПЕРСПЕКТИВНОЕ" \
                                 "Формат выходных данных: совет, наставление. Опиши перспективы каждого из направлений. Краткий вывод. Давай КОНКРЕТНЫЙ ответ без оценки"
    headers = {
        "Authorization": f"Api-Key {_API_KEY}"
    }
    _content_json = {
        "modelUri": f"gpt://{catalogue_addr}/yandexgpt-lite/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": None
            },
            {
                "role": "user",
                "text": ""
            }
        ]
    }

    @property
    def client(self):
        return httpx.AsyncClient(base_url=self._BASE_URL, headers=self.headers, timeout=10.0)

    async def get_appropriate_jobs(self, program):
        async with self.client as client:
            self._content_json["messages"][0]["text"] = self._PROMPT_JOB
            self._content_json["messages"][1]["text"] = program
            response = await client.post(self._BASE_URL, json=self._content_json)
            return json.loads(response.text)["result"]["alternatives"][0]["message"]["text"]

    async def compare_specs(self, spec1, spec2):
        async with self.client as client:
            self._content_json["messages"][0]["text"] = self._PROMPT_COMPARE_SPECS
            self._content_json["messages"][1]["text"] = f"{spec1}, {spec2}"
            response = await client.post(self._BASE_URL, json=self._content_json)
            return json.loads(response.text)["result"]["alternatives"][0]["message"]["text"]
