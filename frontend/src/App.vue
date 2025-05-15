<template>
  <div id="app">
    <AppHeader class="fixed-header" />
    <div class="main-container">
      <MainContent 
        :currentTab="currentTab" 
        :isRightSidebarOpen="isSidebarCollapsed"
        :isMobileView="isMobileView"
      />
      <RightSidebar
        :isCollapsed="isSidebarCollapsed"
        @toggle="toggleSidebar"
        class="fixed-right" v-if="currentTab !== 'Map'"
      />
    </div>
    <AppFooter 
      class="fixed-footer" 
      :tabs="tabs" 
      :currentTab="currentTab"
      @select-tab="selectTab" 
    />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import RightSidebar from './components/RightSidebar.vue'
import MainContent from './components/MainContent.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter,
    RightSidebar,
    MainContent
  },
  data() {
    return {
      tabs: ['Plan', 'Map'],
      currentTab: 'Plan',
      isSidebarCollapsed: false,
      isMobileView: false
    }
  },
  mounted() {
    this.checkViewport()
    window.addEventListener('resize', this.checkViewport)
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.checkViewport)
  },
  methods: {
    checkViewport() {
      this.isMobileView = window.innerWidth <= 768
    },
    toggleSidebar() {
      this.isSidebarCollapsed = !this.isSidebarCollapsed;
    },
    selectTab(tab) {
      this.currentTab = tab;
    }
  }
}
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.fixed-header, .fixed-footer {
  position: fixed;
  left: 0;
  right: 0;
  z-index: 1000;
}

.fixed-header {
  top: 0;
}

.fixed-footer {
  bottom: 0;
}

.main-container {
  display: flex;
  flex: 1;
  margin-top: 100px; /* 調整這個值以匹配 header 的高度 */
  margin-bottom: 60px; /* 調整這個值以匹配 footer 的高度 */
}

.fixed-left, .fixed-right {
  /* position: fixed; */
  margin-top: 30px; /* 調整這個值以匹配 header 的高度 */
  margin-bottom: 0px; /* 調整這個值以匹配 footer 的高度 */
}

.fixed-left {
  left: 0;
}

.fixed-right {
  right: 0;
}
</style>
