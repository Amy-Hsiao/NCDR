<!-- TabSelector.vue -->
<template>
    <div class="tab-selector">
      <div v-for="tab in tabs" :key="tab" class="tab" @click="selectTab(tab)">
        {{ tab }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TabSelector',
    props: {
      tabs: {
        type: Array,
        required: true
      }
    },
    methods: {
      selectTab(tab) {
        // 切換工作表邏輯
        this.$emit('select-tab', tab); // 發出事件，將選中的標籤傳遞給父組件
      }
    }
  }
  </script>
  
  <style scoped>
  .tab-selector {
    display: flex;
    background-color: #ccc;
  }
  .tab {
    padding: 10px;
    cursor: pointer;
  }
  </style>
