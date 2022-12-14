import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/index.js";
import axios from "axios";

const isProduction = process.env.VUE_APP_ENVIRONMENT === "production";
axios.defaults.baseURL = isProduction ? process.env.VUE_APP_PROD_BACKEND_URL : process.env.VUE_APP_DEV_BACKEND_URL;
const app = createApp(App);
app.use(router).mount('#app');
