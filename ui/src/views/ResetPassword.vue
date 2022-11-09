<template>
    <NavBar/>
    <ResetPassword/>
</template>

<script>
import ResetPassword from "@/components/ResetPassword.vue";
import NavBar from "@/components/NavBar.vue";

export default{
name: "ResetPasswordPage",
  components: {
    ResetPassword,
    NavBar
  }
};
</script>