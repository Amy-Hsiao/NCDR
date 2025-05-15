<template>
  <main class="main-content" :class="{ 'shifted': localSidebarState  && !isMobileView }">
    <DocumentEditor v-if="currentTab === 'Plan'"
                    :content="savedPlanContent"
                    @save-content="saveContent"/>
    <MapVisualizer v-if="currentTab === 'Map'"
                       @select-option="onSelectOption" />
  </main>
</template>

<script>
import DocumentEditor from './DocumentEditor.vue'
import MapVisualizer from './MapVisualizer.vue'

export default {
  name: 'MainContent',
  props: {
    isRightSidebarCollapsed: {
      type: Boolean,
      default: false
    },
    isMobileView: {
      type: Boolean,
      default: false
    },
    currentTab: {
      type: String
      //default: ''  // 根據需求可以改成其他預設值
    }
  },
  components: {
    DocumentEditor,
    MapVisualizer
  },
  data() {
    return {
      localSidebarState: this.isRightSidebarCollapsed, // 初始化時同步 props
      savedPlanContent: ''
    }
  },
  methods: {
    onSelectOption(option) {
      const shouldCollapse = (option === "Map");
      this.$emit('toggle-sidebar', shouldCollapse);
    },
    saveContent(payload) {
      // console.log 可以觀察內容
      console.log("儲存內容：", payload);

      // 儲存 markdown 到本地變數
      this.savedPlanContent = payload.markdown;
    }
  }
}
</script>

<style scoped>
main {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.main-content {
  position: relative;
  width: 100%;
  transition: all 0.3s ease;
}

.main-content.shifted {
  width: calc(100% - 300px);  /* 假設側邊欄寬度為300px */
}

/* 移動設備樣式 */
@media (max-width: 768px) {
  .main-content {
    width: 100% !important;
  }
}
</style>
