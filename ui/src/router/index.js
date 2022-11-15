import { createRouter, createWebHistory } from "vue-router";
import ConfirmPage from "@/views/ConfirmPage.vue";
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
  {
    path: '/',
    name: "HomePage",
    component: HomePage,
  },
]

// https://www.digitalocean.com/community/tutorials/vuejs-advanced-vue-routing
const router = createRouter({
    // history: createWebHistory(),
    routes,
});

router.addRoute(
  {
    path: "/confirm/:token?",
    name: "ConfirmPage",
    component: ConfirmPage,
  },
);

export default router;
