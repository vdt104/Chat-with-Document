<script lang="ts">
  import { onMount } from 'svelte';
  import { renderAsync } from 'docx-preview';

  export let url = '';
  let docContainer: HTMLDivElement;

  async function renderDoc(url: string) {
      const response = await fetch(url);
      const arrayBuffer = await response.arrayBuffer();
      await renderAsync(arrayBuffer, docContainer);
  }

  onMount(() => {
      renderDoc(url);
  });
</script>

<div class="doc-container">
  <div bind:this={docContainer} class="doc-wrapper" />
</div>

<style>
  .doc-container {
      height: calc(100vh - 80px);
  }
  .doc-wrapper {
      flex: 1;
      background: #fff;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      overflow-y: scroll;
      max-height: 100%;
  }
</style>