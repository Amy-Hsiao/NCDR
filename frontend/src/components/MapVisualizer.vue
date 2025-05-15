<template>
  <div class="map-visualizer">
    <h1>台南市地圖視覺化防救災醫療資源佈署</h1>
    <!-- 切換資訊按鈕 -->
    <div class="button-group">
      <button @click="mode = 'all'">醫療資源佈署概況</button>
      <button @click="mode = 'gathering'">集結點 🚚</button>
      <button @click="mode = 'hospital'">醫療院所 🏥</button>
    </div>
    <img class="tainan-map" src="../assets/Tainan_map.png" alt="Tainan map" />
    <!-- 顯示行政區 -->
    <template v-if="mode === 'all'">
      <div v-for="area in areaData"
           :key="area.name"
           class="label"
           :style="getLabelStyle(area.name)">
        <strong>{{ area.name }}</strong><br />
        醫療資源：{{ area.resources }}<br />
      </div>
    </template>

    <!-- 顯示集結點 -->
    <template v-if="mode === 'gathering'">
      <div v-for="point in gatheringPoints"
           :key="point.name"
           class="label gathering"
           :style="getLabelStyle(point.name)">
        🚚 {{ point.name }}<br />
        卡車數：{{ point.trucks }}
      </div>
    </template>

    <!-- 顯示醫療院所 -->
    <template v-if="mode === 'hospital'">
      <div v-for="hospital in hospitals"
           :key="hospital.name"
           class="label hospital"
           :style="getLabelStyle(hospital.name)">
        🏥 {{ hospital.name }}<br />
        醫療包：{{ hospital.medicalKits }}
      </div>
    </template>

  </div>
</template>

<script>
  export default {
    name: "MapWithData",
    data() {
      return {
        mode: null, // 控制目前顯示什麼（'gathering' | 'hospital' | null）
        areaData: [
          { name: "新營區", resources: 4342 },
          { name: "鹽水區", resources: 1283 },
          { name: "白河區", resources: 501 },
          { name: "柳營區", resources: 1742 },
          { name: "後壁區", resources: 413 },
          { name: "東山區", resources: 284 },
          { name: "麻豆區", resources: 12164 },
          { name: "下營區", resources: 2614 },
          { name: "六甲區", resources: 1253 },
          { name: "官田區", resources: 1397 },
          { name: "大內區", resources: 345 },
          { name: "佳里區", resources: 9292 },
          { name: "學甲區", resources: 4006 },
          { name: "西港區", resources: 5314 },
          { name: "七股區", resources: 3147 },
          { name: "將軍區", resources: 1844 },
          { name: "北門區", resources: 331 },
          { name: "新化區", resources: 9666 },
          { name: "新市區", resources: 7404 },
          { name: "善化區", resources: 5862 },
          { name: "安定區", resources: 8026 },
          { name: "山上區", resources: 757 },
          { name: "玉井區", resources: 177 },
          { name: "楠西區", resources: 220 },
          { name: "南化區", resources: 169 },
          { name: "左鎮區", resources: 319 },
          { name: "仁德區", resources: 21170 },
          { name: "歸仁區", resources: 19495 },
          { name: "關廟區", resources: 12509 },
          { name: "龍崎區", resources: 1408 },
          { name: "永康區", resources: 47637 },
          { name: "東區", resources: 55314 },
          { name: "南區", resources: 65479 },
          { name: "中西區", resources: 43105 },
          { name: "北區", resources: 48303 },
          { name: "安平區", resources: 74245 },
          { name: "安南區", resources: 34629 },
        ],
        gatheringPoints: [
          { name: "國立成功大學", trucks: 1200 },
          { name: "南臺科技大學", trucks: 1200 },
          { name: "台南應用科技大學", trucks: 1200 },
          { name: "崑山科技大學", trucks: 1200 },
          { name: "嘉南藥理大學", trucks: 422 },
          { name: "長榮大學", trucks: 1159 },
          { name: "中信科技大學", trucks: 1200 },
          { name: "台南藝術大學", trucks: 1200 },
        ],
        hospitals: [
          { name: "衛生福利部臺南醫院", medicalKits: 39800 },
          { name: "郭綜合醫院", medicalKits: 25600 },
          { name: "永川醫院", medicalKits: 5850 },
          { name: "洪外科醫院", medicalKits: 1150 },
          { name: "大安婦幼醫院", medicalKits: 3250 },
          { name: "永和醫院", medicalKits: 4450 },
          { name: "仁村醫院", medicalKits: 2000 },
          { name: "仁愛醫療社團法人仁愛醫院", medicalKits: 2000 },
          { name: "台灣基督長老教會新樓醫療財團法人台南新樓醫院", medicalKits: 27100 },
          { name: "台南市立醫院", medicalKits: 34300 },
          { name: "美德中醫醫院", medicalKits: 500 },
          { name: "陳澤彥婦產科醫院", medicalKits: 3050 },
          { name: "國立成功大學醫學院附設醫院", medicalKits: 67900 },
          { name: "開元寺慈愛醫院", medicalKits: 1650 },
          { name: "志誠醫院", medicalKits: 1150 },
          { name: "臺南市立安南醫院", medicalKits: 26650 },
          { name: "璟馨婦幼醫院", medicalKits: 4400 },
          { name: "高雄榮民總醫院臺南分院", medicalKits: 35450 },
          { name: "奇美醫療財團法人奇美醫院", medicalKits: 62900 },
          { name: "永達醫療社團法人永達醫院", medicalKits: 1850 },
          { name: "晉生醫療社團法人晉生慢性醫院", medicalKits: 4150 },
          { name: "衛生福利部臺南醫院新化分院", medicalKits: 4450 },
          { name: "財團法人台灣省私立台南仁愛之家附設仁馨醫院", medicalKits: 10000 },
          { name: "衛生福利部胸腔病院", medicalKits: 5100 },
          { name: "衛生福利部嘉南療養院", medicalKits: 35650 },
          { name: "吉安醫療社團法人吉安醫院", medicalKits: 1500 },
          { name: "台灣基督長老教會新樓醫療財團法人麻豆新樓醫院", medicalKits: 19650 },
          { name: "新生醫院", medicalKits: 4750 },
          { name: "奇美醫療財團法人佳里奇美醫院", medicalKits: 14350 },
          { name: "信一骨科醫院", medicalKits: 1150 },
          { name: "營新醫院", medicalKits: 6350 },
          { name: "新興醫療社團法人新興醫院", medicalKits: 4900 },
          { name: "衛生福利部新營醫院", medicalKits: 14650 },
          { name: "奇美醫療財團法人柳營奇美醫院", medicalKits: 46650 },
          { name: "宏科醫院", medicalKits: 1400 },
        ],

        // 各文字定位（你需要人工標註）
        labelPositions: {
          // 各行政區的文字定位
          "新營區": { top: "30%", left: "45%" },
          "鹽水區": { top: "32%", left: "36%" },
          "白河區": { top: "24%", left: "67%" },
          "柳營區": { top: "36%", left: "51%" },
          "後壁區": { top: "23%", left: "51%" },
          "東山區": { top: "36%", left: "66%" }, 
          "麻豆區": { top: "49%", left: "36%" },
          "下營區": { top: "42%", left: "39%" },
          "六甲區": { top: "43%", left: "55%" },
          "官田區": { top: "49%", left: "51%" },
          "大內區": { top: "57%", left: "56%" },
          "佳里區": { top: "51%", left: "26%" },
          "學甲區": { top: "40%", left: "27%" },
          "西港區": { top: "57%", left: "30%" },
          "七股區": { top: "59%", left: "17%" },
          "將軍區": { top: "46%", left: "17%" },
          "北門區": { top: "33%", left: "20%" },
          "新化區": { top: "74%", left: "49%" },
          "新市區": { top: "65%", left: "43%" },
          "善化區": { top: "57%", left: "44%" },
          "安定區": { top: "63%", left: "34%" },
          "山上區": { top: "64%", left: "53%" },
          "玉井區": { top: "62%", left: "66%" },
          "楠西區": { top: "49%", left: "74%" },
          "南化區": { top: "63%", left: "79%" },
          "左鎮區": { top: "75%", left: "59%" },
          "仁德區": { top: "90%", left: "33%" },
          "歸仁區": { top: "86%", left: "44%" },
          "關廟區": { top: "81%", left: "50%" },
          "龍崎區": { top: "88%", left: "57%" },
          "永康區": { top: "72%", left: "38%" },
          "東區": { top: "81%", left: "35%" },
          "南區": { top: "86%", left: "26%" },
          "中西區": { top: "77%", left: "22%" },
          "北區": { top: "77%", left: "34%" },
          "安平區": { top: "82%", left: "23%" },
          "安南區": { top: "66%", left: "22%" },
          // 各集結點的文字定位
          "國立成功大學": { top: "81%", left: "35%" }, //701 臺南市東區大學路1號
          "南臺科技大學": { top: "69%", left: "38%" }, //710301 台南市永康區南台街一號
          "台南應用科技大學": { top: "73%", left: "39%" }, //710302台南市永康區中正路529號
          "崑山科技大學": { top: "77%", left: "40%" }, // 710303 台南市永康區崑大路195 號
          "嘉南藥理大學": { top: "90%", left: "35%" }, //717301 臺南市仁德區二仁路一段60號
          "長榮大學": { top: "85%", left: "44%" }, //711301 台南市歸仁區長大路一號
          "中信科技大學": { top: "65%", left: "43%" }, //74448 台南市新市區中華路49號
          "台南藝術大學": { top: "49%", left: "51%" }, //720005臺南市官田區大崎里大崎66號
          // 各醫院的文字定位
          "衛生福利部臺南醫院": { top: "74%", left: "18%" }, //700007 臺南市中西區中山路125號
          "郭綜合醫院": { top: "75%", left: "24%" }, //700002 台南市中西區民生路2段22號
          "永川醫院": { top: "76%", left: "19%" }, //台南市中西區成功路169號
          "洪外科醫院": { top: "77%", left: "26%" }, //台南市中西區民生路二段60號
          "大安婦幼醫院": { top: "78%", left: "21%" }, //700臺南市中西區金華路三段167號
          "永和醫院": { top: "79%", left: "27%" }, //700台南市中西區府前路一段310號
          "仁村醫院": { top: "80%", left: "23%" }, //台南市中西區西門路一段486號
          "仁愛醫療社團法人仁愛醫院": { top: "83%", left: "39%" }, //台南市701東區北門路一段10號
          "台灣基督長老教會新樓醫療財團法人台南新樓醫院": { top: "81%", left: "37%" }, //701002 台南市東區東門路一段57號
          "台南市立醫院": { top: "84%", left: "33%" }, //701 台南市東區崇德路 670 號
          "美德中醫醫院": { top: "75%", left: "30%" }, //台南市北區公園路661號
          "陳澤彥婦產科醫院": { top: "73%", left: "27%" }, //台南市北區中華北路二段101號
          "國立成功大學醫學院附設醫院": { top: "71%", left: "24%" }, //704302 臺南市北區勝利路138號 
          "開元寺慈愛醫院": { top: "77%", left: "32%" }, //台南市北區北園街89之1號
          "志誠醫院": { top: "79%", left: "33%" }, //70448 台南市北區公園路315-1號
          "臺南市立安南醫院": { top: "66%", left: "22%" }, //台南市安南區州南里長和路二段66號
          "璟馨婦幼醫院": { top: "78%", left: "40%" }, //台南市永康區東橋七路198號
          "高雄榮民總醫院臺南分院": { top: "76%", left: "40%" }, //710011 臺南市永康區復興路427號
          "奇美醫療財團法人奇美醫院": { top: "74%", left: "38%" }, //台南市永康區中華路901號
          "永達醫療社團法人永達醫院": { top: "72%", left: "36%" }, //台南市永康區永大路2段1326號
          "晉生醫療社團法人晉生慢性醫院": { top: "70%", left: "34%" }, //台南市永康區中山南路902巷7號
          "衛生福利部臺南醫院新化分院": { top: "75%", left: "52%" }, //712009臺南市新化區那拔里牧場72號
          "財團法人台灣省私立台南仁愛之家附設仁馨醫院": { top: "71%", left: "51%" }, //712 台南市新化區中山路20號
          "衛生福利部胸腔病院": { top: "88%", left: "35%" }, //717203台南市仁德區中山路864號
          "衛生福利部嘉南療養院": { top: "92%", left: "32%" }, //717台南市仁德區裕忠路539號
          "吉安醫療社團法人吉安醫院": { top: "85%", left: "50%" }, //台南市關廟區中正路435號
          "台灣基督長老教會新樓醫療財團法人麻豆新樓醫院": { top: "49%", left: "38%" }, //721010 台南市麻豆區埤頭里麻佳路一段207號
          "新生醫院": { top: "51%", left: "24%" }, //722台南市佳里區新生路272號
          "奇美醫療財團法人佳里奇美醫院": { top: "54%", left: "26%" }, //台南市佳里區佳興里佳里興606號
          "信一骨科醫院": { top: "28%", left: "47%" }, //730台南市新營區民生路43之26號
          "營新醫院": { top: "30%", left: "39%" }, //730台南市新營區隋唐街228號
          "新興醫療社團法人新興醫院": { top: "33%", left: "42%" }, //730台南市新營區中興路10號
          "衛生福利部新營醫院": { top: "36%", left: "38%" }, //730台南市新營區信義街73號
          "奇美醫療財團法人柳營奇美醫院": { top: "38%", left: "55%" }, //736台南市柳營區太康里太康201號
          "宏科醫院": { top: "57%", left: "44%" }, //741台南市善化區南關里三民路1－35號

        }
      };
    },
    methods: {
      getLabelStyle(areaName) {
        const pos = this.labelPositions[areaName] || {};
        return {
          position: "absolute",
          top: pos.top || "0",
          left: pos.left || "0",
          color: "#000",
          fontSize: "12px",
          textAlign: "center",
          backgroundColor: "rgba(255,255,255,0.7)",
          borderRadius: "5px",
          padding: "2px 5px"
        };
      }
    }
  };
</script>

<style scoped>
  .tainan-map {
    width: 100%; /* 或設成固定值像 400px */
    /*max-width: 800px;*/ /* 避免太大 */
    height: auto; /* 讓圖片按比例縮放 */
    border-radius: 8px; /* （可選）讓圖片邊角圓滑 */
  }

  .map-container {
    position: relative;
    width: 1200px;
  }

  .map-image {
    width: 100%;
  }

  .label {
    position: absolute;
    transform: translate(-50%, -50%);
    font-size: 36px; /* 原本是 12px，可以依喜好改大一點 */
    line-height: 1.4; /* 讓文字不要太擠 */
  }

  .button-group {
    margin-bottom: 10px;
  }

  .button-group button {
    margin-right: 10px;
    padding: 6px 12px;
    font-size: 16px;
    cursor: pointer;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px

  }

  .button-group button:hover {
    background-color: #2980b9;
  }

  .label.hospital {
    background-color: rgba(255, 102, 102, 0.85);
  }

  .label.gathering {
    background-color: rgba(255, 204, 0, 0.85);
  }

</style>
