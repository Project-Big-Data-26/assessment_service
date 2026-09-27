require('dotenv').config({ quiet: true });
const { llmAdapter } = require('../src/services/aiAdapters');

async function main() {
  try {
    const result = await llmAdapter.healthCheck();
    console.log(`Gemini siap: provider=${result.provider}, model=${result.model}, latency=${result.latencyMs}ms`);
  } catch (error) {
    console.error(`Gemini belum siap untuk inferensi [${error.code || 'unknown'}]: ${error.message}`);
    if (error.code === 'llm_not_configured') {
      console.error('Salin .env.example menjadi .env, lalu isi GEMINI_API_KEY di file lokal tersebut.');
    } else if (error.code === 'llm_rate_limited') {
      const scope = error.rateLimitScope || 'unknown';
      const providerStatus = error.providerStatus || 'HTTP_429';
      console.error(`API key terbaca, tetapi provider membatasi request (scope=${scope}, status=${providerStatus}).`);
      console.error('Cek Usage dan Rate limits proyek yang sama di Google AI Studio; membuat key baru pada proyek yang sama tidak menambah kuota.');
    } else if (error.code === 'llm_auth_failed') {
      console.error('API key terbaca tetapi ditolak provider. Periksa key dan proyek asalnya di Google AI Studio.');
    }
    process.exitCode = 1;
  }
}

main();
