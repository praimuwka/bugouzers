<template>
  <div class="page">
    <div>
      <h1 style="color: white">Перевод <del>стрéлок</del> на другое направление
        <img src="../assets/bug_pink.png"
             alt="smile"
             class="big_smile"></h1>
    </div>
      <div >
        <div class="column">
          <h5 style="color: white"> На какой программе вы учились?
            <select v-model="selected" style="width: 300px">
              <option v-for="(item, index) in subjects1"
                      :key="index">
                {{item.Название}}
              </option>
            </select>
          </h5>
          <h5 style="color: white"> Сколько семестров отучились?
            <input v-model="sems"
                   type="number"
                   name="sems"
                   style="width: 40px"
                   id="pox_id">
          </h5>
          <button @click="second" style="position: relative">Подобрать подходящие программы для перевода</button>
      </div>
      <div class="column" style="width: 70%;">
        <div v-for="item in subjects2"
             :key="item.id"
             class="plashka1">
          <h3>Программа: {{ item.name }}</h3>
          <h4>Потребуется досдать дисциплин: {{item.exams_number}}</h4>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { EntrantSchema, ExamAdditionalInfo } from '../models/features';
import useGetData from '../hooks/hook';
import { onMounted, ref } from 'vue';

const { data, loading, error, post } = useGetData();

const arr : Array<EntrantSchema|null> = [];
const subjects1 = ref(arr);

const arr2 : Array<ExamAdditionalInfo|null> = [];
const subjects2 = ref(arr2);

const selected = ref('');
const sems = ref(0);

const first = () => {
  post(selected.value, 'http://praimuwka.ru:5000/firstUrl');
  // subjects1.value = [...data];
  subjects1.value = [{Название: 'Перая программа'}, {Название: 'Вторая программа'}]
}

const second = () => {
  // post({name: selected.value, semesters: sems.value}, 'http://praimuwka.ru:5000/secondUrl');
  // subjects2.value = [...data];
  subjects2.value = [{name: 'Подготовка работников мака', exams_number: 5}];

}

onMounted(()=> {
  first();
})
</script>

<style scoped lang="scss">
.column {
  width: 25%; /* Each column takes up half the width of the container */
  float: left; /* Floats the columns to the left */
  padding: 10px;
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

.plashka1 {
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
