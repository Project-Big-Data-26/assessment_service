# Student Response API

Implementasi aktif berada di `app/assessment`, dengan event transaksional di SQLite. Respons terikat delivery, versi soal, populasi, grade, dan assessment. Identitas serta correctness berasal dari server. Runbook: [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

## Submit jawaban

```http
POST /api/v1/responses
Authorization: Bearer <participantToken>
Idempotency-Key: response-0001
Content-Type: application/json
```

```json
{
  "responseId": "response-0001",
  "deliveryInstanceId": "<ID dari GET items/next>",
  "selectedOptionIds": ["<ID opsi publik>"],
  "responseTimeMs": 42000,
  "answerChanges": 1
}
```

Header harus sama dengan `responseId`, 8–128 karakter. Pilot aktif mendukung satu jawaban `multiple_choice`. Numeric, essay, matching, multiple response, interactive grid dan scoring polytomous masih target; field tersebut ditolak dengan 422.

Skip eksplisit memakai `selectedOptionIds: []` dan `skipped: true`. Skor/correctness menjadi `null` dan matriks menjadi `NA`. Salah menjadi `0`; skip tidak dihitung salah.

Server menolak `isCorrect`, `studentHash`, `questionId`, `populationId`, dan field tambahan. Session peserta lain menghasilkan 404. Opsi di luar delivery ditolak dengan 422. Session selesai/kedaluwarsa dan respons kedua untuk delivery yang sama menghasilkan 409.

## Receipt dan retry

```json
{
  "responseId": "response-0001",
  "accepted": true,
  "nextItemUrl": "/api/v1/sessions/<sessionId>/items/next"
}
```

Correctness dan kunci tidak ditampilkan. Retry dengan ID/body identik menghasilkan receipt yang sama, termasuk setelah completion. Penggunaan ulang ID dengan body berbeda menghasilkan 409. Response event tidak ditimpa.

## Event internal dan timing

Event menyimpan response/delivery/session/assessment ID, population, family, grade, HMAC subject, question version/hash, opsi internal, skor, scoring policy, timing dan flag. Nama/NISN/email, kode peserta, serta bearer token tidak disimpan pada event.

`subjectHash` adalah HMAC population + kode peserta. Kode hanya dipakai saat provisioning. `responseTimeMs` internal adalah waktu server sejak delivery; klaim browser disimpan sebagai `clientResponseTimeMs` dan tidak menentukan rapid-guess exclusion.

Cutoff `rapidGuessMs` dibekukan pada assessment, default `null`. Respons rapid guess diberi flag dan dikeluarkan dari analisis. Respons setelah versi item ditahan AI tetap tercatat dengan `item_held_after_delivery` dan tidak valid untuk analisis.

Screening memilih satu **session lengkap** per peserta sesuai `first|last`; jawaban dari beberapa attempt tidak dicampur. Session incomplete dikeluarkan. Filter waktu memakai waktu completion UTC.

`soal_pretest_db.json`, `sesi_pretest.json` dan bundle `hasil_validasi` adalah data authoring/AI, bukan log siswa atau sampel IRT. Lihat [08 delivery](08_ASSESSMENT_DELIVERY_API.md) dan [07 psikometrik](07_PSYCHOMETRICS_API.md).
