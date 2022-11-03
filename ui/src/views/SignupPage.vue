<template>
    <NavBar/>
    <Signup/>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Signup from "@/components/SignupPage.vue";

export default{
name: "LoginPage",
  components: {
    NavBar,
    Signup
  }
};
</script>