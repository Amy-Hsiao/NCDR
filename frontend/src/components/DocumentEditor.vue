<template>
  <div class="document-editor">
    <textarea
      v-model="markdownInput"
      placeholder="輸入 Markdown 內容..."
      class="markdown-editor"
    ></textarea>
    <div class="markdown-preview" v-html="renderedMarkdown"></div>
    <button class="floating-save-button" @click="saveContent">儲存</button>
    <button class="floating-download-button" @click="downloadContent">↧</button>
  </div>
</template>

<script>
  import { marked } from "marked";
  export default {
    name: 'DocumentEditor',
    props: {
      content: {
        type: String,
        default: ''
      }
    },
    data() {
      return {
        markdownInput: "",
        savedContent: null,
      }
    },
    methods: {
      updateContent(event) {
        this.currentContent = event.target.innerHTML;
      },
      saveContent() {
        //this.$emit('save-content', this.version, this.currentContent);
        // 將內容保存到變數中
        this.savedContent = {
          markdown: this.markdownInput,
          timestamp: new Date().toISOString(), // 加入保存時間戳
        };
        alert("內容已儲存！");
        this.$emit('save-content', this.savedContent);
      },
      downloadContent() {
        //this.$emit('download-content', this.version, this.currentContent);
        if (!this.savedContent) {
          alert("請先儲存內容！");
          return;
        }

        // 將內容轉換為 JSON 格式
        const jsonContent = JSON.stringify(this.savedContent, null, 2);

        // 創建下載鏈接
        const blob = new Blob([jsonContent], { type: "application/json" });
        const url = URL.createObjectURL(blob);

        // 創建虛擬的 <a> 標籤以觸發下載
        const link = document.createElement("a");
        link.href = url;
        link.download = "markdown_content.json";
        link.click();

        // 釋放 URL 資源
        URL.revokeObjectURL(url);
      },
      getHeaders(data) {
        return data.length > 0 ? Object.keys(data[0]) : [];
      }
    },
    mounted() {
      this.markdownInput = this.content;
    },
    computed: {
      renderedMarkdown() {
        // 使用 marked 渲染 Markdown
        return marked(this.markdownInput);
      },
    },
    watch: {
      content(newVal) {
        this.markdownInput = newVal;
      }
    },
  }
</script>

<style scoped>
  .document-editor {
    display: flex;
    justify-content: center;
    padding: 20px;
    margin: 10mm auto;
    position: relative;
  }

  .markdown-editor {
    width: 45%;
    min-height: 500px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: none;
  }

  .markdown-preview {
    width: 45%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background: #f9f9f9;
  }

  .a4-page {
    width: 200mm;
    min-height: 297mm;
    padding: 20mm;
    margin: 10mm auto;
    border: 1px #D3D3D3 solid;
    border-radius: 5px;
    background: white;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    
  }

    .a4-page:focus {
      outline: none;
    }

  .floating-save-button {
    position: fixed;
    top: 151px;
    left: 50px;
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }

    .floating-save-button:hover {
      background-color: #45a049;
    }

  .floating-download-button {
    position: fixed;
    top: 151px;
    left: 20px;
    padding: 5px 10px;
    background-color: #C7161D;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }

    .floating-download-button:hover {
      background-color: #aa151a;
    }
</style>
