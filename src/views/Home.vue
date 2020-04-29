<template>
  <div class="home section">
    <h1 class="title is-1">SciLifeLab Covid Data Portal</h1>

    <div class="tile is-ancestor">
      <div class="tile is-vertical">
        <div class="tile is-parent">
          <div class="tile is-child notification home-tiles is-primary">
            <p class="title">About the portal</p>
          </div>
        </div>
        <div class="tile">
          <div class="tile is-parent">
            <div class="tile is-child notification home-tiles is-info">
              <p class="title">Data management</p>
            </div>
          </div>
          <div class="tile is-parent">
            <div class="tile is-child home-tiles notification is-warning">
              <p class="title">Data</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    Contact: <a href="mailto:datacentre@scilifelab.se">datacentre@scilifelab.se</a>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
