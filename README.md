# watsonx Orchestrate demos

Playground for experimenting with watsonx Orchestrate.

## Prerequisites
- Python 3.11 or higher
- `uv` package manager for Python [here](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

## watsonx Orchestrate Setup

### Remote environment
- Sign up for a free trial (Try it free button, and log-in with your IBM ID) [here](https://www.ibm.com/products/watsonx-orchestrate)
- Create an API key: Click on the avatar in the top right corner, then click on "Settings", then click on "API details", then click on "Generate API key".
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
