<template>
    <NavBar/>
    <Login/>

</template>

<script>
import Login from "@/components/LoginPage.vue";
import NavBar from "@/components/NavBar.vue";

export default{
name: "LoginPage",
  components: {
    Login,
    NavBar
  }
};
</script>