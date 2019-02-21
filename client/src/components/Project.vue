<template>
  <div>
    Project {{ id }}

    {{ project }}
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Project',
  props: {
    msg: String
  },
  data() {
    return {
      search: "",
      title: "My XYZ Maps",
      project: null,
      id: this.$route.params.id,

    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/api/v1/project/' + this.id)
      .then(response => (this.project = response.data))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
