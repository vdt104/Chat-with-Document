<!-- <script lang="ts">
	import type { PageData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import PdfViewer from '$c/PdfViewer.svelte';
	import ChatPanel from '$c/chat/ChatPanel.svelte';

	export let data: PageData;

	const document = data.document;
	const documentUrl = data.documentUrl;

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming, documentId: document.id });
	}

	beforeNavigate(resetAll);
</script>

{#if data.error}
	{data.error}
{/if}

{#if document}
	<div class="grid grid-cols-3 gap-2" style="height: calc(100vh - 80px);">
		<div class="col-span-1">
			<ChatPanel documentId={document.id} onSubmit={handleSubmit} />
		</div>
		<div class="col-span-2">
			<PdfViewer url={documentUrl} />
		</div>
	</div>
{/if} -->

<script lang="ts">
	import type { PageData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import PdfViewer from '$c/PdfViewer.svelte';
	import DocxViewer from '$c/DocxViewer.svelte';
	import CsvViewer from '$c/CsvViewer.svelte';
	import TxtViewer from '$c/TxtViewer.svelte';
	import ChatPanel from '$c/chat/ChatPanel.svelte';
  
	export let data: PageData;
  
	const document = data.document;
	const documentUrl = data.documentUrl;
	const documentType = data.documentType;

	console.log('Document Type:', documentType); // Kiểm tra giá trị documentType

	function handleSubmit(content: string, useStreaming: boolean) {
	  sendMessage({ role: 'user', content }, { useStreaming, documentId: document.id });
	}
  
	beforeNavigate(resetAll);
  </script>
  
  {#if data.error}
	{data.error}
  {/if}
  
  {#if document}
	<div class="grid grid-cols-3 gap-2" style="height: calc(100vh - 80px);">
	  <div class="col-span-1">
		<ChatPanel documentId={document.id} onSubmit={handleSubmit} />
	  </div>
	  <div class="col-span-2">
		{#if documentType === 'pdf'}
		  <PdfViewer url={documentUrl} />
		{:else if documentType === 'docx'}
		  <DocxViewer url={documentUrl} />
		{:else if documentType === 'csv'}
		  <CsvViewer url={documentUrl} />
		{:else if documentType === 'txt'}
		  <TxtViewer url={documentUrl} />
		{:else}
		  <p>Unsupported file type: {documentType}</p>
		{/if}
	  </div>
	</div>
  {/if}