<template>
  <aside class="right-sidebar" :class="{ 'collapsed': isCollapsed }">
    <div v-if="!isCollapsed" class="chat-area" ref="chatArea">
      <div v-for="(message, index) in chatHistory" :key="index" class="message" :class="message.sender">
        <img v-if="message.sender === 'ai'" src="../assets/ncdr_logo.png" alt="NCDR Logo" class="message-icon">
        <div class="message-content">
          {{ message.content }}
          <button v-if="message.sender === 'ai'"
                  class="copy-button"
                  @click="copyToClipboard(message.content)">
            📄
          </button>
        </div>
      </div>
    </div>
    <div v-if="!isCollapsed" class="input-area">
      <input type="text" v-model="prompt" placeholder="在這裡輸入..." @keyup.enter="submitPrompt" />
      <button @click="submitPrompt" :disabled="processing">{{ processing ? '處理中...' : '送出' }}</button>
    </div>

  <button @click="toggleSidebar" class="toggle-button">
    <span v-if="isCollapsed">★</span>
    <span v-else>&gt;</span>
  </button>

  </aside>
</template>

<script>
import axios from 'axios';

  export default {
    name: 'RightSidebar',
    data() {
      return {
        isCollapsed: false,
        //userInput: '',
        prompt: '',
        chatHistory: [],
        processing: false
      }
    },
    methods: {
      toggleSidebar() {
        this.isCollapsed = !this.isCollapsed;
        if (!this.isCollapsed) {
          this.$nextTick(this.scrollToBottom);
        }
        this.$emit('toggle')
      },
      async submitPrompt() {
        if (!this.prompt.trim()) return;

        this.processing = true;
        // 將使用者的輸入添加到歷史紀錄中
        this.chatHistory.push({ sender: 'user', content: this.prompt });

        try {
          const response = await axios.post('http://localhost:5000/api/language-model', {
            prompt: this.prompt
          });

          if (response.data.success) {
            // 將 AI 回應加入到聊天紀錄中
            this.chatHistory.push({ sender: 'ai', content: response.data.response });
          }
        } catch (error) {
          console.error('Error:', error);
          alert('處理提示詞時發生錯誤');
        }
        this.prompt = ''; // 清空 prompt
        this.processing = false;
        // 確保新的訊息出現在視窗底部
        this.$nextTick(this.scrollToBottom);
      },
      scrollToBottom() {
        this.$nextTick(() => {
          const chatArea = this.$refs.chatArea;
          if (chatArea) {
            chatArea.scrollTop = chatArea.scrollHeight;
          }
        });
      },
      copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
          alert('已複製到剪貼簿！');
        }).catch(err => {
          console.error('複製失敗:', err);
        });
      }
    },
    mounted() {
      this.$nextTick(this.scrollToBottom);
    }

  };
</script>

<style scoped>
.right-sidebar {
  position: fixed;
  right: 0;
  top: 122px; /* 調整這個值以匹配 header 的高度 */
  bottom: 45px; /* 調整這個值以匹配 footer 的高度 */
  width: 735px;
  background-color: #f9f9f9;
  transition: width 0.3s;
  display: flex;
  flex-direction: column;
  border-left: 1px solid #ddd;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  border-radius: 5px;
}

.right-sidebar.collapsed {
  width: 40px;
}

.chat-area {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  display: flex;
  margin-bottom: 10px;
  align-items: flex-start;
}

.message.user {
  justify-content: flex-end;
}

.message-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
  background-color: white;
  border-radius: 50%;
  padding: 3px;
  object-fit: contain;
}

  .message-content {
    position: relative; /* 讓內部的 copy 按鈕相對定位 */
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
  }

.user .message-content {
  background-color: #3a3f95;
  color: white;
}

.ai .message-content {
  background-color: #f0f0f0;
}

.input-area {
  padding: 10px;
  /* background: linear-gradient(to right, #8e2de2, #4a00e0); */
  background-color: #3a3f95;
  display: flex;
  align-items: center;
  border-radius: 5px;
}

.input-area input {
  flex: 1;
  margin-right: 10px;
  padding: 10px;
  border: none;
  border-radius: 20px;
  outline: none;
}

.input-area button {
  background-color: white;
  color: #3a3f95;
  border: none;
  padding: 10px 15px;
  border-radius: 20px;
  cursor: pointer;
}

.toggle-button {
  position: absolute;
  left: 2px;
  top: 22px;
  transform: translateY(-50%);
  background-color: #f9f9f9;
  border: none;
  /* border: 2px solid #ddd;*/
  /* border-right: none; */
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  /* box-shadow: -2px 0 5px rgba(0,0,0,0.1); */
  font-size: 18px;
}
  .copy-button {
    position: absolute;
    bottom: 5px;
    right: -30px;
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    color: gray;
  }

    .copy-button:hover {
      color: black;
    }

/* 桌面版樣式 */
@media (min-width: 769px) {
  .right-sidebar {
    position: fixed;
  }
}

/* 移動版樣式 */
@media (max-width: 768px) {
  .right-sidebar {
    position: fixed;
    width: 99%;
/*    right: -100%;*/
  }

}

</style>
