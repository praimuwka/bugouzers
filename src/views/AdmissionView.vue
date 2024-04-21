<template>
  <div class="page">
    <div>
      <h1 style="color: white">Потупление в университет
        <img src="../assets/bug_green.png"
             alt="smile"
             class="big_smile"></h1>
    </div>
    <div class="columns">
      <div class="column">
        <h5 style="color: white">Форма обучения
          <select v-model="selected"
                  style="width: 130px">
            <option disabled value="">Выберите один из вариантов</option>
            <option>Бюджет</option>
            <option>Комерция</option>
          </select></h5>
        <h5 style="color: white">Желаемые профессии&nbsp&nbsp&nbsp<input v-model="jobbs"
                                                                         style="width: 130px"
                                                                         type="text"></h5>
        <div v-for="(item, index) in subjects"
             :key="index">
          <h5 style="color: white">Предмет {{index +1 }}
            <select v-model="item.name" style="width: 120px">
              <option disabled value="">Выберите один из вариантов</option>
              <option>Обществознание</option>
              <option>Русский язык</option>
              <option>Математика</option>
              <option>Информатика</option>
              <option>Физика</option>
              <option>Английский язык</option>
            </select>
            <input v-model="item.mark"
                   type="number"
                   name="balls"
                   style="width: 40px"
                   id="ball_input">
          </h5>
        </div>
        <button @click="plus" style="position: relative">Добавить предмет</button>
        <button @click="execuuute" style="position: relative">Подобрать учебные программы</button>
      </div>
      <div class="column" style="width: 70%;">
        <div v-for="item in data"
             :key="item.id"
             class="plashka">
          <h3>{{ item.Направление }}</h3>
          <h4>{{ item['Предмет 1'] }}: {{ item['Мин. балл 1'] }}</h4>
          <h4>{{ item['Предмет 2'] }}: {{ item['Мин. балл 2'] }}</h4>
          <h4>{{ item['Предмет 3'] }}: {{ item['Мин. балл 3'] }}</h4>
          <h4 v-if="selected_temp !== 'Бюджет'">Цена: {{ item.Цена }}</h4>
          <h4 v-if="selected_temp !== 'Бюджет'">Конкурс (чел/место): {{ item.КЦП_К }}</h4>
          <h4 v-else>Конкурс (чел/место): {{ item.КЦП_Б }}</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Ref, ref } from 'vue';
import { EntrantSchema, ExamInfo, ExamNameEnum, ValidationError, HTTPValidationError, ExamAdditionalInfo } from '../models/features';
import useGetData from '../hooks/hook';
const { data, loading, error, post } = useGetData();

// Fetch programs on component mount

const selected = ref<String>('Бюджет');
const selected_temp = ref<String>('Бюджет');
const jobbs = ref<String>('');

const arr : Array<ExamInfo|null> = new Array({ name: 'Математика', mark: 100 },
  { name: 'Русский язык', mark: 100 }, { name: 'Информатика', mark: 100 });
const subjects = ref(arr);

const arrrr : Array<ExamInfo|null> = new Array(0);
const subjects_temp = ref(arrrr);

const plus = () => {
  subjects.value.push({ name: 'Математика', mark: 0 });
}

const execuuute = () => {
  const inp : EntrantSchema = new Object() as EntrantSchema;
  subjects_temp.value = [...subjects.value];
  selected_temp.value = selected.value;
  // inp.jobs = jobbs.value.split(', ');
  // inp.price = 1000000;
  inp.exams = subjects.value;
  inp.is_budget = selected.value === 'Бюджет' ? true : false;
  post(inp, 'http://praimuwka.ru:5000/programs/getPrograms');
}
</script>

<style lang="scss">
.columns {
  width: 100%; /* Ensures the container takes up the full width */
}

.column {
  width: 25%; /* Each column takes up half the width of the container */
  float: left; /* Floats the columns to the left */
  padding: 10px;
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

.plashka {
  margin: 20px;
  padding: 20px;
  display: grid;
  justify-items: start;
  background-color: white;
  color: black;
  h4 {
    margin: 5px; /* Removes default margin */
    padding: 0; /* Removes default padding */
  }
}
</style>
