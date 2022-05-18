<template>
  <div>
    <div v-for="item in court">
      {{ item }}
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      court: [1, 1, 1, 1, 1]
    };
  }
};
</script>
