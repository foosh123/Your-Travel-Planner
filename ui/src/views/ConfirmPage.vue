<template>
    <NavBar/>
    <Confirm/>

</template>

<script>
import Confirm from "@/components/ConfirmPage.vue";
import NavBar from "@/components/NavBar.vue";

export default{
name: "ConfirmPage",
  components: {
    Confirm,
    NavBar
  }
};
</script>
