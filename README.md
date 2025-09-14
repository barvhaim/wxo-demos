# watsonx Orchestrate demos

<img width="579" alt="Image" src="https://github.com/user-attachments/assets/20713ea5-836b-4e3b-865e-c50c6d2422c1" />

Playground for experimenting with watsonx Orchestrate.

## Prerequisites

- Python 3.11 or higher
- `uv` package manager for
  Python [here](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

## watsonx Orchestrate Setup

### Remote environment

- Sign up for a free trial (Try it free button, and log-in with your IBM
  ID) [here](https://www.ibm.com/products/watsonx-orchestrate)
- Create an API key: Click on the avatar in the top right corner, then click on "Settings", then
  click on "API details", then click on "Generate API key".
- Save the created `API key` and `Service instance URL` for later use.

### `orchestrate` CLI tool

Install `orchestrate` CLI tool:

```bash
uv sync
alias orchestrate='uv run orchestrate'
# or even shorter
alias wxo='uv run orchestrate' 
```

And run `orchestrate --help` (or `wxo --help`) to verify the installation.

### Local environment

- Get a remote environment set up.
- Get entitlement key from [MyIBM](https://myibm.ibm.com/)
- Fill up the `.adk` file in the root of the repository with the following content:
   ```
   WO_DEVELOPER_EDITION_SOURCE=myibm
   WO_ENTITLEMENT_KEY=<my_entitlement_key>
   WO_INSTANCE=<service_instance_url>
   WO_API_KEY=<wxo_api_key>
   WO_USERNAME=<your_wxo_email>
   WO_PASSWORD=<your_wxo_password_for_cp4d>
   ```
  OR you can use remote `watsonx.ai` instance for LLM:
   ```
   WO_DEVELOPER_EDITION_SOURCE=myibm
   WO_ENTITLEMENT_KEY=<my_entitlement_key>
   WATSONX_APIKEY=<my_watsonx_api_key>
   WATSONX_SPACE_ID=<my_space_id>
   ```

- Run the server to start the local environment:
   ```bash
   orchestrate server start --env-file=.adk -l # -l enables observability platform
   ```

### Attaching to a remote environment

Add the remote environment (if not already added):

```bash
orchestrate env add --name my-remote-env --url <SERVICE_INSTANCE_URL>
```

Activate the remote environment:

```bash
orchestrate env activate my-remote-env
# And paste the API key when prompted.
```

You should see something like this:

```bash
[INFO] - Environment 'my-remote-env' is now active
```

### Attach to the local environment
You can run `orchestrate env activate local` to set your environment or `orchestrate chat start` to start the UI service and begin chatting.

if you want to enable the observability platform, add `-l` to the `server start` command.

You can access the observability platform Langfuse at http://localhost:3010, username: orchestrate@ibm.com, password: orchestrate


### Stop the local environment
To stop the local environment, run:

```bash
orchestrate server stop
````

### Working with local models (optional)
#### Ollama

Model name: `virtual-model/ollama/*`

```bash
ollama pull llama3.2:latest
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

# Test ollama model
curl --request POST \
  --url http://192.168.68.59:11434/v1/chat/completions \
  --header 'content-type: application/json' \
  --data '{
  "model": "llama3.2:latest",
  "messages": [
    {
      "content": "Hi",
      "role": "user"
    }
  ]
}'
```

##### Add the model
```bash
orchestrate models import --file models/ollama.yaml
[INFO] - Successfully added the model 'virtual-model/ollama/llama3.1:8b'
```

##### Remove the model
```bash
orchestrate models remove -n virtual-model/ollama/llama3.1:8b
[INFO] - Successfully removed the model 'virtual-model/ollama/llama3.1:8b'
```

## Usage

To list all available agents in the active environment:

```bash
orchestrate agents list
```

To list all available tools in the active environment:

```bash
orchestrate tools list
```

To list all available connections in the active environment:

```bash
orchestrate connections list
```

## Demos

1. **IP Reputation Checker** - An agent that checks the reputation of IP addresses using VirusTotal

   This demo showcases an agent that can evaluate the security reputation of any IP address using
   the VirusTotal API. The agent provides detailed information about whether an IP is malicious,
   which security vendors flagged it, its geographic location, and associated threats.

   ### Setup
    1. Make sure you have a VirusTotal API key. You can sign up for free
       at [VirusTotal](https://www.virustotal.com/).
    2. Set your API key as an environment variable:
       ```bash
       export VIRUSTOTAL_API_KEY=your_api_key_here
       ```
    3. Deploy the agent and required components:
       ```bash
       ./demos/demo_1_deploy.sh
       ```

   ### Usage
   Once deployed, you can interact with the agent by providing any IP address you want to check. The
   agent will:
    - Fetch the IP's reputation data from VirusTotal
    - Analyze the security verdicts
    - Present findings in a structured format showing malicious indicators, geographic data, and
      security details

   ### Cleanup
   To remove the agent, tools, and connections created for this demo:
   ```bash
   ./demos/demo_1_clean.sh
   ```

2. **YouTube Transcriber** - An agent that creates transcripts from YouTube videos

   This demo features an agent that can extract and provide text transcripts from any YouTube video. 
   It retrieves video metadata and generates a readable transcript that captures the spoken content.

   ### Setup
    1. Deploy the agent and required components:
       ```bash
       ./demos/demo_2_deploy.sh
       ```

   ### Usage
   After deployment, you can interact with the agent by providing a YouTube URL. The agent will:
    - Extract the video information (title, channel, etc.)
    - Generate a text transcript of the video content
    - Format the transcript for readability
    - For longer videos, provide a summary of key points

   ### Cleanup
   To remove the agent, tools, and connections created for this demo:
   ```bash
   ./demos/demo_2_clean.sh
   ```

3. **Content Extractor** - An agent that extracts content from web pages

   This demo showcases an agent that can extract meaningful content from any web page URL. It
   retrieves the main text, images, and metadata, providing a structured summary of the page's
   content.

   ### Setup
    1. Deploy the agent and required components:
       ```bash
       ./demos/demo_3_deploy.sh
       ```

   ### Usage
   After deployment, you can interact with the agent by providing a URL. The agent will:
    - Fetch the web page content
    - Extract the main text, images, and metadata
    - Provide a structured summary of the page's content

   ### Cleanup
   To remove the agent, tools, and connections created for this demo:
   ```bash
   ./demos/demo_3_clean.sh
   ```
   
4. **Patents generator (WIP)** - An agent that generates patents based on a given topic

   This demo features an agent that can generate patent documents based on user-provided
   topic. It uses a template to create structured patent applications.

   ### Setup
    1. Deploy the agent and required components:
       ```bash
       ./demos/demo_4_deploy.sh
       ```

   ### Usage
   After deployment, you can interact with the agent by providing a description of the invention.
   The agent will:
    - Generate a structured patent document using the provided description
    - Format the document according to standard patent application guidelines

   ### Cleanup
   To remove the agent, tools, and connections created for this demo:
   ```bash
   ./demos/demo_4_clean.sh
   ```

5. **Procurement Assistant** - An agent that analyzes Bill of Materials (BOM) files

   This demo features a specialized agent that can interpret and answer questions about Excel-based
   Bill of Materials (BOM) files. It helps procurement teams quickly analyze component information.

   ### Setup
    1. Deploy the agent and required components:
       ```bash
       ./demos/demo_5_deploy.sh
       ```

   ### Usage
   After deployment, add the BOM manually via the Agents builder UI.
   The agent will:
    - Analyze the provided Excel BOM file
    - Answer specific questions about components, costs, quantities, etc.
    - Help identify procurement needs and opportunities

   ### Cleanup
   To remove the agent, tools, and connections created for this demo:
   ```bash
   ./demos/demo_5_clean.sh
   ```


### Notes:
- (Demo 8) Playwright MCP server over SSE: `npx @playwright/mcp@latest --port 8931 --host 0.0.0.0`

- (Demo 9) Elasticsearch MCP server over SSE: 
    ```bash
    git clone https://github.com/elastic/mcp-server-elasticsearch.git
    cd mcp-server-elasticsearch
    npm install
    npm run build
  
    HOST=0.0.0.0 uv tool run mcp-proxy --transport sse --port 9201 --host 0.0.0.0 \
      -e ES_URL http://<ES_IP>:9200 \
      -e ES_API_KEY "" \
      node /Users/barha/Desktop/IBM/projects/mcp-server-elasticsearch/dist/index.js
    ```