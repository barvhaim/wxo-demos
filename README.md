# watsonx Orchestrate demos

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
- Run the server to start the local environment:
   ```bash
   orchestrate server start --env-file=.adk
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



