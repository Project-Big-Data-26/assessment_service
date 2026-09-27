require('dotenv').config({ quiet: true });
const app = require('./src/app');
const { workflow } = require('./src/services/runtime');

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Assessment API listening on port ${PORT}`));
workflow.recover().catch((error) => console.error('Workflow recovery failed:', error));
