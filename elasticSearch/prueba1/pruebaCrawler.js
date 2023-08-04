const { Client } = require("@elastic/elasticsearch");
const openai = require("openai");

// Set OpenAI API Key
openai.apiKey = "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";

const model = "gpt-3.5-turbo-0301";

// Connect to Elasticsearch cluster
const es_connect = async (cloudId, user, password) => {
  const client = new Client({
    cloud: {
      id: cloudId,
      auth: {
        username: user,
        password: password,
      },
    },
  });
  return client;
};

// Search Elasticsearch index and return body and URL of the result
const search = async (queryText) => {
  const cloudId =
    "ElasticChat_GPT:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRlZTgwYTRiNzU3YWM0Y2Y3YWE5MzFmMmRmZDA0YmM2NyQ2MGRlYjZiNDBlZTQ0N2I2OWU4MzJhZTRlNDg4M2JiZA==";
  const password = "mebcfCSLJiQdfMBlAT9NhwJt";
  const username = "elastic";

  const client = await es_connect(cloudId, username, password);

  // Elasticsearch query (BM25) and kNN configuration for hybrid search
  const query = {
    bool: {
      must: [
        {
          match: {
            title: {
              query: queryText,
              boost: 1,
            },
          },
        },
      ],
      filter: [
        {
          exists: {
            field: "title-vector",
          },
        },
      ],
    },
  };

  const knn = {
    field: "title-vector",
    k: 1,
    num_candidates: 20,
    query_vector_builder: {
      text_embedding: {
        model_id: "sentence-transformers__all-distilroberta-v1",
        model_text: queryText,
      },
    },
    boost: 24,
  };

  const fields = ["title", "body_content", "url"];
  const index = "search-elastic-docs";
  const { body } = await client.search({
    index,
    body: {
      query,
      knn,
      _source: false,
      size: 1,
      stored_fields: fields,
    },
  });

  const hit = body.hits.hits[0];
  const result = {
    body: hit.fields.body_content[0],
    url: hit.fields.url[0],
  };
  return result;
};

const truncateText = (text, maxTokens) => {
  const tokens = text.split(" ");
  if (tokens.length <= maxTokens) {
    return text;
  }
  return tokens.slice(0, maxTokens).join(" ");
};

// Generate a response from ChatGPT based on the given prompt
const chatGPT = async (
  prompt,
  model = "gpt-3.5-turbo",
  maxTokens = 1024,
  maxContextTokens = 4000,
  safetyMargin = 5
) => {
  // Truncate the prompt content to fit within the model's context length
  const truncatedPrompt = truncateText(
    prompt,
    maxContextTokens - maxTokens - safetyMargin
  );

  const response = await openai.complete({
    engine: model,
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: truncatedPrompt },
    ],
  });

  return response.choices[0].message.content;
};

const query = "example question"; // Replace with your query
const negResponse =
  "I'm unable to answer the question based on the information I have from Elastic Docs.";

(async () => {
  try {
    const { body, url } = await search(query);
    const prompt = `Answer this question: ${query}\nUsing only the information from this Elastic Doc: ${body}\nIf the answer is not contained in the supplied doc reply '${negResponse}' and nothing else`;
    const answer = await chatGPT(prompt);

    if (answer.includes(negResponse)) {
      console.log(`ChatGPT: ${answer.trim()}`);
    } else {
      console.log(`ChatGPT: ${answer.trim()}\n\nDocs: ${url}`);
    }
  } catch (error) {
    console.error(error);
  }
})();
