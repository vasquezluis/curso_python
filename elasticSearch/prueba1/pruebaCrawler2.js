const { Client } = require("@elastic/elasticsearch");

const client = new Client({
  node: "", // Elasticsearch endpoint
  auth: {
    apiKey: {
      // API key ID and secret
      id: "",
      api_key: "",
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
