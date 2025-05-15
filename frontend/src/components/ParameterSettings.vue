<!-- ParamsSettings.vue -->
<template>
  <div class="parameter-settings">
    <h2>首頁</h2>
    <pre></pre>
    <div>
        <button @click="selectOption('results')">新增版本</button>
    </div>



    <!-- 1110不需要使用者輸入參數，暫不動 -->
    <!--<h2>參數設定</h2>
    <form @submit.prevent="startProcess">-->
      <!-- 1110只有一個參數，可考慮動態參數配置輸入欄位 -->
      <!--<div class="form-group">
        <label>地震規模：</label>
        <input type="number" v-model="parameters.value" step="0.1">
      </div>
      <button type="submit" :disabled="processing" class="start-button">
        {{ processing ? '處理中...' : 'START' }}
      </button>
    </form>
    <div v-if="showOptions" class="options">-->
      <!-- 先前版本可選擇hospital/gatheringpoint來產生新的tab，
        1110改成一個option，避免直接刪掉option造成後續產生新的tab出錯 -->
      <!--<div>
        <button @click="selectOption('results')">查看結果</button>
      </div>
    </div>-->

    <!-- 先前版本：
      輸入三個參數後按下START，會產生兩個option，選擇其中一個後會根據option產生新的tab -->
    <!--<div class="input-group">
    <label>每一間醫院容納的卡車數量</label>
    <input type="number" v-model="capacity_hos_trucks" />
  </div>
  <div class="input-group">
    <label>每輛卡車可乘載的醫療包數量</label>
    <input type="number" v-model="capacity_truck" />
  </div>
  <div class="input-group">
    <label>每個集結點可以容納多少卡車</label>
    <input type="number" v-model="capacity_gathering_point" />
  </div>-->
    <!--<button @click="startProcess" class="start-button">START</button>

  <div v-if="showOptions" class="options">
    <div>
      <button @click="selectOption('hospital_results')">醫院與醫療包存放數量配置</button>
      <pre>{{ hospitalResults }}</pre>
    </div>
    <div>
      <button @click="selectOption('gathering_point_results')">集結點與資源分配</button>
      <pre>{{ gatheringPointResults }}</pre>
    </div>
  </div>-->
  </div>
  </template>
  
  <script>
    //需要連後端時開啟
    //import axios from 'axios';

    export default {
      name: 'ParameterSettings',
      data() {
        return {
          parameters: {
            value: 0,
          },
          showOptions: false,
          processing: false
        }
      },
      methods: {
        //1110將一個參數丟到後端運作
        //async startProcess() {
        //  this.processing = true;
        //  try {
        //    const response = await axios.post('http://localhost:5000/api/math-model', this.parameters);
        //    if (response.data.success) {
        //      this.$emit('results-updated', response.data.results);
        //    }
        //    this.showOptions = true;
        //  } catch (error) {
        //    console.error('Error:', error);
        //    alert('處理參數時發生錯誤');
        //  }
        //  this.processing = false;
        //},
        selectOption(option) {
          this.$emit('select-option', option)
        }
      }
    }

  
  </script>
  
  <style scoped>
    .parameter-settings {
      max-width: 600px;
      margin: 0 auto;
    }

/*    .input-group {
      margin-bottom: 15px;
    }*/

    .start-button {
      margin-top: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .options {
      margin-top: 30px;
      display: flex;
      justify-content: space-between;
    }
  </style>
