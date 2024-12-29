// import type { PageLoad } from './$types';
// import { api, getErrorMessage } from '$api';

// export const load = (async ({ params }) => {
// 	try {
// 		const {
// 			data: { pdf, download_url }
// 		} = await api.get(`/pdfs/${params.id}`);

// 		return {
// 			document: pdf,
// 			documentUrl: download_url
// 		};
// 	} catch (err) {
// 		return {
// 			error: getErrorMessage(err)
// 		};
// 	}
// }) satisfies PageLoad;

import type { PageLoad } from './$types';
import { api, getErrorMessage } from '$api';

export const load = (async ({ params }) => {
  try {
    const {
      data: { pdf, download_url }
    } = await api.get(`/pdfs/${params.id}`);
    
    console.log('Loaded Page Data:', params);

    return {
      document: pdf,
      documentUrl: download_url,
      documentType: pdf.name.split('.').pop() // Lấy phần mở rộng của file
    };
  } catch (err) {
    return {
      error: getErrorMessage(err)
    };
  }
}) satisfies PageLoad;