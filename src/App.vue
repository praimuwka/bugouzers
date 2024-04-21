<template>
  <div id="app">
    <NavMenu :navList="navItems" />
    <router-view class="router-view"/>
    <PageBackground/>
  </div>
</template>

<script setup >
import NavMenu from './components/NavMenu.vue';
import PageBackground from './components/PageBackground.vue';

const navItems = [
  { label: 'Поступи куда-то', url: '/' },
  { label: 'Мониторь абитурь', url: '/monitor' },
  { label: 'Смени вектор', url: '/transaction' },
  { label: 'Найди точку', url: '/neroute' },
  { label: 'Учись больше', url: '/learnmore' },
];
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
  margin: 0;
  padding: 0;
  z-index: 1;
}

.big_smile {
  width: 12%;
  height: 12%;
}

button {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 10;
}

.router-view {
  margin-left: 100px;
}
</style>
