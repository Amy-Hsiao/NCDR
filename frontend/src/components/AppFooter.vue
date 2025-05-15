<template>
  <footer class="app-footer">

    <div class="tab-selector">
      <button v-for="tab in tabs"
              :key="tab"
              @click="selectTab(tab)"
              :class="{ active: currentTab === tab }">
        {{ tab }}
      </button>
    </div>
    <div class="page-info" v-text="pageinfo(currentTab)"></div>
    <!-- <div class="page-info">currentTab: {{ currentTab }}</div> -->
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
  props: {
    tabs: Array,
    currentTab: String
  },
  data() {
    return {
      pageCount: 1,
      wordCount: 0
    }
  },
  methods: {
    selectTab(tab) {
      this.$emit('select-tab', tab);
    },
    pageinfo(tab){
      if(tab !== 'Home'){
        //return `頁數: ${this.pageCount} 字數: ${this.wordCount}`;
        return `國家災害防救科技中心關心您`;
      }
      else{
        return '國家災害防救科技中心關心您'
      }
    }
  }
}
</script>

<style scoped>
.app-footer {
  background-color: #f0f0f0;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tab-selector {
  display: flex;
}

.tab-selector button {
  margin: 0 5px;
  padding: 5px 10px;
  border: none;
  background-color: #ddd;
  cursor: pointer;
}

.tab-selector button.active {
  background-color: #4CAF50;
  color: white;
}
</style>
