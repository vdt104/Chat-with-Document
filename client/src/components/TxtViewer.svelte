<script lang="ts">
    import { onMount } from 'svelte';
  
    export let url = '';
    let textContent = '';
  
    async function fetchText(url: string) {
      const response = await fetch(url);
      textContent = await response.text();
    }
  
    onMount(() => {
      fetchText(url);
    });
  </script>
  
  <div class="txt-container">
    <pre class="txt-wrapper">{textContent}</pre>
  </div>
  
  <style>
    .txt-container {
      height: calc(100vh - 80px);
    }
    .txt-wrapper {
      flex: 1;
      background: #fff;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: flex-start; /* Align items to the left */
      overflow-y: scroll;
      max-height: 100%;
      white-space: pre-wrap; /* Preserve whitespace and wrap text */
      color: #000; /* Set text color to black */
    }
  </style>