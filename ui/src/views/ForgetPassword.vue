<template>
    <NavBar/>
    <ForgetPassword/>
</template>

<script>
import ForgetPassword from "@/components/ForgetPassword.vue";
import NavBar from "@/components/NavBar.vue";

export default{
name: "ForgetPasswordPage",
  components: {
    ForgetPassword,
    NavBar
  }
};
</script>