const { Client } = require("@elastic/elasticsearch");

const client = new Client({
  node: "https://ee80a4b757ac4cf7aa931f2dfd04bc67.us-central1.gcp.cloud.es.io", // Elasticsearch endpoint
  auth: {
    apiKey: {
      // API key ID and secret
      id: "ee80a4b757ac4cf7aa931f2dfd04bc67",
      api_key: "aTF5aVFZa0J6TG5vMHF2a0oybzI6bXpoVFhMUjVUZlMyZVVDZzRDTVRUdw==",
    },
  },
});

const searchParams = {
  index: "search-elastic-docs",
  body: {
    query: {
      match: {
        field_name: "title-vector",
      },
    },
  },
};

client
  .search(searchParams)
  .then((response) => {
    console.log(response.hits.hits);
  })
  .catch((error) => {
    console.error(error);
  });
