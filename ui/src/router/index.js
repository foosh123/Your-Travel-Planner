import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import SignupPage from "@/views/SignupPage.vue";
import HomePage from "@/views/HomePage.vue";
import ForgetPasswordPage from "@/views/ForgetPassword.vue";
import ResetPasswordPage from "@/views/ResetPassword.vue";

const routes = [
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: '/',
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/signup",
    name: "Signup",
    component: SignupPage,
  },
  {
    path: "/forgetpassword",
    name: "ForgetPassword",
    component: ForgetPasswordPage,
  },
  {
    path: "/resetpassword",
    name: "ResetPassword",
    component: ResetPasswordPage,
  },
]
const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  export default router;
