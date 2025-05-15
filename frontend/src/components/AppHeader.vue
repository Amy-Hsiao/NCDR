<template>
  <header>
    <div class="top-bar">
      <div class="icon save-icon"></div>
      <!--<div class="icon return-icon"></div>-->
      <div class="title">災害防救計畫</div>
      <div class="icon refresh-icon"></div>
    </div>
    <div class="toolbar">
      <img src="../assets/ncdr_logo.png" alt="NCDR Logo" />
      <h1>國家災害防救科技中心</h1>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>

<style scoped>
.top-bar {
  background-color: #3a3f95;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  color: white;
}

.icon {
  width: 24px;
  height: 24px;
  background-size: contain;
  background-repeat: no-repeat;
}
/* 
.save-icon {
  background-image: url('../assets/save-icon.png');
}

.return-icon {
  background-image: url('../assets/return-icon.png');
}

.refresh-icon {
  background-image: url('../assets/refresh-icon.png');
} */

.title {
  text-align: center;
  font-size: 20px;
}

.toolbar {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.toolbar img {
  height: 40px;
  margin-right: 10px;
}
</style>
