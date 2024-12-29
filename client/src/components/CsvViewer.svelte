<script lang="ts">
    import { onMount } from 'svelte';
    import Papa from 'papaparse';
  
    export let url = '';
    let csvContent: string[][] = [];
  
    async function fetchCsv(url: string) {
      const response = await fetch(url);
      const text = await response.text();
      const result = Papa.parse(text, { header: false });
      csvContent = result.data;
    }
  
    onMount(() => {
      fetchCsv(url);
    });
  </script>
  
  <div class="csv-container">
    <table class="csv-wrapper">
      {#each csvContent as row}
        <tr>
          {#each row as cell}
            <td>{cell}</td>
          {/each}
        </tr>
      {/each}
    </table>
  </div>
  
  <style>
    .csv-container {
      height: calc(100vh - 80px);
      overflow-y: scroll;
    }
    .csv-wrapper {
      width: 100%;
      border-collapse: collapse;
    }
    .csv-wrapper td {
      border: 1px solid #ddd;
      padding: 8px;
    }
    .csv-wrapper tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    .csv-wrapper tr:hover {
      background-color: #ddd;
    }
  </style>