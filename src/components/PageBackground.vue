<template>
  <div class="background-image"></div>
</template>

<style lang="scss" scoped>
.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: top;
  background-attachment: fixed;
  background-image: url("../assets/font.png");
  z-index: -1;
}
@media (max-width: 768px) {
  .background-image {
    background-image: url("../assets/font_mobile.png");
  }
}
</style>
