<template>
  <div>
    Space -{{ id }}.
    {{ title }}
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Space',
  props: {
    msg: String
  },
  data() {
    return {
      search: "",
      title: "My XYZ Maps",
      id: this.$route.params.id,
      space: null

    }
  },
  mounted () {
    axios
      .get('https://xyz.api.here.com/hub/spaces/'+this.id)
      .then(response => (this.space = response.data))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
