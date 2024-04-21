<template>
  <div :class="['nav-menu', { 'nav-menu--open': isOpen }]">
    <button @click="toggleMenu"
            class="nav-menu__toggle">
      <span><img class="menu-icon" alt="Menu" src="../assets/menu_icon.png"></span>
    </button>
    <nav v-if="isOpen"
         class="nav-menu__nav">
      <ul>
        <li v-for="(item, index) in navList"
            :key="index"
            class="menu-item">
          <router-link :to="item.url">{{ item.label }}</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import {
  defineProps, onMounted, onUnmounted, ref,
} from 'vue';

defineProps({
  navList: {
    type: Array,
    required: true,
    default: () => [],
  },
});

const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};
</script>

<style scoped lang="scss">
.nav-menu {
  ul {
    margin-top: 60px;
    li {
      margin-top: 20px;
    }
  };
  position: fixed;
  top: 0;
  left: 0;
  width: 72px;
  height: 100%;
  background-color: #333;
  color: white;
  transition: width 0.3s ease;
  z-index: 100;
}

.nav-menu__toggle {
  width: 20px;
  height: 20px;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 10px;
}

.nav-menu__nav {
  padding: 20px;
  ul {
    list-style: none;
    padding: 0;
    li {
      margin-bottom: 10px;
      a {
        color: white;
        text-decoration: none;
      }
    }
  }
}

.nav-menu--open {
  width: 150px;
}

.menu-icon {
  width: 37px;
  height: 37px;
}

.menu-item {
  font-size: 20pt;
}
</style>
