import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/index.js";

const cors = require('cors');

const app = createApp(App);
app.use(cors());
app.use(router).mount('#app');
